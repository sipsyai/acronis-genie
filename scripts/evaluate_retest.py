"""Re-evaluate only the low-scoring Q&A pairs with updated prompt and full content."""
import asyncio, json, subprocess, time, asyncpg, httpx
from pathlib import Path

DB_DSN = "postgresql://acronis:acronis@localhost:5432/acronis_agent"
EMBED_URL = "http://192.168.1.8:8011/v1/embeddings"
EMBED_MODEL = "Qwen/Qwen3-Embedding-4B"
RERANK_URL = "http://192.168.1.8:8012/rerank"
DATA_DIR = Path.home() / "Documents/Projects/acronis-genie/data"
QA_FILE = DATA_DIR / "qa_retest_low.json"
EVAL_FILE = DATA_DIR / "qa_retest_eval.json"

EVAL_PROMPT = """You are a strict evaluator comparing a RAG system answer against an ideal answer.
Score the RAG answer:
1. correctness (0-5): factual accuracy vs ideal
2. completeness (0-5): covers all key points from ideal
3. relevance (0-5): relevant to the question
4. hallucination (0-5): 5=no hallucination, 0=completely made up
Return ONLY valid JSON: {"correctness":4,"completeness":3,"relevance":5,"hallucination":5,"overall":4,"issues":"brief note"}"""

def claude_eval(question, ideal, rag_answer):
    prompt = f"Question: {question}\nIdeal: {ideal}\nRAG: {rag_answer[:1500]}\nScore the RAG answer."
    try:
        r = subprocess.run(["claude", "-p", prompt, "--system-prompt", EVAL_PROMPT,
            "--output-format", "text", "--max-turns", "1"], capture_output=True, text=True, timeout=60)
        if r.returncode == 0:
            text = r.stdout.strip()
            s = text.find("{"); e = text.rfind("}")
            if s != -1 and e > s:
                return json.loads(text[s:e+1])
    except: pass
    return None

def get_rag_answer(question):
    try:
        import httpx as hx
        r = hx.post("http://localhost:8080/api/chat", json={"message": question}, timeout=120)
        return r.json().get("answer", "")
    except: return ""

async def main():
    qa_data = json.loads(QA_FILE.read_text())
    print(f"Re-testing {len(qa_data)} low-scoring questions\n")
    
    results = []
    for i, qa in enumerate(qa_data):
        q = qa["question"]
        ideal = qa["ideal_answer"]
        source = qa["source_file"]
        print(f"[{i+1}/{len(qa_data)}] {q[:55]}...")
        
        rag = get_rag_answer(q)
        if not rag or len(rag) < 20:
            print(f"  SKIP — empty RAG answer")
            time.sleep(2)
            continue
        
        scores = claude_eval(q, ideal, rag)
        if not scores:
            print(f"  SKIP — eval failed")
            time.sleep(2)
            continue
        
        entry = {
            "qa_id": qa["id"], "source_file": source, "question": q,
            "ideal_answer": ideal, "rag_answer": rag,
            "eval_correctness": scores.get("correctness",0),
            "eval_completeness": scores.get("completeness",0),
            "eval_relevance": scores.get("relevance",0),
            "eval_hallucination": scores.get("hallucination",5),
            "eval_overall": scores.get("overall",0),
            "eval_issues": scores.get("issues",""),
        }
        results.append(entry)
        EVAL_FILE.write_text(json.dumps(results, indent=2, ensure_ascii=False))
        
        s = "✓" if scores.get("overall",0)>=4 else ("~" if scores.get("overall",0)>=3 else "✗")
        print(f"  {s} overall:{scores.get('overall')}/5 correct:{scores.get('correctness')}/5 complete:{scores.get('completeness')}/5")
        time.sleep(2)
    
    # Summary
    n = len(results)
    if n == 0: return
    avg_o = sum(e["eval_overall"] for e in results)/n
    avg_c = sum(e["eval_correctness"] for e in results)/n
    avg_cp = sum(e["eval_completeness"] for e in results)/n
    avg_h = sum(e["eval_hallucination"] for e in results)/n
    dist = {}
    for e in results:
        s = e["eval_overall"]; dist[s] = dist.get(s,0)+1
    
    print(f"\n{'='*60}")
    print(f"RETEST SUMMARY ({n} questions)")
    print(f"{'='*60}")
    print(f"  Avg overall:      {avg_o:.2f}/5  (was 1.44/5)")
    print(f"  Avg correctness:  {avg_c:.2f}/5")
    print(f"  Avg completeness: {avg_cp:.2f}/5")
    print(f"  Avg hallucination:{avg_h:.2f}/5")
    print(f"  Distribution: {dict(sorted(dist.items()))}")
    
    improved = sum(1 for e in results if e["eval_overall"] >= 3)
    print(f"  Improved to 3+: {improved}/{n} ({improved*100//n}%)")

asyncio.run(main())
