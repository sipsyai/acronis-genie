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
COSINE_THRESHOLD = 0.30
QA_MATCH_THRESHOLD = 0.80  # Calibrated for Qwen3-Embedding-4B
RETRIEVE_K = 20

QUERY_INSTRUCTION = "Instruct: Given a web search query, retrieve relevant passages that answer the query about Acronis Cyber Protect Cloud\nQuery: "


async def _embed_query(text: str) -> list[float]:
    """Get embedding from remote GPU server with instruction prefix for asymmetric retrieval."""
    prefixed = QUERY_INSTRUCTION + text
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.post(
            EMBED_URL,
            json={"input": prefixed, "model": EMBED_MODEL},
        )
        resp.raise_for_status()
        return resp.json()["data"][0]["embedding"]



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

        # ── Tier 2: Hybrid search (dense + FTS with RRF) ──
        # Dense retrieval
        chunk_rows = await conn.fetch(
            """SELECT id, title, section, content, source_file, doc_url,
                   'local_doc' AS source_type,
                   1 - (embedding <=> $1::vector) AS similarity
            FROM chunks ORDER BY embedding <=> $1::vector LIMIT $2""",
            emb_str, RETRIEVE_K,
        )
        web_rows = await conn.fetch(
            """SELECT id, page_title AS title, section_heading AS section,
                   content, page_slug AS source_file, page_url AS doc_url,
                   source_domain, 'web_doc' AS source_type,
                   1 - (embedding <=> $1::vector) AS similarity
            FROM web_chunks ORDER BY embedding <=> $1::vector LIMIT $2""",
            emb_str, RETRIEVE_K,
        )
        dense_results = list(chunk_rows) + list(web_rows)
        dense_sorted = sorted(dense_results, key=lambda r: float(r["similarity"]), reverse=True)

        # FTS retrieval (OR mode)
        words = query_text.lower().split()
        words = [w for w in words if len(w) > 2 and w not in (
            "the", "and", "for", "how", "what", "does", "can", "are", "with", "from", "this", "that",
        )]
        fts_results = []
        if words:
            or_query = " | ".join(words)
            fts_chunks = await conn.fetch(
                """SELECT id, title, section, content, source_file, doc_url,
                       'local_doc' AS source_type,
                       ts_rank_cd(fts, to_tsquery('english', $1)) AS fts_rank
                FROM chunks WHERE fts @@ to_tsquery('english', $1)
                ORDER BY fts_rank DESC LIMIT $2""",
                or_query, RETRIEVE_K,
            )
            fts_web = await conn.fetch(
                """SELECT id, page_title AS title, section_heading AS section,
                       content, page_slug AS source_file, page_url AS doc_url,
                       source_domain, 'web_doc' AS source_type,
                       ts_rank_cd(fts, to_tsquery('english', $1)) AS fts_rank
                FROM web_chunks WHERE fts @@ to_tsquery('english', $1)
                ORDER BY fts_rank DESC LIMIT $2""",
                or_query, RETRIEVE_K,
            )
            fts_results = list(fts_chunks) + list(fts_web)

        # RRF Fusion
        RRF_K = 60
        scores = {}
        chunk_data = {}

        for rank, row in enumerate(dense_sorted):
            key = (row["source_type"], row["id"])
            scores[key] = scores.get(key, 0) + 1.0 / (RRF_K + rank)
            chunk_data[key] = dict(row)

        for rank, row in enumerate(fts_results):
            key = (row["source_type"], row["id"])
            scores[key] = scores.get(key, 0) + 1.0 / (RRF_K + rank)
            if key not in chunk_data:
                chunk_data[key] = dict(row)
                chunk_data[key]["similarity"] = 0.0  # FTS-only result

        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:RETRIEVE_K]
        rows = []
        for key, rrf in ranked:
            d = chunk_data[key]
            d["rrf_score"] = rrf
            rows.append(d)
    finally:
        await conn.close()

    # Pre-filter: cosine >= threshold OR found via both dense+FTS (high RRF)
    candidates = [r for r in rows if float(r.get("similarity", 0)) >= COSINE_THRESHOLD or r.get("rrf_score", 0) > 1.0 / (60 + RETRIEVE_K)]

    if not candidates:
        return {
            "content": [{
                "type": "text",
                "text": f"No relevant documentation found for: '{query_text}' "
                f"(no candidates passed hybrid search filters)",
            }]
        }

    # Take top results (RRF-ranked, no reranker)
    results = []
    for r in candidates[:top_k]:
        results.append({
            "title": r.get("title", ""),
            "section": r.get("section"),
            "content": r["content"],
            "source_file": r.get("source_file", ""),
            "doc_url": r.get("doc_url"),
            "source_type": r.get("source_type", "local_doc"),
            "cosine": float(r.get("similarity", 0)),
            "rrf_score": float(r.get("rrf_score", 0)),
        })

    if not results:
        return {
            "content": [{
                "type": "text",
                "text": f"No relevant documentation found for: '{query_text}' "
                f"(no candidates passed hybrid search filters)",
            }]
        }

    # Format chunk results — send FULL content, no truncation
    parts = ["[CHUNK SEARCH]"]
    for r in results:
        parts.append(
            f"[RRF: {r['rrf_score']:.4f} | Cosine: {r['cosine']:.2f}] {r['title']}\n"
            f"Source: {r['source_file']}\n"
            f"Doc URL: {r.get('doc_url') or 'N/A'}\n"
            f"Section: {r['section'] or 'N/A'}\n"
            f"---\n{r['content']}\n"
        )

    return {"content": [{"type": "text", "text": "\n".join(parts)}]}
