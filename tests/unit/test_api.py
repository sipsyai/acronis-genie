"""
Tests for agent/api.py — FastAPI endpoints, prompt building, source extraction, doc reading.

These tests mock external dependencies (DB, embedding service, Claude SDK)
and focus on testing the pure logic and HTTP layer.
"""

import json
import pytest
from pathlib import Path
from unittest.mock import AsyncMock, patch, MagicMock

# We need to mock heavy imports before importing the module
import sys
import types

# Create mock for claude_code_sdk before importing api
mock_sdk = types.ModuleType("claude_code_sdk")
mock_sdk.ClaudeSDKClient = MagicMock
mock_sdk.ClaudeCodeOptions = MagicMock
mock_sdk.AssistantMessage = type("AssistantMessage", (), {})
mock_sdk.ResultMessage = type("ResultMessage", (), {})
mock_sdk.TextBlock = type("TextBlock", (), {})
mock_sdk.tool = lambda *a, **kw: (lambda f: f)
mock_sdk.create_sdk_mcp_server = MagicMock(return_value=MagicMock())

mock_internal = types.ModuleType("claude_code_sdk._internal")
mock_mp = types.ModuleType("claude_code_sdk._internal.message_parser")
mock_mp.parse_message = lambda data: data
mock_mp.MessageParseError = Exception

sys.modules.setdefault("claude_code_sdk", mock_sdk)
sys.modules.setdefault("claude_code_sdk._internal", mock_internal)
sys.modules.setdefault("claude_code_sdk._internal.message_parser", mock_mp)

from agent.api import (
    _build_context_prompt,
    _build_rag_prompt,
    _extract_sources,
    _make_source_title,
    _step_event,
    _read_doc,
    ChatRequest,
    SourceInfo,
    app,
)

# Use httpx for testing FastAPI
from httpx import AsyncClient, ASGITransport


# ── Pure function tests ────────────────────────────────────


class TestBuildContextPrompt:
    def test_no_history(self):
        result = _build_context_prompt([], "How to set up 2FA?")
        assert result == "How to set up 2FA?"

    def test_with_history(self):
        history = [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"},
        ]
        result = _build_context_prompt(history, "How to set up 2FA?")
        assert "User: Hello" in result
        assert "Assistant: Hi there!" in result
        assert "User: How to set up 2FA?" in result
        assert "conversation history" in result.lower()

    def test_preserves_message_order(self):
        history = [
            {"role": "user", "content": "First"},
            {"role": "assistant", "content": "Second"},
            {"role": "user", "content": "Third"},
        ]
        result = _build_context_prompt(history, "Fourth")
        first_pos = result.index("First")
        second_pos = result.index("Second")
        third_pos = result.index("Third")
        fourth_pos = result.index("Fourth")
        assert first_pos < second_pos < third_pos < fourth_pos


class TestBuildRagPrompt:
    def test_includes_chunks_and_question(self):
        chunks = [
            {"source_file": "ch01/doc.md", "title": "2FA Setup", "content": "Steps for 2FA setup."},
        ]
        result = _build_rag_prompt("How to set up 2FA?", [], chunks)
        assert "Steps for 2FA setup" in result
        assert "How to set up 2FA?" in result
        assert "ch01/doc.md" in result

    def test_includes_history_when_present(self):
        chunks = [{"source_file": "x.md", "title": "T", "content": "C"}]
        history = [{"role": "user", "content": "prev question"}]
        result = _build_rag_prompt("new question", history, chunks)
        assert "prev question" in result
        assert "new question" in result

    def test_no_history(self):
        chunks = [{"source_file": "x.md", "title": "T", "content": "C"}]
        result = _build_rag_prompt("question", [], chunks)
        assert "Recent conversation" not in result

    def test_multiple_chunks_separated(self):
        chunks = [
            {"source_file": "a.md", "title": "A", "content": "Content A"},
            {"source_file": "b.md", "title": "B", "content": "Content B"},
        ]
        result = _build_rag_prompt("q", [], chunks)
        assert "Content A" in result
        assert "Content B" in result
        assert "---" in result  # separator


class TestExtractSources:
    def test_backtick_file_paths(self):
        text = "Based on `02-installing-deploying-agents/10-gui.md` and `06-backup-and-recovery/01-backup.md`."
        sources = _extract_sources(text)
        assert len(sources) == 2
        assert sources[0].file == "02-installing-deploying-agents/10-gui.md"
        assert sources[1].file == "06-backup-and-recovery/01-backup.md"

    def test_source_colon_pattern(self):
        text = "Some answer.\n**Source:** `03-plans/01-overview.md`"
        sources = _extract_sources(text)
        assert any(s.file == "03-plans/01-overview.md" for s in sources)

    def test_no_duplicates(self):
        text = "See `01-getting-started/01-setup.md` and `01-getting-started/01-setup.md`."
        sources = _extract_sources(text)
        assert len(sources) == 1

    def test_no_sources_found(self):
        text = "I don't have documentation about that topic."
        sources = _extract_sources(text)
        assert sources == []

    def test_title_formatting(self):
        text = "See `02-agents/05-linux-install.md`."
        sources = _extract_sources(text)
        assert sources[0].title == "05 Linux Install"


class TestMakeSourceTitle:
    def test_with_path(self):
        assert _make_source_title("06-backup/01-overview.md") == "01 Overview"

    def test_without_slash(self):
        assert _make_source_title("standalone.md") == "standalone.md"

    def test_dashes_to_spaces(self):
        result = _make_source_title("ch01/my-long-document-name.md")
        assert "My Long Document Name" == result


class TestStepEvent:
    def test_basic_step(self):
        result = _step_event("embedding", "Searching...", "search", 150)
        assert result["event"] == "message"
        data = json.loads(result["data"])
        assert data["type"] == "step"
        assert data["step"] == "embedding"
        assert data["message"] == "Searching..."
        assert data["icon"] == "search"
        assert data["elapsed_ms"] == 150

    def test_with_data_and_details(self):
        result = _step_event("searching", "Found 5", "docs", 200,
                             data={"count": 5},
                             details={"candidates": 5})
        data = json.loads(result["data"])
        assert data["data"]["count"] == 5
        assert data["details"]["candidates"] == 5


class TestReadDoc:
    def test_reads_valid_doc(self):
        fixture = Path(__file__).resolve().parent.parent / "fixtures" / "sample_chunks" / "valid_chunk.md"
        # Clear cache to ensure fresh read
        _read_doc.cache_clear()
        result = _read_doc(str(fixture))
        assert result["title"] == "Two-Factor Authentication Setup"
        assert result["section"] == "Getting Started"
        assert "Setting Up Two-Factor Authentication" in result["content"]
        assert result["doc_url"] == "https://docs.acronis.com/2fa-setup"

    def test_reads_doc_without_frontmatter(self):
        fixture = Path(__file__).resolve().parent.parent / "fixtures" / "sample_chunks" / "no_frontmatter.md"
        _read_doc.cache_clear()
        result = _read_doc(str(fixture))
        # Without proper frontmatter, title should be empty, content should be the raw text
        assert result["title"] == ""

    def test_strips_frontmatter_from_content(self):
        fixture = Path(__file__).resolve().parent.parent / "fixtures" / "sample_chunks" / "valid_chunk.md"
        _read_doc.cache_clear()
        result = _read_doc(str(fixture))
        assert "page_range:" not in result["content"]
        assert "tags:" not in result["content"]


class TestChatRequest:
    def test_default_session_id(self):
        req = ChatRequest(message="hello")
        assert req.session_id is None

    def test_with_session_id(self):
        req = ChatRequest(message="hello", session_id="abc-123")
        assert req.session_id == "abc-123"

    def test_empty_message_allowed(self):
        req = ChatRequest(message="")
        assert req.message == ""


# ── Endpoint tests (with mocked DB) ───────────────────────


@pytest.fixture
def mock_pool():
    """Mock asyncpg connection pool."""
    pool = AsyncMock()
    conn = AsyncMock()
    pool.acquire.return_value.__aenter__ = AsyncMock(return_value=conn)
    pool.acquire.return_value.__aexit__ = AsyncMock(return_value=False)
    return pool, conn


@pytest.mark.asyncio
async def test_health_endpoint_returns_ok(mock_pool):
    pool, conn = mock_pool
    conn.fetchval = AsyncMock(return_value=42)

    with patch("agent.api.get_pool", return_value=pool), \
         patch("agent.api.httpx.AsyncClient") as mock_httpx:
        # Mock GPU health checks
        mock_client = AsyncMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_client.get = AsyncMock(return_value=mock_response)
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        mock_httpx.return_value = mock_client

        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            resp = await client.get("/api/health")

        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "ok"
        assert "chunks_count" in data
        assert "gpu_embedding" in data
        assert "gpu_reranker" in data


@pytest.mark.asyncio
async def test_doc_endpoint_path_traversal_blocked():
    """Path traversal attempts should return 400."""
    from starlette.testclient import TestClient

    # Use raw ASGI scope to bypass httpx URL normalization
    transport = ASGITransport(app=app)

    # Test with encoded traversal (httpx normalizes bare ".." in paths)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        resp = await client.get("/api/docs/..%2F..%2F..%2Fetc/passwd")
    # Should be blocked (400) or not found (404) — never 200
    assert resp.status_code in (400, 404)

    # Test that the code-level check works directly
    from agent.api import get_doc
    result = await get_doc("../../etc/passwd")
    assert result.status_code == 400


@pytest.mark.asyncio
async def test_doc_endpoint_nonexistent_file():
    """Request for non-existent doc should return 404."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        resp = await client.get("/api/docs/nonexistent/file.md")
    assert resp.status_code == 404
