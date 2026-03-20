"""
Minimal test: generate 6 Q&A pairs for ONE chunk, save immediately.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import agent.sdk_patch  # noqa

import asyncio, json, re, asyncpg
from claude_code_sdk import query, ClaudeCodeOptions, AssistantMessage, TextBlock

DB_DSN = "postgresql://acronis:acronis@localhost:5432/acronis_agent"
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "qa_dataset.json"))


async def sdk_query(system: str, user: str) -> str:
    parts = []
    try:
        async for msg in query(prompt=user, options=ClaudeCodeOptions(system_prompt=system, max_turns=1)):
            if msg and isinstance(msg, AssistantMessage):
                for b in msg.content:
                    if isinstance(b, TextBlock):
                        parts.append(b.text)
    except Exception as e:
        if "Unknown message type" not in str(e):
            raise
    return "\n".join(parts)


async def search_direct(question: str) -> dict:
    from agent.tools import search_docs
    result = await search_docs.handler({"query": question, "top_k": 3})
    text = result["content"][0]["text"]
    retrieved, top_cos, top_rer = [], 0.0, 0.0
    for m in re.finditer(r"\[Reranker: ([\d.]+) \| Cosine: ([\d.]+)\] .+\nSource: (.+)\n", text):
        top_rer = max(top_rer, float(m.group(1)))
        top_cos = max(top_cos, float(m.group(2)))
        retrieved.append(m.group(3))
    return {"retrieved": retrieved, "cos": round(top_cos, 4), "rer": round(top_rer, 4),
            "no_results": "No relevant" in text, "context": text}


async def main():
    # Get ONE chunk
    conn = await asyncpg.connect(DB_DSN)
    chunk = await conn.fetchrow("SELECT id, title, content, source_file FROM chunks ORDER BY id LIMIT 1")
    await conn.close()
    print(f"Chunk: {chunk['title']} ({chunk['source_file']})")

    # Generate 6 questions
    print("Generating questions...")
    raw = await sdk_query(
        "Return ONLY a JSON array of 6 objects. No markdown, no explanation.\n"
        "Each: {\"persona\":\"X\",\"question\":\"...\",\"answerable\":true/false}\n"
        "Personas: NEW_ADMIN, EXPERIENCED_SYSADMIN, END_USER, MANAGER, IRRELEVANT(answerable=false), ADVERSARIAL",
        f"Title: {chunk['title']}\nContent:\n{chunk['content'][:1500]}"
    )
    print(f"Raw response length: {len(raw)}")

    # Parse JSON
    cleaned = re.sub(r"```json?\s*|```", "", raw).strip()
    match = re.search(r"\[[\s\S]*\]", cleaned)
    if not match:
        print(f"FAIL: Could not parse JSON from:\n{raw[:500]}")
        return
    questions = json.loads(match.group(0))
    print(f"Parsed {len(questions)} questions")

    # Answer each
    dataset = []
    for i, q in enumerate(questions):
        print(f"  {i+1}/6 {q['persona']}: {q['question'][:60]}...")

        retrieval = await search_direct(q["question"])

        answer = await sdk_query(
            "You are an Acronis support agent. Answer based on the docs below. Cite source file. Be concise.",
            f"Docs:\n{retrieval['context']}\n\n---\nQuestion: {q['question']}"
        )

        entry = {
            "id": f"chunk_{chunk['id']:02d}_{q['persona']}",
            "chunk_id": chunk["id"],
            "chunk_title": chunk["title"],
            "source_file": chunk["source_file"],
            "persona": q["persona"],
            "question": q["question"],
            "expected_answerable": q.get("answerable", True),
            "agent_answer": answer,
            "retrieved_chunks": retrieval["retrieved"],
            "top_cosine_score": retrieval["cos"],
            "top_reranker_score": retrieval["rer"],
            "answer_cites_source": chunk["source_file"] in answer,
        }
        dataset.append(entry)

        # Save after each
        with open(OUT, "w") as f:
            json.dump(dataset, f, indent=2, ensure_ascii=False)

        print(f"    cos={retrieval['cos']:.2f} rer={retrieval['rer']:.2f} saved ✓")

    print(f"\nDone! {len(dataset)} entries → {OUT}")


if __name__ == "__main__":
    asyncio.run(main())
