"""
End-to-end RAG test through the FastAPI /api/chat endpoint.
Tests 15 relevant + 5 irrelevant queries.
"""

import asyncio
import httpx
import json
import time
from pathlib import Path

API_BASE = "http://localhost:8080"

RELEVANT_QUERIES = [
    "How do I set up two-factor authentication?",
    "How to install the backup agent on a Windows server?",
    "What are the system requirements for protection agents?",
    "How do I create a new protection plan?",
    "How to configure email alerts for backup failures?",
    "How to recover files from a cloud backup?",
    "How do I set up disaster recovery failover?",
    "How to configure antimalware real-time protection?",
    "What is endpoint detection and response in Acronis?",
    "How to set up data loss prevention policies?",
    "How do I manage software patches remotely?",
    "How to back up Microsoft 365 mailboxes?",
    "What is the CyberFit Score?",
    "How to configure VPN for disaster recovery?",
    "How to create bootable rescue media?",
]

IRRELEVANT_QUERIES = [
    "How to configure Salesforce integration?",
    "Can Acronis mine cryptocurrency?",
    "How to deploy a Kubernetes cluster?",
    "What is the best pizza recipe?",
    "How to set up AWS Lambda functions?",
]

REJECT_PHRASES = [
    "don't have",
    "no information",
    "not covered",
    "no relevant",
    "outside",
    "don't know",
    "cannot find",
    "not available",
    "no documentation",
    "not related",
    "beyond the scope",
    "i'm not able",
]


async def check_health(client: httpx.AsyncClient) -> dict:
    r = await client.get(f"{API_BASE}/api/health")
    return r.json()


async def send_query(client: httpx.AsyncClient, message: str) -> tuple[dict, float]:
    start = time.time()
    r = await client.post(
        f"{API_BASE}/api/chat",
        json={"message": message},
    )
    elapsed_ms = (time.time() - start) * 1000
    return r.json(), elapsed_ms


async def main():
    async with httpx.AsyncClient(timeout=180.0) as client:
        # Health check
        print("=" * 70)
        print("HEALTH CHECK")
        print("=" * 70)
        health = await check_health(client)
        print(f"  Status:        {health['status']}")
        print(f"  Chunks in DB:  {health['chunks_count']}")
        print(f"  GPU Embedding: {health['gpu_embedding']}")
        print(f"  GPU Reranker:  {health['gpu_reranker']}")
        print()

        results = []
        all_queries = [
            (q, "relevant") for q in RELEVANT_QUERIES
        ] + [
            (q, "irrelevant") for q in IRRELEVANT_QUERIES
        ]

        print("=" * 70)
        print("RUNNING 20 QUERIES")
        print("=" * 70)

        for i, (query, qtype) in enumerate(all_queries, 1):
            print(f"\n[{i}/20] {query[:60]}...")
            try:
                data, elapsed = await send_query(client, query)
                answer = data.get("answer", "")
                sources = data.get("sources", [])

                # Evaluate
                if qtype == "relevant":
                    has_answer = len(answer) > 50
                    has_sources = len(sources) > 0
                    status = "PASS" if has_answer and has_sources else ("WEAK" if has_answer else "FAIL")
                else:
                    answer_lower = answer.lower()
                    rejected = any(p in answer_lower for p in REJECT_PHRASES)
                    no_sources = len(sources) == 0
                    status = "PASS" if rejected or no_sources else "LEAK"

                preview = answer[:150].replace("\n", " ")
                source_names = [s["title"] for s in sources[:3]]

                print(f"  Status: {status} | Sources: {len(sources)} | Time: {elapsed:.0f}ms")
                print(f"  Answer: {preview}...")
                if source_names:
                    print(f"  Sources: {', '.join(source_names)}")

                results.append({
                    "index": i,
                    "query": query,
                    "type": qtype,
                    "status": status,
                    "answer": answer,
                    "answer_preview": preview,
                    "sources": sources,
                    "source_count": len(sources),
                    "response_time_ms": round(elapsed),
                })
            except Exception as e:
                print(f"  ERROR: {e}")
                results.append({
                    "index": i,
                    "query": query,
                    "type": qtype,
                    "status": "ERROR",
                    "answer": str(e),
                    "answer_preview": str(e)[:150],
                    "sources": [],
                    "source_count": 0,
                    "response_time_ms": 0,
                })

        # Summary
        print("\n" + "=" * 70)
        print("RESULTS TABLE")
        print("=" * 70)
        print(f"{'#':<3} {'Query':<50} {'Status':<6} {'Src':<4} {'Time':<8}")
        print("-" * 70)
        for r in results:
            q_short = r["query"][:48]
            print(f"{r['index']:<3} {q_short:<50} {r['status']:<6} {r['source_count']:<4} {r['response_time_ms']}ms")

        # Stats
        relevant_results = [r for r in results if r["type"] == "relevant"]
        irrelevant_results = [r for r in results if r["type"] == "irrelevant"]

        rel_pass = sum(1 for r in relevant_results if r["status"] in ("PASS", "WEAK"))
        rel_with_sources = sum(1 for r in relevant_results if r["source_count"] > 0)
        irr_pass = sum(1 for r in irrelevant_results if r["status"] == "PASS")

        times = [r["response_time_ms"] for r in results if r["response_time_ms"] > 0]
        avg_time = sum(times) / len(times) if times else 0
        fastest = min(results, key=lambda r: r["response_time_ms"] if r["response_time_ms"] > 0 else 999999)
        slowest = max(results, key=lambda r: r["response_time_ms"])
        errors = sum(1 for r in results if r["status"] == "ERROR")

        print("\n" + "=" * 70)
        print("SUMMARY")
        print("=" * 70)
        print(f"  Relevant answered:          {rel_pass}/15")
        print(f"  Relevant with sources:      {rel_with_sources}/15")
        print(f"  Irrelevant rejected:        {irr_pass}/5")
        print(f"  Errors:                     {errors}/20")
        print(f"  Average response time:      {avg_time:.0f}ms")
        print(f"  Fastest: [{fastest['response_time_ms']}ms] {fastest['query'][:50]}")
        print(f"  Slowest: [{slowest['response_time_ms']}ms] {slowest['query'][:50]}")

        # Save JSON
        output = {
            "health": health,
            "summary": {
                "relevant_answered": rel_pass,
                "relevant_with_sources": rel_with_sources,
                "irrelevant_rejected": irr_pass,
                "errors": errors,
                "avg_response_time_ms": round(avg_time),
            },
            "results": results,
        }
        out_path = Path(__file__).parent.parent / "data" / "chat_api_test.json"
        out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False))
        print(f"\n  Results saved to: {out_path}")


if __name__ == "__main__":
    asyncio.run(main())
