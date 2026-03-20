"""
Tests for scripts/load_all_chunks.py — parse_chunk() function.
"""

import pytest
from pathlib import Path

# Import parse_chunk directly
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "scripts"))
from load_all_chunks import parse_chunk

FIXTURES_DIR = Path(__file__).resolve().parent.parent / "fixtures" / "sample_chunks"


class TestParseChunk:
    def test_valid_chunk_all_fields(self):
        """Full frontmatter with all fields should be parsed correctly."""
        result = parse_chunk(FIXTURES_DIR / "valid_chunk.md", "01-getting-started")

        assert result["title"] == "Two-Factor Authentication Setup"
        assert result["section"] == "Getting Started"
        assert result["subsection"] == "Security"
        assert result["page_range"] == "15-17"
        assert result["tags"] == ["security", "2fa", "authentication"]
        assert result["source_file"] == "01-getting-started/valid_chunk.md"
        assert result["doc_url"] == "https://docs.acronis.com/2fa-setup"
        assert "Setting Up Two-Factor Authentication" in result["content"]
        assert result["word_count"] > 0

    def test_minimal_frontmatter(self):
        """Only title in frontmatter — optional fields should be None/empty."""
        result = parse_chunk(FIXTURES_DIR / "minimal_frontmatter.md", "01-getting-started")

        assert result["title"] == "Minimal Doc"
        assert result["section"] is None
        assert result["subsection"] is None
        assert result["tags"] == []
        assert result["source_file"] == "01-getting-started/minimal_frontmatter.md"
        assert "Some content" in result["content"]

    def test_no_frontmatter_raises(self):
        """File without YAML frontmatter should raise ValueError."""
        with pytest.raises(ValueError, match="No frontmatter"):
            parse_chunk(FIXTURES_DIR / "no_frontmatter.md", "01-getting-started")

    def test_source_file_includes_chapter_dir(self):
        """source_file should be chapter_dir/filename."""
        result = parse_chunk(FIXTURES_DIR / "valid_chunk.md", "06-backup-and-recovery")
        assert result["source_file"] == "06-backup-and-recovery/valid_chunk.md"

    def test_word_count_is_accurate(self):
        """word_count should match actual word count of content."""
        result = parse_chunk(FIXTURES_DIR / "valid_chunk.md", "01-getting-started")
        actual_words = len(result["content"].split())
        assert result["word_count"] == actual_words

    def test_content_excludes_frontmatter(self):
        """Content should not contain the YAML frontmatter block."""
        result = parse_chunk(FIXTURES_DIR / "valid_chunk.md", "01-getting-started")
        assert "---" not in result["content"]
        assert "page_range:" not in result["content"]
