"""
Load ALL chapter markdown chunks into pgvector.
Re-runnable: skips already-loaded chunks, only inserts new ones.
Uses remote GPU server (192.168.1.8:8011) for embeddings via OpenAI-compatible API.
"""

import asyncio
import re
import yaml
import asyncpg
import httpx
from pathlib import Path

DB_DSN = "postgresql://acronis:acronis@localhost:5432/acronis_agent"
DOCS_DIR = Path.home() / "Documents/Projects/acronis-genie/docs"
EMBED_URL = "http://192.168.1.8:8011/v1/embeddings"
EMBED_MODEL = "Qwen/Qwen3-Embedding-4B"
EMBED_DIM = 2560
BATCH_SIZE = 16  # GPU can handle larger batches


def parse_chunk(path: Path, chapter_dir_name: str) -> dict:
    text = path.read_text()
    match = re.match(r"^---\n(.+?)\n---\n(.+)", text, re.DOTALL)
    if not match:
        raise ValueError(f"No frontmatter in {path}")
    meta = yaml.safe_load(match.group(1))
    content = match.group(2).strip()
    source_file = f"{chapter_dir_name}/{path.name}"
    return {
        "title": meta.get("title", ""),
        "section": meta.get("section"),
        "subsection": meta.get("subsection"),
        "page_range": meta.get("page_range"),
        "tags": meta.get("tags", []),
        "source_file": source_file,
        "content": content,
        "word_count": len(content.split()),
        "doc_url": meta.get("doc_url"),
    }


async def get_embeddings(texts: list[str]) -> list[list[float]]:
    """Get embeddings from remote GPU server in batches."""
    all_embeddings = []
    async with httpx.AsyncClient(timeout=120.0) as client:
        for i in range(0, len(texts), BATCH_SIZE):
            batch = texts[i : i + BATCH_SIZE]
            resp = await client.post(
                EMBED_URL,
                json={"input": batch, "model": EMBED_MODEL},
            )
            resp.raise_for_status()
            data = resp.json()["data"]
            # Sort by index to ensure order
            data.sort(key=lambda x: x["index"])
            all_embeddings.extend([d["embedding"] for d in data])
            print(f"  Embedded batch {i // BATCH_SIZE + 1}/{(len(texts) - 1) // BATCH_SIZE + 1} ({len(batch)} chunks)")
    return all_embeddings


async def get_single_embedding(text: str) -> list[float]:
    """Get a single embedding for a query."""
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.post(
            EMBED_URL,
            json={"input": text, "model": EMBED_MODEL},
        )
        resp.raise_for_status()
        return resp.json()["data"][0]["embedding"]


async def main():
    # Discover all chapter directories and .md files
    chapter_dirs = sorted([d for d in DOCS_DIR.iterdir() if d.is_dir() and d.name[0].isdigit()])
    all_files = []
    for d in chapter_dirs:
        md_files = sorted(d.glob("*.md"))
        for f in md_files:
            all_files.append((d.name, f))

    print(f"Found {len(all_files)} .md files across {len(chapter_dirs)} chapters")
    for d in chapter_dirs:
        count = len(list(d.glob("*.md")))
        if count > 0:
            print(f"  {d.name}: {count} files")
    print()

    # Parse all chunks
    chunks = []
    for chapter_dir_name, f in all_files:
        try:
            chunks.append(parse_chunk(f, chapter_dir_name))
        except ValueError as e:
            print(f"  SKIP: {e}")

    # Connect to DB
    conn = await asyncpg.connect(DB_DSN)
    try:
        # Check for --fresh flag to truncate
        import sys
        if "--fresh" in sys.argv:
            await conn.execute("TRUNCATE chunks")
            print("TRUNCATED chunks table (fresh start)")
            existing_files = set()
        else:
            existing_rows = await conn.fetch("SELECT source_file FROM chunks")
            existing_files = {r["source_file"] for r in existing_rows}

        new_chunks = [c for c in chunks if c["source_file"] not in existing_files]
        already_loaded = len(chunks) - len(new_chunks)

        print(f"Already loaded: {already_loaded}")
        print(f"New to load: {len(new_chunks)}")
        print()

        if not new_chunks:
            print("Nothing new to load.")
        else:
            print(f"Generating embeddings via GPU server ({EMBED_URL})...")
            contents = [c["content"] for c in new_chunks]
            embeddings = await get_embeddings(contents)
            print()

            print("Inserting into pgvector...")
            for chunk, emb in zip(new_chunks, embeddings):
                emb_str = "[" + ",".join(str(float(x)) for x in emb) + "]"
                await conn.execute(
                    """
                    INSERT INTO chunks (title, section, subsection, content, page_range, tags, source_file, word_count, embedding, doc_url)
                    VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9::vector, $10)
                    """,
                    chunk["title"],
                    chunk["section"],
                    chunk["subsection"],
                    chunk["content"],
                    chunk["page_range"],
                    chunk["tags"],
                    chunk["source_file"],
                    chunk["word_count"],
                    emb_str,
                    chunk["doc_url"],
                )
                print(f"  Loaded: {chunk['source_file']} ({chunk['word_count']} words)")

        total = await conn.fetchval("SELECT count(*) FROM chunks")
        print(f"\nDone. Total chunks in DB: {total}\n")

        # ── Search quality tests ──────────────────────────────
        queries = [
            "How do I set up two-factor authentication?",
            "How to install backup agent on Windows?",
            "How do I create a protection plan?",
            "How to configure disaster recovery failover?",
            "How to set up antivirus protection?",
            "What is endpoint detection and response?",
            "How to configure data loss prevention?",
            "How to manage patches and updates?",
        ]

        print("=" * 60)
        print("SEARCH QUALITY TESTS")
        print("=" * 60)

        for q in queries:
            q_emb = await get_single_embedding(q)
            q_str = "[" + ",".join(str(float(x)) for x in q_emb) + "]"

            rows = await conn.fetch(
                """
                SELECT title, source_file, section,
                       1 - (embedding <=> $1::vector) AS similarity
                FROM chunks
                ORDER BY embedding <=> $1::vector
                LIMIT 3
                """,
                q_str,
            )

            print(f'\nQuery: "{q}"')
            for i, r in enumerate(rows, 1):
                print(f"  {i}. [{r['similarity']:.4f}] {r['title']}")
                print(f"     └─ {r['source_file']}")

    finally:
        await conn.close()


if __name__ == "__main__":
    asyncio.run(main())
