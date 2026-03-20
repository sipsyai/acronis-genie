"""
FastAPI backend for Acronis Cyber Protect Cloud Assistant chat UI.
Serves chat UI and provides RAG-powered Q&A via ClaudeSDKClient.
Chat history persisted to PostgreSQL.
"""

import agent.sdk_patch  # noqa: F401 — must be first

import asyncio
import asyncpg
import httpx
import json
import logging
import time
import uuid

logger = logging.getLogger("acronis.api")
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from pathlib import Path
from sse_starlette.sse import EventSourceResponse
from claude_code_sdk import (
    ClaudeSDKClient,
    ClaudeCodeOptions,
    AssistantMessage,
    ResultMessage,
    TextBlock,
)
from agent.server import get_server, get_tool_names

DB_DSN = "postgresql://acronis:acronis@localhost:5432/acronis_agent"
EMBED_URL = "http://192.168.1.8:8011/v1/embeddings"
RERANK_URL = "http://192.168.1.8:8012/rerank"

SYSTEM_PROMPT = """\
You are the Acronis Cyber Protect Cloud Assistant, a professional support agent for Acronis Cyber Protect Cloud (version 26.02).

## Language
Respond in the same language the user writes in. All documentation is in English — translate concepts naturally when responding in other languages.

## How to answer
1. ALWAYS search documentation first using the search_docs tool before answering.
2. Base your answer ONLY on the retrieved documentation chunks. Never use outside knowledge or assumptions.
3. If retrieved chunks have low relevance (reranker score below 0.30) or the topic is clearly outside Acronis Cyber Protect Cloud scope, respond: "I don't have documentation about that topic. Please check the Acronis Knowledge Base at https://kb.acronis.com or contact Acronis Support."
4. If the question is partially covered, answer what you can and clearly state what information is not available.

## Answer format
- Use **bold** for key terms, product names, and important actions.
- Use numbered lists for step-by-step instructions.
- Use `code blocks` for CLI commands, paths, and configuration values.
- End every answer with source citation on a new line: **Source:** `source_file`

## Completeness rules
- For how-to questions: include EVERY step mentioned in the documentation. Do not skip steps to be brief.
- For limitation/requirement questions: list ALL items. If the doc lists 7 unsupported features, list all 7.
- For CLI/command questions: include the EXACT command syntax and parameters from the documentation.
- For version/OS questions: include ALL version numbers and specific OS names.
- If a table exists in the source, present ALL rows — do not summarize tables.
- Completeness > brevity for technical documentation.

## Reading documentation carefully
- Read the ENTIRE retrieved documentation before answering, not just the first few sentences.
- If the documentation contains the answer, provide it — do not say "the context does not contain" unless you have read every word and it truly is not there.
- Tables, lists, and bullet points at the END of a chunk are just as important as text at the beginning.
- If the documentation is long, extract ALL relevant details — do not summarize by omitting specifics.

## Guardrails
- NEVER invent features, settings, or procedures not in the documentation.
- NEVER guess version numbers, system requirements, or compatibility information.
- NEVER guess CLI parameter names, flags, or command syntax. Only provide exact parameters found in the documentation.
- NEVER guess registry paths, port numbers, or configuration file locations.
- When you see a truncated text ending with "...", do NOT try to complete it — acknowledge it is incomplete.
- If the exact parameter/command is not in the retrieved documentation, say: "The specific command syntax is not available in the documentation I found. Please refer to [source file] for exact parameters."
- If asked about pricing, licensing, or account-specific issues, direct to Acronis sales/support.
- If asked about topics completely unrelated to Acronis, politely decline.

## Q&A matches
When search results contain a [Q&A MATCH], use that answer directly — it has been verified against the documentation. You may rephrase slightly for natural conversation but do not add information beyond what the Q&A answer provides. Always include the source citation.\
"""

MAX_HISTORY_TURNS = 5

app = FastAPI(title="Acronis Cyber Protect Assistant")

STATIC_DIR = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# Connection pool
_pool: asyncpg.Pool | None = None


async def get_pool() -> asyncpg.Pool:
    global _pool
    if _pool is None:
        _pool = await asyncpg.create_pool(DB_DSN, min_size=2, max_size=5)
    return _pool


@app.on_event("shutdown")
async def shutdown():
    global _pool
    if _pool:
        await _pool.close()


# ── DB helpers ──────────────────────────────────────────────

async def db_get_or_create_session(session_id: str | None) -> str:
    pool = await get_pool()
    async with pool.acquire() as conn:
        if session_id:
            exists = await conn.fetchval(
                "SELECT id FROM chat_sessions WHERE id = $1", session_id
            )
            if exists:
                await conn.execute(
                    "UPDATE chat_sessions SET updated_at = NOW() WHERE id = $1", session_id
                )
                return session_id

        new_id = session_id or str(uuid.uuid4())
        await conn.execute(
            "INSERT INTO chat_sessions (id) VALUES ($1) ON CONFLICT DO NOTHING", new_id
        )
        return new_id


async def db_get_history(session_id: str) -> list[dict]:
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch(
            """SELECT role, content FROM chat_messages
               WHERE session_id = $1 ORDER BY created_at DESC LIMIT $2""",
            session_id, MAX_HISTORY_TURNS * 2,
        )
        # Reverse to chronological order
        return [{"role": r["role"], "content": r["content"]} for r in reversed(rows)]


async def db_save_message(session_id: str, role: str, content: str, sources: list = None):
    pool = await get_pool()
    async with pool.acquire() as conn:
        await conn.execute(
            """INSERT INTO chat_messages (session_id, role, content, sources)
               VALUES ($1, $2, $3, $4)""",
            session_id, role, content, json.dumps(sources or []),
        )
        await conn.execute(
            """UPDATE chat_sessions
               SET updated_at = NOW(), message_count = message_count + 1
               WHERE id = $1""",
            session_id,
        )


# ── Prompt builder ──────────────────────────────────────────

def _build_context_prompt(history: list[dict], current_question: str) -> str:
    if not history:
        return current_question
    context_lines = []
    for msg in history:
        role = msg["role"].capitalize()
        context_lines.append(f"{role}: {msg['content']}")
    context_lines.append(f"User: {current_question}")
    return (
        "Here is the recent conversation history:\n\n"
        + "\n\n".join(context_lines)
        + "\n\nRespond to the latest user message. Use search_docs if needed."
    )


# ── Models ──────────────────────────────────────────────────

class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None


class SourceInfo(BaseModel):
    title: str
    file: str
    score: float
    doc_url: str | None = None


class ChatResponse(BaseModel):
    answer: str
    sources: list[SourceInfo]
    session_id: str


class NewChatRequest(BaseModel):
    session_id: str | None = None


# ── Endpoints ───────────────────────────────────────────────

@app.get("/")
async def root():
    return FileResponse(str(STATIC_DIR / "index.html"))


@app.get("/api/health")
async def health():
    chunks_count = 0
    web_chunks_count = 0
    sessions_count = 0
    messages_count = 0
    try:
        pool = await get_pool()
        async with pool.acquire() as conn:
            chunks_count = await conn.fetchval("SELECT count(*) FROM chunks")
            try:
                web_chunks_count = await conn.fetchval("SELECT count(*) FROM web_chunks")
            except Exception:
                pass
            sessions_count = await conn.fetchval("SELECT count(*) FROM chat_sessions")
            messages_count = await conn.fetchval("SELECT count(*) FROM chat_messages")
    except Exception:
        pass

    gpu_embed = False
    gpu_rerank = False
    async with httpx.AsyncClient(timeout=3.0) as client:
        try:
            r = await client.get("http://192.168.1.8:8011/health")
            gpu_embed = r.status_code == 200
        except Exception:
            pass
        try:
            r = await client.get("http://192.168.1.8:8012/health")
            gpu_rerank = r.status_code == 200
        except Exception:
            pass

    return {
        "status": "ok",
        "chunks_count": chunks_count,
        "web_chunks_count": web_chunks_count,
        "chat_sessions": sessions_count,
        "chat_messages": messages_count,
        "gpu_embedding": gpu_embed,
        "gpu_reranker": gpu_rerank,
    }


@app.post("/api/chat/new")
async def new_chat(req: NewChatRequest | None = None):
    new_id = str(uuid.uuid4())
    pool = await get_pool()
    async with pool.acquire() as conn:
        await conn.execute("INSERT INTO chat_sessions (id) VALUES ($1)", new_id)
    return {"session_id": new_id}


@app.get("/api/chat/history/{session_id}")
async def get_chat_history(session_id: str):
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch(
            """SELECT role, content, sources, created_at
               FROM chat_messages WHERE session_id = $1
               ORDER BY created_at""",
            session_id,
        )
    return {
        "session_id": session_id,
        "messages": [
            {
                "role": r["role"],
                "content": r["content"],
                "sources": json.loads(r["sources"]) if r["sources"] else [],
                "created_at": r["created_at"].isoformat(),
            }
            for r in rows
        ],
    }


@app.get("/api/chat/sessions")
async def list_sessions():
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch(
            """SELECT s.id, s.created_at, s.updated_at, s.message_count,
                      (SELECT content FROM chat_messages
                       WHERE session_id = s.id AND role = 'user'
                       ORDER BY created_at LIMIT 1) AS first_question
               FROM chat_sessions s
               ORDER BY s.updated_at DESC LIMIT 20"""
        )
    return {
        "sessions": [
            {
                "id": r["id"],
                "created_at": r["created_at"].isoformat(),
                "updated_at": r["updated_at"].isoformat(),
                "message_count": r["message_count"],
                "title": (r["first_question"] or "New Chat")[:60],
            }
            for r in rows
        ]
    }


# ── Direct search (no SDK, for streaming) ──────────────────

EMBED_MODEL = "Qwen/Qwen3-Embedding-4B"
QA_MATCH_THRESHOLD = 0.80
COSINE_THRESHOLD = 0.40
RERANKER_THRESHOLD = 0.20


async def _direct_search(question: str) -> dict:
    """Search Q&A pairs + chunks directly. Returns {type, answer?, sources, chunks}."""
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.post(EMBED_URL, json={"input": question, "model": EMBED_MODEL})
        resp.raise_for_status()
        embedding = resp.json()["data"][0]["embedding"]

    emb_str = "[" + ",".join(str(float(x)) for x in embedding) + "]"

    pool = await get_pool()
    async with pool.acquire() as conn:
        # Tier 1: Q&A match
        qa_row = await conn.fetchrow(
            """SELECT question, ideal_answer, source_file, section, doc_url,
                      1 - (embedding <=> $1::vector) AS similarity
               FROM qa_pairs WHERE embedding IS NOT NULL
               ORDER BY embedding <=> $1::vector LIMIT 1""",
            emb_str,
        )
        if qa_row and float(qa_row["similarity"]) >= QA_MATCH_THRESHOLD:
            src = qa_row["source_file"] or ""
            title = src.split("/")[-1].replace(".md", "").replace("-", " ").title() if "/" in src else src
            return {
                "type": "qa_match",
                "answer": qa_row["ideal_answer"],
                "similarity": float(qa_row["similarity"]),
                "sources": [{"title": title, "file": src, "score": float(qa_row["similarity"]), "doc_url": qa_row.get("doc_url")}],
            }

        # Tier 2: Chunk search (local + web merged)
        chunk_rows = await conn.fetch(
            """SELECT title, section, content, source_file, doc_url,
                      'local_doc' AS source_type,
                      1 - (embedding <=> $1::vector) AS similarity
               FROM chunks ORDER BY embedding <=> $1::vector LIMIT 10""",
            emb_str,
        )
        web_rows = await conn.fetch(
            """SELECT page_title AS title, section_heading AS section,
                      content, page_slug AS source_file, page_url AS doc_url,
                      'web_doc' AS source_type,
                      1 - (embedding <=> $1::vector) AS similarity
               FROM web_chunks ORDER BY embedding <=> $1::vector LIMIT 10""",
            emb_str,
        )
        rows = sorted(
            list(chunk_rows) + list(web_rows),
            key=lambda r: float(r["similarity"]), reverse=True,
        )[:10]

    candidates = [r for r in rows if float(r["similarity"]) >= COSINE_THRESHOLD]
    if not candidates:
        return {"type": "no_results", "sources": [], "chunks": []}

    # Rerank
    texts = [r["content"][:2000] for r in candidates]
    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post(RERANK_URL, json={"query": question, "texts": texts})
            resp.raise_for_status()
            rr_results = resp.json()
    except Exception:
        # Fallback: use cosine order if reranker fails
        rr_results = [{"index": i, "score": float(r["similarity"])} for i, r in enumerate(candidates)]

    scored = []
    for rr in rr_results:
        r = candidates[rr["index"]]
        scored.append({
            "title": r["title"],
            "section": r["section"],
            "content": r["content"],
            "source_file": r["source_file"],
            "doc_url": r.get("doc_url"),
            "source_type": r.get("source_type", "local_doc"),
            "cosine": float(r["similarity"]),
            "reranker": float(rr["score"]),
        })
    scored.sort(key=lambda x: x["reranker"], reverse=True)
    top3 = [s for s in scored if s["reranker"] >= RERANKER_THRESHOLD][:3]

    if not top3:
        return {"type": "no_results", "sources": [], "chunks": []}

    sources = []
    for s in top3:
        sf = s["source_file"]
        title = sf.split("/")[-1].replace(".md", "").replace("-", " ").title() if "/" in sf else sf
        sources.append({"title": title, "file": sf, "score": s["reranker"],
                        "doc_url": s.get("doc_url"), "source_type": s.get("source_type", "local_doc")})

    return {"type": "chunks", "sources": sources, "chunks": top3}


def _build_rag_prompt(question: str, history: list[dict], chunks: list[dict]) -> str:
    """Build prompt with retrieved context for Claude."""
    context_parts = []
    for c in chunks:
        context_parts.append(
            f"[Source: {c['source_file']}] {c['title']}\n{c['content'][:1000]}"
        )
    context = "\n\n---\n\n".join(context_parts)

    history_text = ""
    if history:
        lines = []
        for msg in history:
            lines.append(f"{msg['role'].capitalize()}: {msg['content']}")
        history_text = "Recent conversation:\n" + "\n".join(lines) + "\n\n"

    return (
        f"{history_text}"
        f"Documentation context:\n{context}\n\n"
        f"User question: {question}\n\n"
        f"Answer based ONLY on the documentation context above."
    )


# ── RAG pipeline helpers (shared by _direct_search and streaming) ──

async def _embed_query(question: str) -> list[float]:
    """Get embedding from remote GPU server."""
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.post(EMBED_URL, json={"input": question, "model": EMBED_MODEL})
        resp.raise_for_status()
        return resp.json()["data"][0]["embedding"]


async def _search_qa_match(conn, emb_str: str):
    """Check Q&A pairs for a high-confidence match. Returns row or None."""
    return await conn.fetchrow(
        """SELECT question, ideal_answer, source_file, section, doc_url,
                  1 - (embedding <=> $1::vector) AS similarity
           FROM qa_pairs WHERE embedding IS NOT NULL
           ORDER BY embedding <=> $1::vector LIMIT 1""",
        emb_str,
    )


async def _search_chunks(conn, emb_str: str):
    """Fetch top candidates from chunks + web_chunks, merged by similarity."""
    chunk_rows = await conn.fetch(
        """SELECT title, section, content, source_file, doc_url,
                  'local_doc' AS source_type,
                  1 - (embedding <=> $1::vector) AS similarity
           FROM chunks ORDER BY embedding <=> $1::vector LIMIT 10""",
        emb_str,
    )
    web_rows = await conn.fetch(
        """SELECT page_title AS title, section_heading AS section,
                  content, page_slug AS source_file, page_url AS doc_url,
                  'web_doc' AS source_type,
                  1 - (embedding <=> $1::vector) AS similarity
           FROM web_chunks ORDER BY embedding <=> $1::vector LIMIT 10""",
        emb_str,
    )
    merged = sorted(
        list(chunk_rows) + list(web_rows),
        key=lambda r: float(r["similarity"]), reverse=True,
    )[:10]
    return merged


async def _rerank_candidates(question: str, candidates) -> list[dict]:
    """Rerank candidates via GPU server. Returns scored list sorted by reranker desc."""
    texts = [r["content"][:2000] for r in candidates]
    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post(RERANK_URL, json={"query": question, "texts": texts})
            resp.raise_for_status()
            rr_results = resp.json()
    except Exception:
        rr_results = [{"index": i, "score": float(r["similarity"])} for i, r in enumerate(candidates)]

    scored = []
    for rr in rr_results:
        r = candidates[rr["index"]]
        scored.append({
            "title": r["title"],
            "section": r["section"],
            "content": r["content"],
            "source_file": r["source_file"],
            "doc_url": r.get("doc_url"),
            "source_type": r.get("source_type", "local_doc"),
            "cosine": float(r["similarity"]),
            "reranker": float(rr["score"]),
        })
    scored.sort(key=lambda x: x["reranker"], reverse=True)
    return scored


def _make_source_title(src: str) -> str:
    return src.split("/")[-1].replace(".md", "").replace("-", " ").title() if "/" in src else src


# ── SSE Streaming endpoint ─────────────────────────────────

STREAM_SYSTEM_PROMPT = """\
You are the Acronis Cyber Protect Cloud Assistant (v26.02).
Answer the user's question based ONLY on the provided documentation context.
Be concise. Use **bold** for key terms, numbered lists for steps, `code` for commands.
End with: **Source:** [`source_file`](doc_url) — or just `source_file` if no URL.
If the context doesn't cover the topic, say so. Never invent information.\
"""


def _step_event(step: str, message: str, icon: str, elapsed_ms: int, data: dict = None, details: dict = None):
    """Build a step SSE event dict."""
    payload = {"type": "step", "step": step, "message": message, "icon": icon, "elapsed_ms": elapsed_ms}
    if data:
        payload["data"] = data
    if details:
        payload["details"] = details
    return {"event": "message", "data": json.dumps(payload)}


@app.post("/api/chat/stream")
async def chat_stream(req: ChatRequest):
    question = req.message.strip()

    async def event_generator():
        sid = await db_get_or_create_session(req.session_id)
        yield {"event": "message", "data": json.dumps({"type": "session", "session_id": sid})}

        if not question:
            yield {"event": "message", "data": json.dumps({"type": "token", "text": "Please enter a question."})}
            yield {"event": "message", "data": json.dumps({"type": "done"})}
            return

        t0 = time.monotonic()

        def elapsed():
            return int((time.monotonic() - t0) * 1000)

        # ── Step 1: Embedding ──
        yield _step_event("embedding", "Searching knowledge base...", "search", elapsed(),
                          details={"query_length": len(question)})

        try:
            embedding = await _embed_query(question)
        except Exception as e:
            yield {"event": "message", "data": json.dumps({"type": "token", "text": f"Embedding error: {e}"})}
            yield {"event": "message", "data": json.dumps({"type": "done"})}
            return

        emb_str = "[" + ",".join(str(float(x)) for x in embedding) + "]"

        pool = await get_pool()
        async with pool.acquire() as conn:
            # ── Step 2: Q&A match check ──
            qa_row = await _search_qa_match(conn, emb_str)

            if qa_row and float(qa_row["similarity"]) >= QA_MATCH_THRESHOLD:
                sim = float(qa_row["similarity"])
                yield _step_event("qa_match", f"Found verified answer (score: {sim:.2f})", "verified", elapsed(),
                                  {"score": sim},
                                  details={"candidates": 1, "top_score": round(sim, 4), "tier": "qa_match"})

                src = qa_row["source_file"] or ""
                title = _make_source_title(src)
                qa_doc_url = qa_row.get("doc_url")
                sources = [{"title": title, "file": src, "score": sim, "doc_url": qa_doc_url, "source_type": "qa_match"}]

                yield _step_event("generating", "Streaming answer...", "brain", elapsed())
                yield {"event": "message", "data": json.dumps({"type": "sources", "sources": sources})}

                answer = qa_row["ideal_answer"]
                words = answer.split(" ")
                for i in range(0, len(words), 3):
                    chunk = " ".join(words[i:i + 3]) + " "
                    yield {"event": "message", "data": json.dumps({"type": "token", "text": chunk})}
                    await asyncio.sleep(0.02)
                yield {"event": "message", "data": json.dumps({"type": "token", "text": f"\n\n**Source:** `{src}`"})}

                await db_save_message(sid, "user", question)
                await db_save_message(sid, "assistant", answer, sources)
                yield {"event": "message", "data": json.dumps({"type": "done", "elapsed_ms": elapsed()})}
                return

            # ── Step 3: Chunk search ──
            rows = await _search_chunks(conn, emb_str)

        candidates = [r for r in rows if float(r["similarity"]) >= COSINE_THRESHOLD]
        top_cosine = round(float(candidates[0]["similarity"]), 4) if candidates else 0.0
        yield _step_event("searching", f"Found {len(candidates)} candidate chunks", "docs", elapsed(),
                          {"count": len(candidates)},
                          details={"candidates": len(candidates), "top_score": top_cosine, "tier": "chunk_search"})

        if not candidates:
            decline = "I don't have documentation about that topic. Please check the Acronis Knowledge Base at https://kb.acronis.com or contact Acronis Support."
            yield {"event": "message", "data": json.dumps({"type": "token", "text": decline})}
            await db_save_message(sid, "user", question)
            await db_save_message(sid, "assistant", decline)
            yield {"event": "message", "data": json.dumps({"type": "done", "elapsed_ms": elapsed()})}
            return

        # ── Step 4: Reranking ──
        yield _step_event("reranking", f"Reranking {len(candidates)} results...", "filter", elapsed(),
                          details={"reranked": len(candidates)})

        scored = await _rerank_candidates(question, candidates)
        top3 = [s for s in scored if s["reranker"] >= RERANKER_THRESHOLD][:3]

        if not top3:
            decline = "I don't have documentation about that topic. Please check the Acronis Knowledge Base at https://kb.acronis.com or contact Acronis Support."
            yield {"event": "message", "data": json.dumps({"type": "token", "text": decline})}
            await db_save_message(sid, "user", question)
            await db_save_message(sid, "assistant", decline)
            yield {"event": "message", "data": json.dumps({"type": "done", "elapsed_ms": elapsed()})}
            return

        # ── Step 5: Sources selected ──
        source_names = [s["source_file"].split("/")[-1] for s in top3]
        source_details = [
            {"file": s["source_file"], "title": _make_source_title(s["source_file"]),
             "score": round(s["cosine"], 4), "rerank_score": round(s["reranker"], 4)}
            for s in top3
        ]
        top_rerank = round(top3[0]["reranker"], 4) if top3 else 0.0
        yield _step_event("sources", f"Top {len(top3)} sources selected", "check", elapsed(),
                          {"sources": source_names},
                          details={"sources": source_details, "top_rerank_score": top_rerank})

        sources = []
        for s in top3:
            sf = s["source_file"]
            sources.append({"title": _make_source_title(sf), "file": sf, "score": s["reranker"],
                            "doc_url": s.get("doc_url"), "source_type": s.get("source_type", "local_doc")})
        yield {"event": "message", "data": json.dumps({"type": "sources", "sources": sources})}

        # ── Step 6: Generate answer ──
        context_len = sum(len(c["content"][:1000]) for c in top3)
        yield _step_event("generating", "Generating answer...", "brain", elapsed(),
                          details={"model": "claude-sonnet", "context_tokens": context_len})

        history = await db_get_history(sid)
        rag_prompt = _build_rag_prompt(question, history, top3)

        try:
            opts = ClaudeCodeOptions(
                system_prompt=STREAM_SYSTEM_PROMPT,
                permission_mode="acceptEdits",
                max_turns=1,
            )

            full_answer = ""
            last_len = 0
            async with ClaudeSDKClient(options=opts) as client:
                await client.query(rag_prompt)
                async for msg in client.receive_messages():
                    if msg is None:
                        continue
                    if isinstance(msg, AssistantMessage):
                        for block in msg.content:
                            if isinstance(block, TextBlock):
                                new_text = block.text
                                if len(new_text) > last_len:
                                    delta = new_text[last_len:]
                                    last_len = len(new_text)
                                    # Simulate streaming: emit in small word-chunks
                                    words = delta.split(" ")
                                    buf = ""
                                    for w in words:
                                        buf += w + " "
                                        if len(buf) >= 12:
                                            yield {"event": "message", "data": json.dumps({"type": "token", "text": buf})}
                                            buf = ""
                                            await asyncio.sleep(0.02)
                                    if buf:
                                        yield {"event": "message", "data": json.dumps({"type": "token", "text": buf})}
                                full_answer = new_text
                    elif isinstance(msg, ResultMessage):
                        if hasattr(msg, 'content'):
                            for block in getattr(msg, 'content', []):
                                if isinstance(block, TextBlock) and len(block.text) > last_len:
                                    delta = block.text[last_len:]
                                    yield {"event": "message", "data": json.dumps({"type": "token", "text": delta})}
                                    full_answer = block.text
                        break

            if not full_answer:
                full_answer = "I couldn't generate a response. Please try again."
                yield {"event": "message", "data": json.dumps({"type": "token", "text": full_answer})}

            await db_save_message(sid, "user", question)
            await db_save_message(sid, "assistant", full_answer, sources)

        except Exception as e:
            err_msg = f"Sorry, an error occurred: {str(e)}"
            yield {"event": "message", "data": json.dumps({"type": "token", "text": err_msg})}
            await db_save_message(sid, "user", question)
            await db_save_message(sid, "assistant", err_msg)

        yield {"event": "message", "data": json.dumps({"type": "done", "elapsed_ms": elapsed()})}

    return EventSourceResponse(event_generator())


# ── Non-streaming endpoint (fallback) ─────────────────────

@app.post("/api/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    question = req.message.strip()
    if not question:
        sid = await db_get_or_create_session(req.session_id)
        return ChatResponse(answer="Please enter a question.", sources=[], session_id=sid)

    sid = await db_get_or_create_session(req.session_id)

    try:
        # Get history from DB
        history = await db_get_history(sid)
        prompt = _build_context_prompt(history, question)

        opts = ClaudeCodeOptions(
            system_prompt=SYSTEM_PROMPT,
            mcp_servers={"acronis_kb": get_server()},
            allowed_tools=get_tool_names(),
            permission_mode="acceptEdits",
            max_turns=6,
        )

        async def _sdk_generate(attempt_prompt):
            p = []
            try:
                async with ClaudeSDKClient(options=opts) as client:
                    await client.query(attempt_prompt)
                    async for msg in client.receive_response():
                        if msg is None:
                            continue
                        if isinstance(msg, AssistantMessage):
                            for block in msg.content:
                                if isinstance(block, TextBlock):
                                    p.append(block.text)
                        elif isinstance(msg, ResultMessage):
                            break
            except Exception as e:
                if "Unknown message type" not in str(e):
                    raise
            return "\n".join(p)

        # Attempt 1
        answer = ""
        try:
            answer = await asyncio.wait_for(_sdk_generate(prompt), timeout=60)
        except asyncio.TimeoutError:
            answer = ""
        except Exception as e:
            if "Unknown message type" not in str(e):
                raise

        # Retry once if answer is empty or too short
        if not answer or len(answer) < 50:
            await asyncio.sleep(3)
            try:
                answer = await asyncio.wait_for(_sdk_generate(prompt), timeout=60)
            except asyncio.TimeoutError:
                answer = ""
            except Exception as e:
                if "Unknown message type" not in str(e):
                    pass

        # Fallback
        if not answer or len(answer) < 50:
            answer = "I apologize, I couldn't generate a response. Please rephrase or try again."

        sources = _extract_sources(answer)

        # Save to DB
        await db_save_message(sid, "user", question)
        sources_json = [{"title": s.title, "file": s.file, "score": s.score} for s in sources]
        await db_save_message(sid, "assistant", answer, sources_json)

        return ChatResponse(answer=answer, sources=sources, session_id=sid)

    except Exception as e:
        return ChatResponse(
            answer=f"Sorry, an error occurred: {str(e)}. Please try again.",
            sources=[],
            session_id=sid,
        )


def _extract_sources(text: str) -> list[SourceInfo]:
    """Extract source citations from agent response text."""
    import re
    sources = []
    seen = set()
    # Match backtick-wrapped file paths: `02-installing-deploying-agents/10-gui.md`
    for match in re.finditer(r'`([\w-]+/[\w-]+\.md)`', text):
        src = match.group(1)
        if src not in seen:
            seen.add(src)
            title = src.split("/")[-1].replace(".md", "").replace("-", " ").title()
            sources.append(SourceInfo(title=title, file=src, score=0.0))
    # Also match "Source: path" patterns
    for line in text.split("\n"):
        line_s = line.strip()
        for prefix in ("source:", "└─", "source file:"):
            if prefix in line_s.lower():
                parts = line_s.split(":" if ":" in prefix else "└─", 1)
                if len(parts) > 1:
                    src = parts[-1].strip().strip("`").strip("*").strip()
                    if src and src not in seen and "/" in src and src.endswith(".md"):
                        seen.add(src)
                        title = src.split("/")[-1].replace(".md", "").replace("-", " ").title()
                        sources.append(SourceInfo(title=title, file=src, score=0.0))
    return sources


# ── Document viewer endpoint ──────────────────────────────

DOCS_BASE_DIR = Path(__file__).resolve().parent.parent / "docs"

import functools


@functools.lru_cache(maxsize=256)
def _read_doc(abs_path: str) -> dict:
    """Read and parse a markdown doc file with YAML frontmatter."""
    p = Path(abs_path)
    raw = p.read_text(encoding="utf-8")

    title = ""
    section = ""
    pages = ""
    doc_url = ""
    body = raw

    # Strip YAML frontmatter
    if raw.startswith("---"):
        parts = raw.split("---", 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            body = parts[2].strip()
            for line in frontmatter.strip().splitlines():
                if line.startswith("title:"):
                    title = line.split(":", 1)[1].strip().strip('"').strip("'")
                elif line.startswith("section:"):
                    section = line.split(":", 1)[1].strip().strip('"').strip("'")
                elif line.startswith("page_range:"):
                    pages = "p." + line.split(":", 1)[1].strip().strip('"').strip("'")
                elif line.startswith("doc_url:"):
                    doc_url = line.split(":", 1)[1].strip().strip('"').strip("'")

    return {"title": title, "section": section, "pages": pages, "content": body, "doc_url": doc_url}


@app.get("/api/docs/{source_path:path}")
async def get_doc(source_path: str):
    # Path traversal protection
    if ".." in source_path or source_path.startswith("/"):
        return JSONResponse(status_code=400, content={"error": "Invalid path"})

    file_path = DOCS_BASE_DIR / source_path
    resolved = file_path.resolve()

    # Ensure resolved path is within DOCS_BASE_DIR
    if not str(resolved).startswith(str(DOCS_BASE_DIR.resolve())):
        return JSONResponse(status_code=400, content={"error": "Invalid path"})

    if not resolved.is_file():
        return JSONResponse(status_code=404, content={"error": "Document not found"})

    doc = _read_doc(str(resolved))
    return {
        "path": source_path,
        "title": doc["title"],
        "content": doc["content"],
        "section": doc["section"],
        "pages": doc["pages"],
        "doc_url": doc.get("doc_url", ""),
    }


@app.get("/api/web-docs/{slug}")
async def get_web_doc(slug: str):
    """Return all chunks for a web doc page, merged into one document."""
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch(
            """SELECT page_title, page_url, section_heading, content, chunk_index
               FROM web_chunks WHERE page_slug = $1
               ORDER BY chunk_index""",
            slug,
        )
    if not rows:
        return JSONResponse(status_code=404, content={"error": "Web document not found"})

    title = rows[0]["page_title"]
    page_url = rows[0]["page_url"]
    merged_content = "\n\n".join(r["content"] for r in rows)

    return {
        "slug": slug,
        "title": title,
        "content": merged_content,
        "page_url": page_url,
        "chunk_count": len(rows),
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("agent.api:app", host="0.0.0.0", port=8080, reload=True)
