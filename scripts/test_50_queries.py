"""
50-query search quality test across all 15 chapters.
Uses cosine similarity (pgvector) + BGE reranker (TEI on GPU server).
"""

import asyncio
import json
import httpx
import asyncpg
from pathlib import Path

DB_DSN = "postgresql://acronis:acronis@localhost:5432/acronis_agent"
EMBED_URL = "http://192.168.1.8:8011/v1/embeddings"
EMBED_MODEL = "Qwen/Qwen3-Embedding-4B"
RERANK_URL = "http://192.168.1.8:8012/rerank"
TOP_K_COSINE = 10  # Retrieve top-10 by cosine, then rerank
TOP_K_FINAL = 3    # Show top-3 after reranking

QUERIES = [
    # Chapter 01 - Getting Started
    ("How do I activate my Acronis account?", "01"),
    ("What are the password requirements for Acronis console?", "01"),
    ("Which web browsers are supported by Acronis?", "01"),
    # Chapter 02 - Installing/Deploying Agents
    ("How do I install the protection agent on Windows?", "02"),
    ("What are the system requirements for Acronis agents?", "02"),
    ("How to deploy agents via command line silently?", "02"),
    ("How to set up the virtual appliance for VMware?", "02"),
    ("How does device discovery work in Acronis?", "02"),
    # Chapter 03 - Working with Plans
    ("How do I create a protection plan?", "03"),
    ("What types of protection plans are available?", "03"),
    ("How to configure plan validation and cleanup?", "03"),
    ("How do I set up SIEM integration?", "03"),
    # Chapter 04 - Monitoring/Dashboards
    ("How do I configure alerts in Acronis?", "04"),
    ("What dashboard widgets are available?", "04"),
    ("How to generate reports in Acronis console?", "04"),
    ("How to monitor backup status across all machines?", "04"),
    # Chapter 05 - Managing Workloads
    ("How do I manage device groups?", "05"),
    ("What is CyberFit Score?", "05"),
    ("How to run scripts remotely on workloads?", "05"),
    # Chapter 06 - Backup and Recovery
    ("How do I back up a SQL Server database?", "06"),
    ("How to configure continuous data protection?", "06"),
    ("How to recover files from a backup?", "06"),
    ("How do I back up Microsoft 365 mailboxes?", "06"),
    ("How to create bootable rescue media?", "06"),
    ("How to back up Oracle databases?", "06"),
    ("What backup options are available for Google Workspace?", "06"),
    ("How do I configure backup encryption?", "06"),
    # Chapter 07 - Disaster Recovery
    ("How do I perform a failover in disaster recovery?", "07"),
    ("How to configure VPN for disaster recovery?", "07"),
    ("How to set up disaster recovery to Azure?", "07"),
    ("What is the disaster recovery dashboard?", "07"),
    ("How does failback work after disaster recovery?", "07"),
    # Chapter 08 - Antivirus/Antimalware
    ("How do I configure antimalware protection?", "08"),
    ("How to set up URL filtering?", "08"),
    ("How to manage quarantined files?", "08"),
    ("How to whitelist trusted applications?", "08"),
    # Chapter 09 - GenAI/Workflows
    ("What is GenAI Protection in Acronis?", "09"),
    ("How do I set up automated workflows?", "09"),
    # Chapter 10 - EDR/XDR
    ("How does endpoint detection and response work?", "10"),
    ("How to investigate security incidents in XDR?", "10"),
    ("How to remediate threats with EDR?", "10"),
    # Chapter 11 - MDR
    ("What MDR service levels are available?", "11"),
    ("How to enable managed detection and response?", "11"),
    # Chapter 12 - RMM
    ("How to manage patches and software updates?", "12"),
    ("How to do hardware inventory remotely?", "12"),
    ("How to use remote desktop in Acronis?", "12"),
    ("How to monitor system performance of workloads?", "12"),
    # Chapter 13 - DLP
    ("How to configure data loss prevention policies?", "13"),
    ("How to create custom sensitive data detectors?", "13"),
    # Chapter 14 - Additional
    ("How to set up immutable backup storage?", "14"),
]


async def embed_query(client: httpx.AsyncClient, text: str) -> list[float]:
    resp = await client.post(EMBED_URL, json={"input": text, "model": EMBED_MODEL})
    resp.raise_for_status()
    return resp.json()["data"][0]["embedding"]


async def rerank(client: httpx.AsyncClient, query: str, texts: list[str]) -> list[dict]:
    resp = await client.post(RERANK_URL, json={"query": query, "texts": texts})
    resp.raise_for_status()
    results = resp.json()
    results.sort(key=lambda x: x["score"], reverse=True)
    return results


async def main():
    conn = await asyncpg.connect(DB_DSN)
    client = httpx.AsyncClient(timeout=30.0)

    results = []
    top1_correct = 0
    top3_correct = 0
    chapter_stats = {}  # chapter -> {queries, top1, top3, cosine_scores, reranker_scores}

    print("=" * 70)
    print("   50-QUERY SEARCH QUALITY TEST (Cosine + Reranker)")
    print("=" * 70)
    print()

    for idx, (query, expected_ch) in enumerate(QUERIES, 1):
        # 1. Embed query
        q_emb = await embed_query(client, query)
        q_str = "[" + ",".join(str(float(x)) for x in q_emb) + "]"

        # 2. Cosine retrieval top-10
        rows = await conn.fetch(
            """
            SELECT title, source_file, content,
                   1 - (embedding <=> $1::vector) AS cosine_sim
            FROM chunks
            ORDER BY embedding <=> $1::vector
            LIMIT $2
            """,
            q_str,
            TOP_K_COSINE,
        )

        # 3. Rerank top-10
        texts = [r["content"][:2000] for r in rows]  # truncate for reranker
        rerank_results = await rerank(client, query, texts)

        # Build final top-3
        top3 = []
        for rr in rerank_results[:TOP_K_FINAL]:
            orig_row = rows[rr["index"]]
            sf = orig_row["source_file"]
            ch = sf.split("-")[0]  # "02" from "02-installing-deploying-agents/..."
            top3.append({
                "title": orig_row["title"],
                "source_file": sf,
                "chapter": ch,
                "cosine": float(orig_row["cosine_sim"]),
                "reranker": float(rr["score"]),
            })

        # 4. Check accuracy
        top1_ch = top3[0]["chapter"] if top3 else ""
        top3_chs = [t["chapter"] for t in top3]
        is_top1 = top1_ch == expected_ch
        is_top3 = expected_ch in top3_chs

        if is_top1:
            top1_correct += 1
        if is_top3:
            top3_correct += 1

        # Track per-chapter stats
        if expected_ch not in chapter_stats:
            chapter_stats[expected_ch] = {"queries": 0, "top1": 0, "top3": 0, "cosine": [], "reranker": []}
        chapter_stats[expected_ch]["queries"] += 1
        if is_top1:
            chapter_stats[expected_ch]["top1"] += 1
        if is_top3:
            chapter_stats[expected_ch]["top3"] += 1
        chapter_stats[expected_ch]["cosine"].append(top3[0]["cosine"])
        chapter_stats[expected_ch]["reranker"].append(top3[0]["reranker"])

        # Print result
        mark = "OK" if is_top1 else ("~3" if is_top3 else "MISS")
        print(f"[{mark:>4}] Q{idx:02d}: {query}")
        for i, t in enumerate(top3, 1):
            print(f"        {i}. [cos={t['cosine']:.3f} rr={t['reranker']:.4f}] {t['title']}")
            print(f"           └─ {t['source_file']}")

        results.append({
            "id": idx,
            "query": query,
            "expected_chapter": expected_ch,
            "top1_correct": is_top1,
            "top3_correct": is_top3,
            "results": top3,
        })

    await client.aclose()
    await conn.close()

    # ── Analysis ──────────────────────────────────────────
    print("\n" + "=" * 70)
    print("   ANALYSIS")
    print("=" * 70)

    print(f"\n### 1. Overall Accuracy")
    print(f"   Top-1: {top1_correct}/50 ({top1_correct * 100 // 50}%)")
    print(f"   Top-3: {top3_correct}/50 ({top3_correct * 100 // 50}%)")

    print(f"\n### 2. Per-Chapter Breakdown")
    print(f"   {'Ch':>3} {'Queries':>7} {'Top-1':>6} {'Top-3':>6} {'AvgCos':>8} {'AvgRR':>8}")
    print(f"   {'---':>3} {'-------':>7} {'-----':>6} {'-----':>6} {'------':>8} {'-----':>8}")
    for ch in sorted(chapter_stats.keys()):
        s = chapter_stats[ch]
        avg_cos = sum(s["cosine"]) / len(s["cosine"])
        avg_rr = sum(s["reranker"]) / len(s["reranker"])
        print(f"   {ch:>3} {s['queries']:>7} {s['top1']:>6} {s['top3']:>6} {avg_cos:>8.4f} {avg_rr:>8.4f}")

    print(f"\n### 3. Failed Queries (wrong chapter in top-1)")
    fails = [r for r in results if not r["top1_correct"]]
    if not fails:
        print("   None! Perfect top-1 accuracy.")
    else:
        for r in fails:
            got_ch = r["results"][0]["chapter"] if r["results"] else "?"
            print(f"   Q{r['id']:02d}: expected={r['expected_chapter']}, got={got_ch}")
            print(f"        \"{r['query']}\"")
            print(f"        → {r['results'][0]['title']} ({r['results'][0]['source_file']})")

    print(f"\n### 4. Low Confidence Results (reranker < 0.10)")
    low = [r for r in results if r["results"] and r["results"][0]["reranker"] < 0.10]
    if not low:
        print("   None! All top results have good reranker confidence.")
    else:
        for r in low:
            print(f"   Q{r['id']:02d}: rr={r['results'][0]['reranker']:.4f} \"{r['query']}\"")

    print(f"\n### 5. Score Distribution")
    all_cos = [r["results"][0]["cosine"] for r in results if r["results"]]
    all_rr = [r["results"][0]["reranker"] for r in results if r["results"]]
    print(f"   Cosine:   avg={sum(all_cos)/len(all_cos):.4f}  min={min(all_cos):.4f}  max={max(all_cos):.4f}")
    print(f"   Reranker: avg={sum(all_rr)/len(all_rr):.4f}  min={min(all_rr):.4f}  max={max(all_rr):.4f}")

    # Save results
    out_path = Path(__file__).parent.parent / "data" / "search_quality_50.json"
    out_path.parent.mkdir(exist_ok=True)
    with open(out_path, "w") as f:
        json.dump({
            "total_queries": 50,
            "top1_accuracy": top1_correct,
            "top3_accuracy": top3_correct,
            "results": results,
        }, f, indent=2)
    print(f"\n### 6. Results saved to {out_path}")


if __name__ == "__main__":
    asyncio.run(main())
