"""
Evaluate Q&A dataset by asking questions through the RAG pipeline,
comparing RAG answers to ideal answers, and scoring retrieval accuracy.
Updates dataset entries with evaluation results.

Usage: python scripts/evaluate_qa.py [--limit N] [--resume]
"""

import asyncio
import json
import subprocess
import sys
import time
from pathlib import Path

import asyncpg
import httpx

DB_DSN = "postgresql://acronis:acronis@localhost:5432/acronis_agent"
EMBED_URL = "http://192.168.1.8:8011/v1/embeddings"
EMBED_MODEL = "Qwen/Qwen3-Embedding-4B"
RERANK_URL = "http://192.168.1.8:8012/rerank"

DATA_DIR = Path.home() / "Documents/Projects/acronis-genie/data"
QA_FILE = DATA_DIR / "qa_dataset_v2.json"
EVAL_FILE = DATA_DIR / "qa_evaluation.json"
EVAL_SUMMARY = DATA_DIR / "qa_eval_summary.json"

EVAL_SYSTEM_PROMPT = """You are a strict evaluator comparing a RAG system answer against an ideal answer.

Score the RAG answer on these dimensions:
1. correctness (0-5): How factually accurate is the RAG answer compared to the ideal?
2. completeness (0-5): Does the RAG answer cover all key points from the ideal?
3. relevance (0-5): Is the RAG answer relevant to the question asked?
4. hallucination (0-5): 5=no hallucination, 0=completely made up

Return ONLY a valid JSON object. No markdown, no explanation.

{
  "correctness": 4,
  "completeness": 3,
  "relevance": 5,
  "hallucination": 5,
  "overall": 4,
  "issues": "brief note if any issues, or empty string"
}"""


def claude_evaluate(question: str, ideal: str, rag_answer: str) -> dict | None:
    """Use Claude to compare RAG answer vs ideal answer."""
    user_prompt = f"""Evaluate this RAG answer against the ideal answer.

Question: {question}

Ideal Answer: {ideal}

RAG Answer: {rag_answer[:1500]}

Score the RAG answer."""

    try:
        result = subprocess.run(
            ["claude", "-p", user_prompt, "--system-prompt", EVAL_SYSTEM_PROMPT,
             "--output-format", "text", "--max-turns", "1"],
            capture_output=True, text=True, timeout=60,
        )
        if result.returncode == 0 and result.stdout.strip():
            text = result.stdout.strip()
            # Parse JSON
            if "```" in text:
                for part in text.split("```"):
                    part = part.strip()
                    if part.startswith("json"):
                        part = part[4:].strip()
                    if part.startswith("{"):
                        try:
                            return json.loads(part)
                        except json.JSONDecodeError:
                            continue
            s = text.find("{")
            e = text.rfind("}")
            if s != -1 and e > s:
                try:
                    return json.loads(text[s:e + 1])
                except json.JSONDecodeError:
                    pass
    except Exception as e:
        print(f"    Eval error: {e}")
    return None


async def get_rag_answer(conn, http: httpx.AsyncClient, question: str) -> dict:
    """Get RAG answer: embed → retrieve → rerank → return top results."""
    q_emb_resp = await http.post(EMBED_URL, json={"input": question, "model": EMBED_MODEL})
    q_emb = q_emb_resp.json()["data"][0]["embedding"]
    q_str = "[" + ",".join(str(float(x)) for x in q_emb) + "]"

    rows = await conn.fetch(
        """SELECT title, source_file, content,
                  1 - (embedding <=> $1::vector) AS cosine_sim
           FROM chunks ORDER BY embedding <=> $1::vector LIMIT 10""",
        q_str,
    )
    if not rows:
        return {"answer_context": "", "sources": [], "cosine": 0, "reranker": 0}

    texts = [r["content"][:2000] for r in rows]
    rr_resp = await http.post(RERANK_URL, json={"query": question, "texts": texts})
    rr_results = rr_resp.json()
    rr_results.sort(key=lambda x: x["score"], reverse=True)

    top3 = []
    for item in rr_results[:3]:
        row = rows[item["index"]]
        top3.append({
            "file": row["source_file"],
            "title": row["title"],
            "content": row["content"][:1000],
            "cosine": float(row["cosine_sim"]),
            "reranker": float(item["score"]),
        })

    # Build context from top-3 for answer generation
    context = "\n\n---\n\n".join(
        f"[{t['title']}] ({t['file']})\n{t['content']}" for t in top3
    )

    return {
        "answer_context": context,
        "sources": [t["file"] for t in top3],
        "top1_file": top3[0]["file"] if top3 else "",
        "cosine": top3[0]["cosine"] if top3 else 0,
        "reranker": top3[0]["reranker"] if top3 else 0,
    }


def generate_rag_answer(question: str, context: str) -> str:
    """Use Claude to generate answer from retrieved context."""
    prompt = f"""Based on this documentation context, answer the question concisely.
If the context doesn't contain relevant information, say so.

Context:
{context[:3000]}

Question: {question}

Answer concisely in 2-5 sentences."""

    sys_prompt = "You are an Acronis Cyber Protect Cloud support agent. Answer based strictly on the provided context. Be concise."

    try:
        result = subprocess.run(
            ["claude", "-p", prompt, "--system-prompt", sys_prompt,
             "--output-format", "text", "--max-turns", "1"],
            capture_output=True, text=True, timeout=60,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return ""


async def main():
    limit = None
    resume = "--resume" in sys.argv
    for arg in sys.argv:
        if arg.startswith("--limit"):
            try:
                limit = int(sys.argv[sys.argv.index(arg) + 1])
            except (ValueError, IndexError):
                pass

    # Load Q&A dataset
    if not QA_FILE.exists():
        print(f"ERROR: {QA_FILE} not found. Run generate_qa_v2.py first.")
        return

    qa_data = json.loads(QA_FILE.read_text())
    print(f"Loaded {len(qa_data)} Q&A pairs from dataset")

    conn = await asyncpg.connect(DB_DSN)
    http = httpx.AsyncClient(timeout=30.0)

    # Load existing evaluations for resume (from JSON + DB)
    evaluations = []
    done_ids = set()
    if resume:
        if EVAL_FILE.exists():
            evaluations = json.loads(EVAL_FILE.read_text())
            done_ids = {e["qa_id"] for e in evaluations}
        # Also check DB for entries not in JSON
        db_done = await conn.fetch("SELECT qa_id FROM qa_evaluations")
        for r in db_done:
            done_ids.add(r["qa_id"])
        print(f"Resuming: {len(done_ids)} already evaluated (JSON: {len(evaluations)}, DB: {len(db_done)})")

    # Filter to unevaluated entries
    to_eval = [qa for qa in qa_data if qa["id"] not in done_ids]
    if limit:
        to_eval = to_eval[:limit]
    print(f"To evaluate: {len(to_eval)}\n")

    for i, qa in enumerate(to_eval):
        qa_id = qa["id"]
        question = qa["question"]
        ideal = qa["ideal_answer"]
        source = qa["source_file"]

        print(f"[{i + 1}/{len(to_eval)}] {question[:55]}...")

        # Step 1: RAG retrieval
        rag = await get_rag_answer(conn, http, question)
        correct_top1 = rag.get("top1_file") == source
        correct_top3 = source in rag.get("sources", [])

        # Step 2: Generate RAG answer from context
        rag_answer = generate_rag_answer(question, rag["answer_context"])
        if not rag_answer:
            print(f"  SKIP — empty RAG answer")
            time.sleep(2)
            continue

        # Step 3: Evaluate RAG answer vs ideal
        eval_scores = claude_evaluate(question, ideal, rag_answer)
        if not eval_scores:
            print(f"  SKIP — evaluation failed")
            time.sleep(2)
            continue

        eval_entry = {
            "qa_id": qa_id,
            "chunk_id": qa["chunk_id"],
            "source_file": source,
            "question": question,
            "ideal_answer": ideal,
            "rag_answer": rag_answer,
            "rag_sources": rag.get("sources", []),
            "cosine_score": round(rag["cosine"], 4),
            "reranker_score": round(rag["reranker"], 4),
            "correct_source_top1": correct_top1,
            "correct_source_top3": correct_top3,
            "eval_correctness": eval_scores.get("correctness", 0),
            "eval_completeness": eval_scores.get("completeness", 0),
            "eval_relevance": eval_scores.get("relevance", 0),
            "eval_hallucination": eval_scores.get("hallucination", 5),
            "eval_overall": eval_scores.get("overall", 0),
            "eval_issues": eval_scores.get("issues", ""),
        }
        evaluations.append(eval_entry)

        # Save incrementally — JSON file
        EVAL_FILE.write_text(json.dumps(evaluations, indent=2, ensure_ascii=False))

        # Save to DB
        try:
            await conn.execute("""
                INSERT INTO qa_evaluations (qa_id, rag_answer, rag_sources, cosine_score, reranker_score,
                    correct_source_top1, correct_source_top3, eval_correctness, eval_completeness,
                    eval_relevance, eval_hallucination, eval_overall, eval_issues)
                VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13)
            """, eval_entry["qa_id"], eval_entry["rag_answer"],
                json.dumps(eval_entry["rag_sources"]),
                eval_entry["cosine_score"], eval_entry["reranker_score"],
                eval_entry["correct_source_top1"], eval_entry["correct_source_top3"],
                eval_entry["eval_correctness"], eval_entry["eval_completeness"],
                eval_entry["eval_relevance"], eval_entry["eval_hallucination"],
                eval_entry["eval_overall"], eval_entry["eval_issues"])
        except Exception as db_err:
            print(f"  DB write error: {db_err}")

        status = "✓" if eval_scores.get("overall", 0) >= 4 else ("~" if eval_scores.get("overall", 0) >= 3 else "✗")
        src_mark = "top-1" if correct_top1 else ("top-3" if correct_top3 else "miss")
        print(f"  {status} overall:{eval_scores.get('overall')}/5 correct:{eval_scores.get('correctness')}/5 complete:{eval_scores.get('completeness')}/5 retrieval:{src_mark}")

        time.sleep(2)

    await http.aclose()
    await conn.close()

    # Summary
    if not evaluations:
        print("No evaluations to summarize.")
        return

    n = len(evaluations)
    avg_correct = sum(e["eval_correctness"] for e in evaluations) / n
    avg_complete = sum(e["eval_completeness"] for e in evaluations) / n
    avg_relevance = sum(e["eval_relevance"] for e in evaluations) / n
    avg_halluc = sum(e["eval_hallucination"] for e in evaluations) / n
    avg_overall = sum(e["eval_overall"] for e in evaluations) / n
    top1_acc = sum(1 for e in evaluations if e["correct_source_top1"])
    top3_acc = sum(1 for e in evaluations if e["correct_source_top3"])
    avg_cosine = sum(e["cosine_score"] for e in evaluations) / n
    avg_reranker = sum(e["reranker_score"] for e in evaluations) / n

    # Score distribution
    overall_dist = {}
    for e in evaluations:
        s = e["eval_overall"]
        overall_dist[s] = overall_dist.get(s, 0) + 1

    # Issues
    issues = [e for e in evaluations if e.get("eval_issues")]

    summary = {
        "total_evaluated": n,
        "avg_correctness": round(avg_correct, 2),
        "avg_completeness": round(avg_complete, 2),
        "avg_relevance": round(avg_relevance, 2),
        "avg_hallucination": round(avg_halluc, 2),
        "avg_overall": round(avg_overall, 2),
        "retrieval_top1_accuracy": f"{top1_acc}/{n} ({top1_acc * 100 // n}%)",
        "retrieval_top3_accuracy": f"{top3_acc}/{n} ({top3_acc * 100 // n}%)",
        "avg_cosine": round(avg_cosine, 4),
        "avg_reranker": round(avg_reranker, 4),
        "overall_score_distribution": overall_dist,
        "entries_with_issues": len(issues),
    }
    EVAL_SUMMARY.write_text(json.dumps(summary, indent=2))

    print(f"\n{'=' * 65}")
    print("EVALUATION SUMMARY")
    print(f"{'=' * 65}")
    print(f"  Evaluated:          {n} Q&A pairs")
    print(f"  Avg correctness:    {avg_correct:.2f}/5")
    print(f"  Avg completeness:   {avg_complete:.2f}/5")
    print(f"  Avg relevance:      {avg_relevance:.2f}/5")
    print(f"  Avg hallucination:  {avg_halluc:.2f}/5 (5=none)")
    print(f"  Avg overall:        {avg_overall:.2f}/5")
    print(f"  Retrieval top-1:    {top1_acc}/{n} ({top1_acc * 100 // n}%)")
    print(f"  Retrieval top-3:    {top3_acc}/{n} ({top3_acc * 100 // n}%)")
    print(f"  Avg cosine:         {avg_cosine:.4f}")
    print(f"  Avg reranker:       {avg_reranker:.4f}")
    print(f"\n  Score distribution:")
    for s in sorted(overall_dist.keys()):
        print(f"    {s}/5: {overall_dist[s]:>4} {'█' * overall_dist[s]}")
    if issues:
        print(f"\n  Entries with issues: {len(issues)}")
        for e in issues[:5]:
            print(f"    - [{e['qa_id']}] {e['eval_issues'][:80]}")

    # Merge eval results back into qa_dataset_v2.json
    print(f"\n  Merging evaluation scores into {QA_FILE.name}...")
    eval_by_id = {e["qa_id"]: e for e in evaluations}
    qa_data_fresh = json.loads(QA_FILE.read_text())
    merged = 0
    for entry in qa_data_fresh:
        ev = eval_by_id.get(entry["id"])
        if ev:
            entry["eval_rag_answer"] = ev["rag_answer"]
            entry["eval_rag_sources"] = ev["rag_sources"]
            entry["eval_correctness"] = ev["eval_correctness"]
            entry["eval_completeness"] = ev["eval_completeness"]
            entry["eval_relevance"] = ev["eval_relevance"]
            entry["eval_hallucination"] = ev["eval_hallucination"]
            entry["eval_overall"] = ev["eval_overall"]
            entry["eval_issues"] = ev["eval_issues"]
            merged += 1
    QA_FILE.write_text(json.dumps(qa_data_fresh, indent=2, ensure_ascii=False))
    print(f"  Merged {merged} eval results into {QA_FILE.name}")

    print(f"\n  Evaluation: {EVAL_FILE}")
    print(f"  Dataset:    {QA_FILE}")
    print(f"  Summary:    {EVAL_SUMMARY}")


if __name__ == "__main__":
    asyncio.run(main())
