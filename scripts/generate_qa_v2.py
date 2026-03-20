"""
Q&A Generation Pipeline — Single Claude call per chunk.
215 chunks × 1 call = 215 calls. Each call generates 2 Q&A pairs with ideal answers.
RAG retrieval scores computed separately via GPU server (no SDK needed).
Resume support + incremental save.
"""

import asyncio
import json
import subprocess
import time
import asyncpg
import httpx
from pathlib import Path

DB_DSN = "postgresql://acronis:acronis@localhost:5432/acronis_agent"
EMBED_URL = "http://192.168.1.8:8011/v1/embeddings"
EMBED_MODEL = "Qwen/Qwen3-Embedding-4B"
RERANK_URL = "http://192.168.1.8:8012/rerank"

DATA_DIR = Path(__file__).parent.parent / "data"
OUTPUT_FILE = DATA_DIR / "qa_dataset_v2.json"
SUMMARY_FILE = DATA_DIR / "qa_summary_v2.json"
FAILURES_FILE = DATA_DIR / "qa_failures.json"

TOP_K_COSINE = 10
TOP_K_RERANK = 3

SYSTEM_PROMPT = """You are a Q&A dataset generator for Acronis Cyber Protect Cloud documentation.

For the given documentation chunk, generate exactly 2 Q&A pairs:
1. A practical how-to question a real customer would ask
2. A specific detail or edge-case question about settings, requirements, or limitations

Return ONLY a valid JSON array with exactly 2 objects. No markdown fences, no explanation, no preamble.

[
  {
    "question": "practical how-to question",
    "ideal_answer": "concise answer based strictly on chunk content, 2-5 sentences",
    "type": "how_to",
    "quality_score": 5,
    "difficulty": "easy"
  },
  {
    "question": "specific detail or edge-case question",
    "ideal_answer": "concise answer based strictly on chunk content, 2-5 sentences",
    "type": "detail",
    "quality_score": 4,
    "difficulty": "medium"
  }
]

Quality: 5=natural+complete, 4=good, 3=acceptable, 2=obvious/incomplete, 1=poor.
Difficulty: easy=basic usage, medium=specific config, hard=edge case/troubleshooting.
Answers MUST be based strictly on the chunk content. Do not invent information."""


def claude_call(user_prompt: str, max_retries: int = 2) -> str:
    """Call Claude Code CLI with OAuth session."""
    for attempt in range(max_retries):
        try:
            result = subprocess.run(
                ["claude", "-p", user_prompt, "--system-prompt", SYSTEM_PROMPT,
                 "--output-format", "text", "--max-turns", "1"],
                capture_output=True, text=True, timeout=90,
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
            if result.stderr and "rate" in result.stderr.lower():
                print(f"    Rate limited, sleeping 10s...")
                time.sleep(10)
                continue
            if result.stderr:
                err_short = result.stderr.strip()[:150]
                print(f"    Claude stderr: {err_short}")
        except subprocess.TimeoutExpired:
            print(f"    Timeout (attempt {attempt + 1})")
        except Exception as e:
            print(f"    Error: {e}")
    return ""


def parse_json_response(text: str) -> list | None:
    """Extract JSON array from Claude response."""
    text = text.strip()
    # Remove markdown fences
    if "```" in text:
        for part in text.split("```"):
            part = part.strip()
            if part.startswith("json"):
                part = part[4:].strip()
            if part.startswith("["):
                try:
                    return json.loads(part)
                except json.JSONDecodeError:
                    continue
    # Direct parse
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # Find array in text
    s = text.find("[")
    e = text.rfind("]")
    if s != -1 and e > s:
        try:
            return json.loads(text[s:e + 1])
        except json.JSONDecodeError:
            pass
    return None


async def embed_text(client: httpx.AsyncClient, text: str) -> list[float]:
    resp = await client.post(EMBED_URL, json={"input": text, "model": EMBED_MODEL})
    resp.raise_for_status()
    return resp.json()["data"][0]["embedding"]


async def rerank_texts(client: httpx.AsyncClient, query: str, texts: list[str]) -> list[dict]:
    resp = await client.post(RERANK_URL, json={"query": query, "texts": texts})
    resp.raise_for_status()
    results = resp.json()
    results.sort(key=lambda x: x["score"], reverse=True)
    return results


async def search_rag(conn, http: httpx.AsyncClient, question: str) -> dict:
    """RAG search: embed → cosine → rerank. Returns scores + sources."""
    q_emb = await embed_text(http, question)
    q_str = "[" + ",".join(str(float(x)) for x in q_emb) + "]"

    rows = await conn.fetch(
        """SELECT title, source_file, content,
                  1 - (embedding <=> $1::vector) AS cosine_sim
           FROM chunks ORDER BY embedding <=> $1::vector LIMIT $2""",
        q_str, TOP_K_COSINE,
    )
    if not rows:
        return {"cosine": 0, "reranker": 0, "sources": [], "top1_file": ""}

    texts = [r["content"][:2000] for r in rows]
    rr = await rerank_texts(http, question, texts)

    top3 = []
    for item in rr[:TOP_K_RERANK]:
        row = rows[item["index"]]
        top3.append({
            "file": row["source_file"],
            "title": row["title"],
            "cosine": float(row["cosine_sim"]),
            "reranker": float(item["score"]),
        })

    return {
        "cosine": top3[0]["cosine"] if top3 else 0,
        "reranker": top3[0]["reranker"] if top3 else 0,
        "sources": [t["file"] for t in top3],
        "top1_file": top3[0]["file"] if top3 else "",
    }


def load_dataset() -> list[dict]:
    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE) as f:
            return json.load(f)
    return []


def save_dataset(entries: list[dict]):
    DATA_DIR.mkdir(exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)


def save_failures(failures: list[dict]):
    DATA_DIR.mkdir(exist_ok=True)
    with open(FAILURES_FILE, "w") as f:
        json.dump(failures, f, indent=2, ensure_ascii=False)


async def main():
    conn = await asyncpg.connect(DB_DSN)
    http = httpx.AsyncClient(timeout=30.0)

    rows = await conn.fetch(
        "SELECT id, title, section, subsection, source_file, content, word_count FROM chunks ORDER BY id"
    )
    print(f"Chunks in DB: {len(rows)}")

    # Resume support
    dataset = load_dataset()
    done_chunks = {e["chunk_id"] for e in dataset}
    print(f"Already done: {len(done_chunks)} chunks, {len(dataset)} Q&A pairs")

    failures = []
    new_count = 0

    for idx, row in enumerate(rows):
        chunk_id = row["id"]
        if chunk_id in done_chunks:
            continue

        title = row["title"]
        source_file = row["source_file"]
        section = row["section"] or ""
        content = row["content"]
        wc = row["word_count"]

        # Build user prompt
        user_prompt = f"""Generate 2 Q&A pairs from this chunk:

Title: {title}
Section: {section}
Source: {source_file}
Words: {wc}

Content:
{content[:2500]}"""

        # Single Claude call
        raw = claude_call(user_prompt)
        if not raw:
            print(f"[{idx + 1}/{len(rows)}] {title[:40]} — FAILED (empty response)")
            failures.append({"chunk_id": chunk_id, "title": title, "error": "empty response"})
            time.sleep(2)
            continue

        qa_pairs = parse_json_response(raw)
        if not qa_pairs or not isinstance(qa_pairs, list) or len(qa_pairs) == 0:
            # Retry once
            time.sleep(3)
            raw = claude_call(user_prompt)
            qa_pairs = parse_json_response(raw) if raw else None
            if not qa_pairs or not isinstance(qa_pairs, list):
                print(f"[{idx + 1}/{len(rows)}] {title[:40]} — FAILED (JSON parse)")
                failures.append({"chunk_id": chunk_id, "title": title, "error": "json_parse", "raw": raw[:200]})
                time.sleep(2)
                continue

        # Process each Q&A pair
        scores_str = []
        for q_idx, qa in enumerate(qa_pairs[:2]):
            question = qa.get("question", "").strip()
            ideal_answer = qa.get("ideal_answer", "").strip()
            q_type = qa.get("type", "how_to" if q_idx == 0 else "detail")
            quality = qa.get("quality_score", 3)
            difficulty = qa.get("difficulty", "medium")

            if not question or not ideal_answer:
                continue

            # RAG retrieval (no Claude call, just GPU server)
            rag = await search_rag(conn, http, question)
            correct_top3 = source_file in rag["sources"]
            correct_top1 = rag["top1_file"] == source_file

            entry_id = f"qa_{chunk_id:03d}_{q_type}"
            entry = {
                "id": entry_id,
                "chunk_id": chunk_id,
                "chunk_title": title,
                "source_file": source_file,
                "section": section,
                "question": question,
                "ideal_answer": ideal_answer,
                "type": q_type,
                "difficulty": difficulty,
                "quality_score": quality,
                "cosine_score": round(rag["cosine"], 4),
                "reranker_score": round(rag["reranker"], 4),
                "correct_source_in_top1": correct_top1,
                "correct_source_in_top3": correct_top3,
                "retrieved_sources": rag["sources"],
                "verified": False,
                "added_to_qa_rag": False,
            }
            dataset.append(entry)
            mark = "1" if correct_top1 else ("3" if correct_top3 else "X")
            scores_str.append(f"{quality}")

        done_chunks.add(chunk_id)
        new_count += len(scores_str)

        # Incremental save
        save_dataset(dataset)

        retrieval_mark = "top-1" if any(e.get("correct_source_in_top1") for e in dataset[-2:]) \
            else ("top-3" if any(e.get("correct_source_in_top3") for e in dataset[-2:]) else "miss")
        print(f"[{idx + 1}/{len(rows)}] {title[:45]:45s} — {len(scores_str)} Q&A (scores: {','.join(scores_str)}) — retrieval: {retrieval_mark} — saved")

        time.sleep(2)

    await http.aclose()
    await conn.close()

    # Save failures
    if failures:
        save_failures(failures)

    # Final save
    save_dataset(dataset)

    # Summary
    print(f"\n{'=' * 65}")
    print(f"SUMMARY")
    print(f"{'=' * 65}")
    print(f"Total Q&A pairs: {len(dataset)}")
    print(f"Chunks processed: {len(done_chunks)} / {len(rows)}")
    print(f"Chunks failed: {len(failures)}")
    print(f"New this run: {new_count}")

    if dataset:
        scores = [e["quality_score"] for e in dataset]
        top1 = sum(1 for e in dataset if e.get("correct_source_in_top1"))
        top3 = sum(1 for e in dataset if e.get("correct_source_in_top3"))
        difficulties = {}
        for e in dataset:
            d = e.get("difficulty", "unknown")
            difficulties[d] = difficulties.get(d, 0) + 1

        avg_q = sum(scores) / len(scores)
        avg_cos = sum(e["cosine_score"] for e in dataset) / len(dataset)
        avg_rr = sum(e["reranker_score"] for e in dataset) / len(dataset)

        print(f"Avg quality: {avg_q:.2f}/5")
        print(f"Avg cosine: {avg_cos:.4f}")
        print(f"Avg reranker: {avg_rr:.4f}")
        print(f"Correct source top-1: {top1}/{len(dataset)} ({top1 * 100 // len(dataset)}%)")
        print(f"Correct source top-3: {top3}/{len(dataset)} ({top3 * 100 // len(dataset)}%)")

        print(f"\nQuality distribution:")
        q_dist = {}
        for q in range(1, 6):
            cnt = scores.count(q)
            q_dist[str(q)] = cnt
            print(f"  {q}/5: {cnt:>4} {'█' * cnt}")

        print(f"\nDifficulty distribution:")
        for d, cnt in sorted(difficulties.items()):
            print(f"  {d}: {cnt}")

        summary = {
            "total_pairs": len(dataset),
            "chunks_processed": len(done_chunks),
            "chunks_failed": len(failures),
            "avg_quality": round(avg_q, 2),
            "avg_cosine": round(avg_cos, 4),
            "avg_reranker": round(avg_rr, 4),
            "top1_accuracy": f"{top1}/{len(dataset)} ({top1 * 100 // len(dataset)}%)",
            "top3_accuracy": f"{top3}/{len(dataset)} ({top3 * 100 // len(dataset)}%)",
            "quality_dist": q_dist,
            "difficulty_dist": difficulties,
        }
        with open(SUMMARY_FILE, "w") as f:
            json.dump(summary, f, indent=2)
        print(f"\nSummary: {SUMMARY_FILE}")

    print(f"Dataset: {OUTPUT_FILE}")
    if failures:
        print(f"Failures: {FAILURES_FILE}")


if __name__ == "__main__":
    asyncio.run(main())
