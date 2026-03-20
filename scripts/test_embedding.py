"""
End-to-end test: parse a chunk → embed with BGE-M3 → store in pgvector → similarity search.
"""

import asyncio
import re
import yaml
import asyncpg
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer

# ── Config ──────────────────────────────────────────────────
DB_DSN = "postgresql://acronis:acronis@localhost:5432/acronis_agent"
DOCS_DIR = Path.home() / "Documents/Projects/acronis-genie/docs"
CHUNK_FILE = DOCS_DIR / "01-getting-started/03-two-factor-authentication.md"
EMBEDDING_MODEL = "BAAI/bge-m3"


def parse_chunk(path: Path) -> dict:
    """Parse a markdown chunk with YAML frontmatter."""
    text = path.read_text()
    match = re.match(r"^---\n(.+?)\n---\n(.+)", text, re.DOTALL)
    if not match:
        raise ValueError(f"No frontmatter found in {path}")
    meta = yaml.safe_load(match.group(1))
    content = match.group(2).strip()
    return {
        "title": meta.get("title", ""),
        "section": meta.get("section"),
        "subsection": meta.get("subsection"),
        "page_range": meta.get("page_range"),
        "tags": meta.get("tags", []),
        "source_file": path.name,
        "content": content,
        "word_count": len(content.split()),
    }


async def main():
    # 1. Parse chunk
    print("1. Parsing chunk...")
    chunk = parse_chunk(CHUNK_FILE)
    print(f"   Title: {chunk['title']}")
    print(f"   Words: {chunk['word_count']}")
    print(f"   Tags:  {chunk['tags']}")

    # 2. Generate embedding
    print(f"\n2. Loading {EMBEDDING_MODEL}...")
    model = SentenceTransformer(EMBEDDING_MODEL)
    embedding = model.encode(chunk["content"], normalize_embeddings=True)
    print(f"   Embedding shape: {embedding.shape}")
    print(f"   Embedding dtype: {embedding.dtype}")
    print(f"   First 5 values:  {embedding[:5]}")

    # 3. Connect to pgvector and insert
    print("\n3. Inserting into pgvector...")
    conn = await asyncpg.connect(DB_DSN)
    try:
        # Clear previous test data
        await conn.execute("DELETE FROM chunks WHERE source_file = $1", chunk["source_file"])

        # Insert chunk with embedding
        embedding_str = "[" + ",".join(str(float(x)) for x in embedding) + "]"
        await conn.execute(
            """
            INSERT INTO chunks (title, section, subsection, content, page_range, tags, source_file, word_count, embedding)
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9::vector)
            """,
            chunk["title"],
            chunk["section"],
            chunk["subsection"],
            chunk["content"],
            chunk["page_range"],
            chunk["tags"],
            chunk["source_file"],
            chunk["word_count"],
            embedding_str,
        )
        count = await conn.fetchval("SELECT count(*) FROM chunks")
        print(f"   Inserted! Total chunks in DB: {count}")

        # 4. Similarity search
        print("\n4. Similarity search test...")
        query_text = "How do I set up two-factor authentication?"
        query_embedding = model.encode(query_text, normalize_embeddings=True)
        query_str = "[" + ",".join(str(float(x)) for x in query_embedding) + "]"

        rows = await conn.fetch(
            """
            SELECT id, title, source_file, word_count,
                   1 - (embedding <=> $1::vector) AS similarity
            FROM chunks
            ORDER BY embedding <=> $1::vector
            LIMIT 3
            """,
            query_str,
        )

        print(f"   Query: '{query_text}'")
        print(f"   Results:")
        for row in rows:
            print(f"   ├─ [{row['similarity']:.4f}] {row['title']}")
            print(f"   │  File: {row['source_file']}, Words: {row['word_count']}")

        if rows:
            # Show snippet from top result
            top = await conn.fetchval(
                "SELECT content FROM chunks WHERE id = $1", rows[0]["id"]
            )
            snippet = top[:200].replace("\n", " ")
            print(f"   └─ Snippet: {snippet}...")

        print("\n✅ Pipeline works end-to-end!")

    finally:
        await conn.close()


if __name__ == "__main__":
    asyncio.run(main())
