"""
Generate a Q&A evaluation dataset from pgvector chunks.
Incremental save — each Q&A pair written to disk immediately.
Resume support — skips already-completed chunk+persona combos.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import agent.sdk_patch  # noqa: F401

import asyncio
import json
import re
import time
import asyncpg
from claude_code_sdk import (
    query,
    ClaudeCodeOptions,
    AssistantMessage,
    ResultMessage,
    TextBlock,
)

DB_DSN = "postgresql://acronis:acronis@localhost:5432/acronis_agent"
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
DATASET_PATH = os.path.abspath(os.path.join(DATA_DIR, "qa_dataset.json"))

QGEN_SYSTEM_PROMPT = """\
You are a Q&A dataset generator for Acronis Cyber Protect Cloud documentation.
Given a documentation chunk, generate exactly 6 questions that different personas would ask.
Return ONLY a JSON array, no other text. No markdown fences, no explanation.

Personas and question styles:
1. NEW_ADMIN: Simple how-to question, beginner level.
2. EXPERIENCED_SYSADMIN: Specific technical question about details, edge cases, or limitations.
3. END_USER: Confused user, may use wrong terms or vague language.
4. MANAGER: High-level feature/capability question.
5. IRRELEVANT: Question that sounds related but is NOT answerable from this chunk.
6. ADVERSARIAL: Question with a wrong assumption that the agent should correct.

Format:
[
  {"persona": "NEW_ADMIN", "question": "...", "answerable": true},
  {"persona": "EXPERIENCED_SYSADMIN", "question": "...", "answerable": true},
  {"persona": "END_USER", "question": "...", "answerable": true},
  {"persona": "MANAGER", "question": "...", "answerable": true},
  {"persona": "IRRELEVANT", "question": "...", "answerable": false},
  {"persona": "ADVERSARIAL", "question": "...", "answerable": true}
]\
"""

ANSWER_SYSTEM_PROMPT = """\
You are an Acronis Cyber Protect Cloud support agent.
You have been given relevant documentation chunks retrieved from the knowledge base.
Answer the user's question based strictly on the provided documentation.
If the documentation doesn't contain relevant information, say you don't have information about that topic.
Cite the source file at the end of your answer. Be concise and helpful.\
"""


def load_dataset() -> list[dict]:
    if os.path.exists(DATASET_PATH):
        with open(DATASET_PATH) as f:
            return json.load(f)
    return []


def save_dataset(dataset: list[dict]):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(DATASET_PATH, "w") as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)


async def sdk_query(system_prompt: str, user_prompt: str) -> str:
    """One-shot Claude call using query()."""
    options = ClaudeCodeOptions(system_prompt=system_prompt, max_turns=1)
    parts = []
    try:
        async for msg in query(prompt=user_prompt, options=options):
            if msg is None:
                continue
            if isinstance(msg, AssistantMessage):
                for block in msg.content:
                    if isinstance(block, TextBlock):
                        parts.append(block.text)
    except Exception as e:
        if "Unknown message type" not in str(e):
            raise
    return "\n".join(parts)


async def search_direct(question: str) -> dict:
    """Call search_docs tool handler directly — no SDK session needed."""
    from agent.tools import search_docs
    result = await search_docs.handler({"query": question, "top_k": 3})
    text = result["content"][0]["text"]

    retrieved = []
    top_cosine = 0.0
    top_reranker = 0.0
    for match in re.finditer(
        r"\[Reranker: ([\d.]+) \| Cosine: ([\d.]+)\] (.+)\nSource: (.+)\n", text
    ):
        reranker_score = float(match.group(1))
        cosine_score = float(match.group(2))
        source = match.group(4)
        retrieved.append(source)
        top_cosine = max(top_cosine, cosine_score)
        top_reranker = max(top_reranker, reranker_score)

    no_results = "No relevant documentation found" in text
    return {
        "retrieved_chunks": retrieved,
        "top_cosine_score": round(top_cosine, 4),
        "top_reranker_score": round(top_reranker, 4),
        "no_results": no_results,
        "context_text": text,
    }


def parse_questions(text: str) -> list[dict] | None:
    cleaned = re.sub(r"```json?\s*", "", text)
    cleaned = re.sub(r"```\s*", "", cleaned)
    match = re.search(r"\[[\s\S]*\]", cleaned.strip())
    if match:
        try:
            items = json.loads(match.group(0))
            if isinstance(items, list) and len(items) == 6:
                return items
        except json.JSONDecodeError:
            pass
    return None


async def generate_questions_for_chunk(chunk: dict) -> list[dict] | None:
    """Generate 6 persona questions for a chunk. Retry once on failure."""
    user_prompt = (
        f"Generate 6 persona-based questions for this documentation chunk:\n\n"
        f"Title: {chunk['title']}\n"
        f"Source: {chunk['source_file']}\n"
        f"Content:\n{chunk['content']}"
    )
    for attempt in range(2):
        raw = await sdk_query(QGEN_SYSTEM_PROMPT, user_prompt)
        questions = parse_questions(raw)
        if questions:
            return questions
        if attempt == 0:
            print(f"    Retry question generation...")
            await asyncio.sleep(3)
    return None


async def generate_answer(question: str, context_text: str) -> str:
    """Generate answer using query() with pre-retrieved context — no MCP session."""
    user_prompt = (
        f"Retrieved documentation:\n\n{context_text}\n\n"
        f"---\n\nUser question: {question}"
    )
    return await sdk_query(ANSWER_SYSTEM_PROMPT, user_prompt)


async def main():
    print("=" * 60)
    print("  Q&A Dataset Generator (incremental)")
    print("=" * 60)

    # Load existing progress
    dataset = load_dataset()
    done_ids = {d["id"] for d in dataset}
    if done_ids:
        print(f"  Resuming: {len(done_ids)} Q&A pairs already done")

    # Read chunks from pgvector
    conn = await asyncpg.connect(DB_DSN)
    chunks = await conn.fetch(
        "SELECT id, title, content, source_file FROM chunks ORDER BY id"
    )
    await conn.close()
    print(f"  Chunks: {len(chunks)}")

    total_expected = len(chunks) * 6
    counter = len(done_ids)

    for idx, chunk in enumerate(chunks):
        chunk_id = chunk["id"]
        title = chunk["title"]
        source = chunk["source_file"]

        # Check if all 6 personas done for this chunk
        chunk_done_count = sum(
            1 for d in dataset if d["chunk_id"] == chunk_id
        )
        if chunk_done_count >= 6:
            print(f"\n[{idx+1}/{len(chunks)}] {title} — all 6 done, skipping")
            continue

        print(f"\n[{idx+1}/{len(chunks)}] {title}")

        # Generate questions (or use existing ones if partially done)
        questions = await generate_questions_for_chunk(chunk)
        if not questions:
            print(f"  SKIP: Failed to generate questions")
            continue

        await asyncio.sleep(2)

        for q in questions:
            persona = q["persona"]
            question_text = q["question"]
            answerable = q.get("answerable", True)
            qid = f"chunk_{chunk_id:02d}_persona_{persona}"

            if qid in done_ids:
                print(f"  Skipping {persona} (already done)")
                continue

            counter += 1

            # Direct search (no SDK session)
            try:
                retrieval = await search_direct(question_text)
            except Exception as e:
                print(f"  ERROR search: {e}")
                await asyncio.sleep(10)
                try:
                    retrieval = await search_direct(question_text)
                except Exception:
                    retrieval = {
                        "retrieved_chunks": [],
                        "top_cosine_score": 0,
                        "top_reranker_score": 0,
                        "no_results": True,
                        "context_text": "No results.",
                    }

            # Generate answer with query() + pre-retrieved context
            try:
                answer = await generate_answer(question_text, retrieval["context_text"])
            except Exception as e:
                print(f"  ERROR answer: {e}")
                await asyncio.sleep(10)
                try:
                    answer = await generate_answer(question_text, retrieval["context_text"])
                except Exception:
                    answer = f"[Error generating answer: {e}]"

            cites_source = source in answer

            entry = {
                "id": qid,
                "chunk_id": chunk_id,
                "chunk_title": title,
                "source_file": source,
                "persona": persona,
                "question": question_text,
                "expected_answerable": answerable,
                "agent_answer": answer,
                "retrieved_chunks": retrieval["retrieved_chunks"],
                "top_cosine_score": retrieval["top_cosine_score"],
                "top_reranker_score": retrieval["top_reranker_score"],
                "no_results": retrieval["no_results"],
                "answer_cites_source": cites_source,
            }

            dataset.append(entry)
            done_ids.add(qid)
            save_dataset(dataset)

            status = "✓" if not retrieval["no_results"] else "○"
            print(
                f"  Q {counter}/{total_expected}: {persona} "
                f"cos={retrieval['top_cosine_score']:.2f} "
                f"rer={retrieval['top_reranker_score']:.2f} "
                f"— saved {status}"
            )

            await asyncio.sleep(2)

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Total Q&A pairs: {len(dataset)}")

    persona_counts = {}
    for d in dataset:
        p = d["persona"]
        persona_counts[p] = persona_counts.get(p, 0) + 1
    print(f"\n  Per persona:")
    for p, c in sorted(persona_counts.items()):
        print(f"    {p:25s} {c}")

    answerable = [d for d in dataset if d["expected_answerable"]]
    good = [d for d in answerable if d["top_cosine_score"] >= 0.50]
    print(f"\n  Answerable with good retrieval (cosine ≥ 0.50): {len(good)}/{len(answerable)}")

    irrelevant = [d for d in dataset if not d["expected_answerable"]]
    low = [d for d in irrelevant if d["no_results"] or d["top_reranker_score"] < 0.30]
    print(f"  Irrelevant with low/no results: {len(low)}/{len(irrelevant)}")

    cited = [d for d in answerable if d["answer_cites_source"]]
    print(f"  Answerable with source citation: {len(cited)}/{len(answerable)}")

    summary = {
        "total_questions": len(dataset),
        "questions_per_persona": persona_counts,
        "answerable_good_retrieval": f"{len(good)}/{len(answerable)}",
        "irrelevant_low_results": f"{len(low)}/{len(irrelevant)}",
        "citation_rate": f"{len(cited)}/{len(answerable)}",
    }
    summary_path = DATASET_PATH.replace("qa_dataset.json", "qa_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\n  Summary: {summary_path}")
    print(f"  Dataset: {DATASET_PATH}")


if __name__ == "__main__":
    asyncio.run(main())
