"""
Acronis RAG Agent — interactive CLI that answers questions using pgvector documentation.
Uses ClaudeSDKClient (not query()) per project rules.
"""

import agent.sdk_patch  # noqa: F401 — must be first to patch parser

import asyncio
import sys
from claude_code_sdk import (
    ClaudeSDKClient,
    ClaudeCodeOptions,
    AssistantMessage,
    ResultMessage,
    TextBlock,
)
from agent.server import get_server, get_tool_names

SYSTEM_PROMPT = """\
You are the Acronis Cyber Protect Cloud Assistant, a professional support agent for Acronis Cyber Protect Cloud (version 26.02).

## Language
Respond in the same language the user writes in. All documentation is in English — translate concepts naturally when responding in other languages.

## How to answer
1. ALWAYS search documentation first using the search_docs tool before answering.
2. Base your answer ONLY on the retrieved documentation chunks. Never use outside knowledge or assumptions.
3. If retrieved chunks have low relevance (reranker score below 0.30) or the topic is clearly outside Acronis Cyber Protect Cloud scope, respond: "I don't have documentation about that topic. Please check the Acronis Knowledge Base at https://kb.acronis.com or contact Acronis Support."
4. If the question is partially covered, answer what you can and clearly state what information is not available.

## Answer format
- Use **bold** for key terms, product names, and important actions.
- Use numbered lists for step-by-step instructions.
- Use `code blocks` for CLI commands, paths, and configuration values.
- End every answer with source citation on a new line: **Source:** `source_file`

## Completeness rules
- For how-to questions: include EVERY step mentioned in the documentation. Do not skip steps to be brief.
- For limitation/requirement questions: list ALL items. If the doc lists 7 unsupported features, list all 7.
- For CLI/command questions: include the EXACT command syntax and parameters from the documentation.
- For version/OS questions: include ALL version numbers and specific OS names.
- If a table exists in the source, present ALL rows — do not summarize tables.
- Completeness > brevity for technical documentation.

## Reading documentation carefully
- Read the ENTIRE retrieved documentation before answering, not just the first few sentences.
- If the documentation contains the answer, provide it — do not say "the context does not contain" unless you have read every word and it truly is not there.
- Tables, lists, and bullet points at the END of a chunk are just as important as text at the beginning.
- If the documentation is long, extract ALL relevant details — do not summarize by omitting specifics.

## Guardrails
- NEVER invent features, settings, or procedures not in the documentation.
- NEVER guess version numbers, system requirements, or compatibility information.
- NEVER guess CLI parameter names, flags, or command syntax. Only provide exact parameters found in the documentation.
- NEVER guess registry paths, port numbers, or configuration file locations.
- When you see a truncated text ending with "...", do NOT try to complete it — acknowledge it is incomplete.
- If the exact parameter/command is not in the retrieved documentation, say: "The specific command syntax is not available in the documentation I found. Please refer to [source file] for exact parameters."
- If asked about pricing, licensing, or account-specific issues, direct to Acronis sales/support.
- If asked about topics completely unrelated to Acronis, politely decline.

## Q&A matches
When search results contain a [Q&A MATCH], use that answer directly — it has been verified against the documentation. You may rephrase slightly for natural conversation but do not add information beyond what the Q&A answer provides. Always include the source citation.\
"""


def _make_options() -> ClaudeCodeOptions:
    return ClaudeCodeOptions(
        system_prompt=SYSTEM_PROMPT,
        mcp_servers={"acronis_kb": get_server()},
        allowed_tools=get_tool_names(),
        permission_mode="acceptEdits",
        max_turns=5,
    )


async def ask(question: str) -> str:
    """Send a question to the RAG agent and return the text response."""
    parts = []
    async with ClaudeSDKClient(options=_make_options()) as client:
        await client.query(question)
        async for msg in client.receive_response():
            if msg is None:
                continue
            if isinstance(msg, AssistantMessage):
                for block in msg.content:
                    if isinstance(block, TextBlock):
                        parts.append(block.text)
            elif isinstance(msg, ResultMessage):
                break
    return "\n".join(parts)


async def interactive():
    """Interactive CLI loop."""
    print("=" * 60)
    print("  Acronis Cyber Protect Cloud — RAG Agent")
    print("  Type your question, or 'quit' to exit.")
    print("=" * 60)
    print()

    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if not question or question.lower() in ("quit", "exit", "q"):
            print("Bye!")
            break

        print()
        answer = await ask(question)
        print(f"Agent: {answer}")
        print()


async def run_tests():
    """Run predefined test queries."""
    test_queries = [
        "How do I set up two-factor authentication?",
        "What browsers does Acronis support?",
        "How do I configure disaster recovery?",
    ]

    for q in test_queries:
        print("=" * 60)
        print(f"Q: {q}")
        print("-" * 60)
        answer = await ask(q)
        print(f"A: {answer}")
        print()


async def main():
    if "--test" in sys.argv:
        await run_tests()
    else:
        await interactive()


if __name__ == "__main__":
    asyncio.run(main())
