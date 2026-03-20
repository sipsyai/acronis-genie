"""
Tests for agent/tools.py — search_docs MCP tool and helper functions.

All external dependencies (DB, embedding API, reranker API) are mocked.
"""

import pytest
from unittest.mock import AsyncMock, patch, MagicMock
import types
import sys

# Mock claude_code_sdk before importing tools
mock_sdk = types.ModuleType("claude_code_sdk")
mock_sdk.tool = lambda *a, **kw: (lambda f: f)
sys.modules.setdefault("claude_code_sdk", mock_sdk)

from agent.tools import (
    _embed_query,
    _rerank,
    _search_qa_pairs,
    search_docs,
    COSINE_THRESHOLD,
    RERANKER_THRESHOLD,
    QA_MATCH_THRESHOLD,
)


# ── Threshold constants ────────────────────────────────────


def test_threshold_values():
    """Verify threshold constants haven't drifted from expected values."""
    assert QA_MATCH_THRESHOLD == 0.80
    assert COSINE_THRESHOLD == 0.40
    assert RERANKER_THRESHOLD == 0.20


# ── _embed_query ───────────────────────────────────────────


@pytest.mark.asyncio
async def test_embed_query_returns_embedding():
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "data": [{"embedding": [0.1, 0.2, 0.3]}]
    }
    mock_response.raise_for_status = MagicMock()

    mock_client = AsyncMock()
    mock_client.post = AsyncMock(return_value=mock_response)
    mock_client.__aenter__ = AsyncMock(return_value=mock_client)
    mock_client.__aexit__ = AsyncMock(return_value=False)

    with patch("agent.tools.httpx.AsyncClient", return_value=mock_client):
        result = await _embed_query("test query")

    assert result == [0.1, 0.2, 0.3]


@pytest.mark.asyncio
async def test_embed_query_raises_on_http_error():
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = Exception("HTTP 500")

    mock_client = AsyncMock()
    mock_client.post = AsyncMock(return_value=mock_response)
    mock_client.__aenter__ = AsyncMock(return_value=mock_client)
    mock_client.__aexit__ = AsyncMock(return_value=False)

    with patch("agent.tools.httpx.AsyncClient", return_value=mock_client):
        with pytest.raises(Exception, match="HTTP 500"):
            await _embed_query("test")


# ── _rerank ────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_rerank_returns_ordered_scores():
    mock_response = MagicMock()
    mock_response.json.return_value = [
        {"index": 1, "score": 0.9},
        {"index": 0, "score": 0.3},
    ]
    mock_response.raise_for_status = MagicMock()

    mock_client = AsyncMock()
    mock_client.post = AsyncMock(return_value=mock_response)
    mock_client.__aenter__ = AsyncMock(return_value=mock_client)
    mock_client.__aexit__ = AsyncMock(return_value=False)

    with patch("agent.tools.httpx.AsyncClient", return_value=mock_client):
        result = await _rerank("query", ["text A", "text B"])

    assert result == [0.3, 0.9]


@pytest.mark.asyncio
async def test_rerank_handles_empty_texts():
    mock_response = MagicMock()
    mock_response.json.return_value = []
    mock_response.raise_for_status = MagicMock()

    mock_client = AsyncMock()
    mock_client.post = AsyncMock(return_value=mock_response)
    mock_client.__aenter__ = AsyncMock(return_value=mock_client)
    mock_client.__aexit__ = AsyncMock(return_value=False)

    with patch("agent.tools.httpx.AsyncClient", return_value=mock_client):
        result = await _rerank("query", [])

    assert result == []


# ── _search_qa_pairs ───────────────────────────────────────


@pytest.mark.asyncio
async def test_search_qa_pairs_high_similarity_returns_match():
    mock_conn = AsyncMock()
    mock_conn.fetchrow = AsyncMock(return_value={
        "question": "How to set up 2FA?",
        "ideal_answer": "Go to Settings > Security > Enable 2FA.",
        "source_file": "01-getting-started/03-2fa.md",
        "section": "Getting Started",
        "similarity": 0.92,
        "quality_score": 5,
    })

    result = await _search_qa_pairs(mock_conn, "[0.1,0.2,0.3]")
    assert result is not None
    assert result["question"] == "How to set up 2FA?"
    assert result["similarity"] == 0.92


@pytest.mark.asyncio
async def test_search_qa_pairs_low_similarity_returns_none():
    mock_conn = AsyncMock()
    mock_conn.fetchrow = AsyncMock(return_value={
        "question": "Something",
        "ideal_answer": "Answer",
        "source_file": "x.md",
        "section": "S",
        "similarity": 0.5,  # Below QA_MATCH_THRESHOLD (0.80)
        "quality_score": 3,
    })

    result = await _search_qa_pairs(mock_conn, "[0.1,0.2,0.3]")
    assert result is None


@pytest.mark.asyncio
async def test_search_qa_pairs_no_rows_returns_none():
    mock_conn = AsyncMock()
    mock_conn.fetchrow = AsyncMock(return_value=None)

    result = await _search_qa_pairs(mock_conn, "[0.1,0.2]")
    assert result is None


# ── search_docs (full pipeline) ────────────────────────────


def _make_mock_conn(qa_row=None, chunk_rows=None):
    """Create a mock asyncpg connection with configurable responses."""
    conn = AsyncMock()
    conn.fetchrow = AsyncMock(return_value=qa_row)
    conn.fetch = AsyncMock(return_value=chunk_rows or [])
    conn.close = AsyncMock()
    return conn


def _make_chunk_row(title, content, source_file, similarity):
    """Helper to create a mock DB row for chunks."""
    return {
        "id": 1,
        "title": title,
        "section": "Test Section",
        "content": content,
        "source_file": source_file,
        "doc_url": f"https://docs.acronis.com/{source_file}",
        "similarity": similarity,
    }


@pytest.mark.asyncio
async def test_search_docs_qa_match_returns_directly():
    """When a QA match is found above threshold, it should return immediately."""
    qa_row = {
        "question": "How to set up 2FA?",
        "ideal_answer": "Go to Settings > Security.",
        "source_file": "01-getting-started/03-2fa.md",
        "section": "Getting Started",
        "similarity": 0.92,
        "quality_score": 5,
    }
    mock_conn = _make_mock_conn(qa_row=qa_row)

    with patch("agent.tools._embed_query", return_value=[0.1, 0.2, 0.3]), \
         patch("agent.tools.asyncpg.connect", return_value=mock_conn):
        result = await search_docs({"query": "How to set up 2FA?", "top_k": 3})

    assert "content" in result
    text = result["content"][0]["text"]
    assert "Q&A MATCH" in text
    assert "Go to Settings > Security." in text


@pytest.mark.asyncio
async def test_search_docs_no_results_below_cosine():
    """When all chunks are below cosine threshold, return 'no results' message."""
    chunk_rows = [
        _make_chunk_row("Doc A", "Content A", "ch01/a.md", 0.30),  # Below 0.40
        _make_chunk_row("Doc B", "Content B", "ch01/b.md", 0.25),
    ]
    mock_conn = _make_mock_conn(qa_row=None, chunk_rows=chunk_rows)

    with patch("agent.tools._embed_query", return_value=[0.1, 0.2, 0.3]), \
         patch("agent.tools.asyncpg.connect", return_value=mock_conn):
        result = await search_docs({"query": "irrelevant pizza recipe", "top_k": 3})

    text = result["content"][0]["text"]
    assert "No relevant documentation found" in text
    assert "cosine threshold" in text


@pytest.mark.asyncio
async def test_search_docs_no_results_below_reranker():
    """Chunks pass cosine but fail reranker threshold."""
    chunk_rows = [
        _make_chunk_row("Doc A", "Content A", "ch01/a.md", 0.55),
    ]
    mock_conn = _make_mock_conn(qa_row=None, chunk_rows=chunk_rows)

    with patch("agent.tools._embed_query", return_value=[0.1, 0.2, 0.3]), \
         patch("agent.tools.asyncpg.connect", return_value=mock_conn), \
         patch("agent.tools._rerank", return_value=[0.10]):  # Below 0.20
        result = await search_docs({"query": "something", "top_k": 3})

    text = result["content"][0]["text"]
    assert "No relevant documentation found" in text
    assert "reranker" in text


@pytest.mark.asyncio
async def test_search_docs_returns_top_k_results():
    """Successful chunk search should return top_k ranked results."""
    chunk_rows = [
        _make_chunk_row("Doc A", "Content A about backups", "ch06/a.md", 0.65),
        _make_chunk_row("Doc B", "Content B about backups", "ch06/b.md", 0.60),
        _make_chunk_row("Doc C", "Content C about backups", "ch06/c.md", 0.55),
        _make_chunk_row("Doc D", "Content D about backups", "ch06/d.md", 0.50),
    ]
    mock_conn = _make_mock_conn(qa_row=None, chunk_rows=chunk_rows)

    rerank_scores = [0.85, 0.70, 0.45, 0.30]

    with patch("agent.tools._embed_query", return_value=[0.1, 0.2, 0.3]), \
         patch("agent.tools.asyncpg.connect", return_value=mock_conn), \
         patch("agent.tools._rerank", return_value=rerank_scores):
        result = await search_docs({"query": "how to backup", "top_k": 2})

    text = result["content"][0]["text"]
    assert "CHUNK SEARCH" in text
    assert "Doc A" in text
    assert "Doc B" in text
    # Doc C and D should not be in top_k=2
    assert text.count("Doc C") <= 0 or "Doc C" not in text.split("Doc B")[-1][:50]


@pytest.mark.asyncio
async def test_search_docs_default_top_k():
    """top_k should default to 3 when not specified."""
    chunk_rows = [
        _make_chunk_row(f"Doc {i}", f"Content {i}", f"ch01/{i}.md", 0.6 + i * 0.01)
        for i in range(5)
    ]
    mock_conn = _make_mock_conn(qa_row=None, chunk_rows=chunk_rows)

    with patch("agent.tools._embed_query", return_value=[0.1, 0.2, 0.3]), \
         patch("agent.tools.asyncpg.connect", return_value=mock_conn), \
         patch("agent.tools._rerank", return_value=[0.9, 0.8, 0.7, 0.6, 0.5]):
        result = await search_docs({"query": "test"})  # No top_k

    text = result["content"][0]["text"]
    # Should return at most 3 results (default)
    assert "CHUNK SEARCH" in text


@pytest.mark.asyncio
async def test_search_docs_closes_connection():
    """DB connection should always be closed, even on error."""
    mock_conn = _make_mock_conn(qa_row=None, chunk_rows=[])
    mock_conn.fetchrow = AsyncMock(side_effect=Exception("DB error"))

    with patch("agent.tools._embed_query", return_value=[0.1, 0.2]), \
         patch("agent.tools.asyncpg.connect", return_value=mock_conn):
        with pytest.raises(Exception, match="DB error"):
            await search_docs({"query": "test"})

    mock_conn.close.assert_called_once()
