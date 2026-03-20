"""
MCP tool: search_docs — two-tier RAG over Acronis documentation in pgvector.
Tier 1: Q&A pair matching (fast, pre-verified answers)
Tier 2: Chunk semantic search + reranking (full RAG)

Uses remote GPU server (192.168.1.8) for:
  - Qwen3-Embedding (port 8011) — query embedding
  - BGE-Reranker-v2-M3 (port 8012) — cross-encoder reranking
"""

import asyncpg
import httpx
from claude_code_sdk import tool

DB_DSN = "postgresql://acronis:acronis@localhost:5432/acronis_agent"
EMBED_URL = "http://192.168.1.8:8011/v1/embeddings"
EMBED_MODEL = "Qwen/Qwen3-Embedding-4B"
RERANK_URL = "http://192.168.1.8:8012/rerank"
COSINE_THRESHOLD = 0.40
RERANKER_THRESHOLD = 0.20
QA_MATCH_THRESHOLD = 0.80  # Calibrated for Qwen3-Embedding-4B
RETRIEVE_K = 10


async def _embed_query(text: str) -> list[float]:
    """Get embedding from remote GPU server."""
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.post(
            EMBED_URL,
            json={"input": text, "model": EMBED_MODEL},
        )
        resp.raise_for_status()
        return resp.json()["data"][0]["embedding"]


async def _rerank(query: str, texts: list[str]) -> list[float]:
    """Rerank texts against query via remote GPU server."""
    async with httpx.AsyncClient(timeout=60.0) as client:
        resp = await client.post(
            RERANK_URL,
            json={"query": query, "texts": texts},
        )
        resp.raise_for_status()
        results = resp.json()
        scores = [0.0] * len(texts)
        for r in results:
            scores[r["index"]] = r["score"]
        return scores


async def _search_qa_pairs(conn, emb_str: str) -> dict | None:
    """Check Q&A pairs for a high-confidence match."""
    row = await conn.fetchrow(
        """
        SELECT question, ideal_answer, source_file, section, quality_score,
               1 - (embedding <=> $1::vector) AS similarity
        FROM qa_pairs
        WHERE embedding IS NOT NULL
        ORDER BY embedding <=> $1::vector
        LIMIT 1
        """,
        emb_str,
    )
    if row and float(row["similarity"]) >= QA_MATCH_THRESHOLD:
        return {
            "question": row["question"],
            "answer": row["ideal_answer"],
            "source_file": row["source_file"],
            "section": row["section"],
            "similarity": float(row["similarity"]),
            "quality_score": row["quality_score"],
        }
    return None


@tool(
    "search_docs",
    "Search Acronis Cyber Protect Cloud documentation by semantic similarity with reranking. "
    "Use this to find relevant documentation chunks for answering user questions about Acronis.",
    {"query": str, "top_k": int},
)
async def search_docs(args: dict) -> dict:
    query_text = args["query"]
    top_k = args.get("top_k", 3)

    # Embed query once — reuse for both Q&A and chunk search
    embedding = await _embed_query(query_text)
    emb_str = "[" + ",".join(str(float(x)) for x in embedding) + "]"

    conn = await asyncpg.connect(DB_DSN)
    try:
        # ── Tier 1: Q&A pair matching ──────────────────────────
        qa_match = await _search_qa_pairs(conn, emb_str)
        if qa_match:
            return {
                "content": [{
                    "type": "text",
                    "text": (
                        f"[Q&A MATCH - similarity: {qa_match['similarity']:.2f}]\n"
                        f"Question: {qa_match['question']}\n"
                        f"Answer: {qa_match['answer']}\n"
                        f"Source: {qa_match['source_file']}\n"
                        f"Section: {qa_match['section'] or 'N/A'}\n\n"
                        f"Note: This is a verified answer from the knowledge base. "
                        f"You can use it directly."
                    ),
                }]
            }

        # ── Tier 2: Chunk search + reranking (local + web merged) ──
        chunk_rows = await conn.fetch(
            """
            SELECT id, title, section, content, source_file, doc_url,
                   'local_doc' AS source_type,
                   1 - (embedding <=> $1::vector) AS similarity
            FROM chunks
            ORDER BY embedding <=> $1::vector
            LIMIT $2
            """,
            emb_str,
            RETRIEVE_K,
        )
        web_rows = await conn.fetch(
            """
            SELECT id, page_title AS title, section_heading AS section,
                   content, page_slug AS source_file, page_url AS doc_url,
                   'web_doc' AS source_type,
                   1 - (embedding <=> $1::vector) AS similarity
            FROM web_chunks
            ORDER BY embedding <=> $1::vector
            LIMIT $2
            """,
            emb_str,
            RETRIEVE_K,
        )
        rows = sorted(
            list(chunk_rows) + list(web_rows),
            key=lambda r: float(r["similarity"]), reverse=True,
        )[:RETRIEVE_K]
    finally:
        await conn.close()

    # Pre-filter by cosine threshold
    candidates = [r for r in rows if r["similarity"] >= COSINE_THRESHOLD]

    if not candidates:
        return {
            "content": [{
                "type": "text",
                "text": f"No relevant documentation found for: '{query_text}' "
                f"(all {len(rows)} results below cosine threshold {COSINE_THRESHOLD})",
            }]
        }

    # Rerank via GPU server
    texts = [r["content"] for r in candidates]
    rerank_scores = await _rerank(query_text, texts)

    scored = []
    for r, rscore in zip(candidates, rerank_scores):
        scored.append({
            "title": r["title"],
            "section": r["section"],
            "content": r["content"],
            "source_file": r["source_file"],
            "doc_url": r.get("doc_url"),
            "source_type": r.get("source_type", "local_doc"),
            "cosine": float(r["similarity"]),
            "reranker": float(rscore),
        })

    scored.sort(key=lambda x: x["reranker"], reverse=True)
    results = [s for s in scored if s["reranker"] >= RERANKER_THRESHOLD][:top_k]

    if not results:
        return {
            "content": [{
                "type": "text",
                "text": f"No relevant documentation found for: '{query_text}' "
                f"(best reranker score: {scored[0]['reranker']:.4f}, threshold: {RERANKER_THRESHOLD})",
            }]
        }

    # Format chunk results — send FULL content, no truncation
    parts = ["[CHUNK SEARCH]"]
    for r in results:
        parts.append(
            f"[Reranker: {r['reranker']:.4f} | Cosine: {r['cosine']:.2f}] {r['title']}\n"
            f"Source: {r['source_file']}\n"
            f"Doc URL: {r.get('doc_url') or 'N/A'}\n"
            f"Section: {r['section'] or 'N/A'}\n"
            f"---\n{r['content']}\n"
        )

    return {"content": [{"type": "text", "text": "\n".join(parts)}]}
