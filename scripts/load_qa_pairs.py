"""
Load Q&A pairs into pgvector with question embeddings.
Only loads quality_score >= 4. Embeds the QUESTION text for similarity matching.
"""

import asyncio
import json
import asyncpg
import httpx
from pathlib import Path

DB_DSN = "postgresql://acronis:acronis@localhost:5432/acronis_agent"
EMBED_URL = "http://192.168.1.8:8011/v1/embeddings"
EMBED_MODEL = "Qwen/Qwen3-Embedding-4B"
BATCH_SIZE = 16
QA_FILE = Path(__file__).parent.parent / "data" / "qa_dataset_v2.json"
MIN_QUALITY = 4

QUERY_INSTRUCTION = "Instruct: Given a web search query, retrieve relevant passages that answer the query about Acronis Cyber Protect Cloud\nQuery: "


async def embed_batch(client: httpx.AsyncClient, texts: list[str]) -> list[list[float]]:
    prefixed = [QUERY_INSTRUCTION + t for t in texts]
    resp = await client.post(EMBED_URL, json={"input": prefixed, "model": EMBED_MODEL})
    resp.raise_for_status()
    data = resp.json()["data"]
    data.sort(key=lambda x: x["index"])
    return [d["embedding"] for d in data]


async def main():
    with open(QA_FILE) as f:
        all_pairs = json.load(f)

    print(f"Total Q&A pairs in file: {len(all_pairs)}")

    # Filter by quality
    pairs = [p for p in all_pairs if p.get("quality_score", 0) >= MIN_QUALITY]
    skipped = len(all_pairs) - len(pairs)
    print(f"Quality >= {MIN_QUALITY}: {len(pairs)} (skipped {skipped})")

    conn = await asyncpg.connect(DB_DSN)
    client = httpx.AsyncClient(timeout=60.0)

    # Clean start
    await conn.execute("TRUNCATE qa_pairs")
    print("Truncated qa_pairs table")

    # Embed questions in batches
    print(f"Embedding {len(pairs)} questions...")
    questions = [p["question"] for p in pairs]
    all_embeddings = []
    for i in range(0, len(questions), BATCH_SIZE):
        batch = questions[i:i + BATCH_SIZE]
        embs = await embed_batch(client, batch)
        all_embeddings.extend(embs)
        print(f"  Batch {i // BATCH_SIZE + 1}/{(len(questions) - 1) // BATCH_SIZE + 1}")

    # Insert
    print("Inserting into qa_pairs...")
    for pair, emb in zip(pairs, all_embeddings):
        emb_str = "[" + ",".join(str(float(x)) for x in emb) + "]"
        await conn.execute(
            """INSERT INTO qa_pairs (id, chunk_id, source_file, section, question, ideal_answer,
                                     type, difficulty, quality_score, cosine_score, reranker_score,
                                     correct_source_in_top1, correct_source_in_top3, verified, embedding)
               VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15::vector)""",
            pair["id"], pair.get("chunk_id"), pair.get("source_file"), pair.get("section"),
            pair["question"], pair["ideal_answer"],
            pair.get("type"), pair.get("difficulty"), pair.get("quality_score"),
            pair.get("cosine_score"), pair.get("reranker_score"),
            pair.get("correct_source_in_top1", False), pair.get("correct_source_in_top3", False),
            pair.get("verified", False), emb_str,
        )

    total = await conn.fetchval("SELECT count(*) FROM qa_pairs")
    await client.aclose()
    await conn.close()
    print(f"\nLoaded {total} Q&A pairs (skipped {skipped} low quality)")


if __name__ == "__main__":
    asyncio.run(main())
