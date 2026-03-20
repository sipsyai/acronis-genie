# Test Coverage Analysis

## Current State

The codebase has ~3,600 lines of Python across 19 files, but **zero unit tests**. The 4 existing "test" files in `scripts/` are integration/evaluation scripts that:

- Require live external services (PostgreSQL, GPU embedding server, reranker, FastAPI app)
- Produce JSON reports rather than pass/fail assertions
- Must be run manually — no pytest, no CI
- Have no mocking, fixtures, or isolation

## Coverage Map

| Module | Lines | Unit Tests | Integration Tests |
|---|---|---|---|
| `agent/api.py` | 857 | None | `test_chat_api.py` (partial) |
| `agent/tools.py` | 177 | None | `test_50_queries.py` (indirect) |
| `agent/main.py` | 144 | None | None |
| `agent/server.py` | 20 | None | None |
| `agent/sdk_patch.py` | 23 | None | None |
| `scripts/load_all_chunks.py` | 190 | None | None |
| `scripts/load_qa_pairs.py` | 80 | None | None |
| `scripts/generate_qa_v2.py` | 365 | None | None |
| `scripts/evaluate_qa.py` | 369 | None | None |

## Priority Recommendations

### 1. Set up pytest infrastructure (High Priority)

- Add `pytest`, `pytest-asyncio`, `pytest-httpx` to dev dependencies
- Create `tests/` directory with `conftest.py`
- Add a `pyproject.toml` or `pytest.ini` for configuration
- This unblocks everything else

### 2. Unit tests for `agent/api.py` (Highest Impact)

This is the largest file (857 lines) and the main entry point. Needs tests for:

- **`/api/health` endpoint** — verify response shape, DB connectivity check
- **`/api/chat/stream` SSE endpoint** — mock Claude client, verify event sequence (embedding → qa_match → searching → reranking → sources → generating → done)
- **Session management** — creation, retrieval, history endpoints
- **RAG pipeline functions** — embedding call, cosine search, reranking logic, score thresholds (0.80 for QA match, 0.40 for cosine, 0.20 for reranker)
- **Error handling** — DB connection failures, embedding service down, malformed requests
- **Input validation** — empty messages, very long messages, special characters

### 3. Unit tests for `agent/tools.py` (High Impact)

The `search_docs` MCP tool contains core RAG logic:

- QA pair matching with similarity threshold
- Chunk search + reranking pipeline
- Result formatting and source attribution
- Edge cases: no results found, all results below threshold, embedding service errors

### 4. Unit tests for `agent/sdk_patch.py` (Quick Win)

Small file, easy to test:

- Verify monkey-patch correctly handles `rate_limit_event`
- Verify known message types still work
- Verify other unknown types are handled gracefully

### 5. Unit tests for `scripts/load_all_chunks.py` (Medium Priority)

- `parse_chunk()` — YAML frontmatter parsing, edge cases (missing fields, malformed YAML)
- Chunk text extraction
- Batch embedding logic
- Idempotency (skip already-loaded chunks)

### 6. Convert existing integration scripts to pytest (Medium Priority)

- Wrap `test_chat_api.py` scenarios as proper pytest test cases with assertions
- Make `test_50_queries.py` a parametrized pytest suite with pass/fail thresholds
- Add `@pytest.mark.integration` markers so they can be excluded in fast CI runs

### 7. Add tests for `agent/main.py` CLI (Lower Priority)

- Test `ask()` function with mocked ClaudeSDKClient
- Test `run_tests()` behavior
- Test argument parsing

## Specific Gaps That Carry Risk

| Gap | Risk |
|---|---|
| No test for SSE streaming format | Breaking the frontend silently |
| No test for score thresholds (0.80, 0.40, 0.20) | RAG quality regression |
| No test for session/history DB operations | Data loss or corruption |
| No test for rejection of irrelevant queries | Hallucination leaks to users |
| No test for `sdk_patch.py` | Claude SDK upgrades breaking silently |
| No test for frontmatter parsing | Silent data ingestion failures |

## Suggested Test Structure

```
tests/
├── conftest.py              # Shared fixtures (mock DB, mock embedding service)
├── unit/
│   ├── test_api_endpoints.py
│   ├── test_api_rag_pipeline.py
│   ├── test_tools_search.py
│   ├── test_sdk_patch.py
│   └── test_chunk_parser.py
├── integration/
│   ├── test_chat_quality.py   # From test_chat_api.py
│   └── test_search_quality.py # From test_50_queries.py
└── fixtures/
    ├── sample_chunks/         # Small markdown files for testing
    └── mock_responses.py      # Canned embedding/reranker responses
```
