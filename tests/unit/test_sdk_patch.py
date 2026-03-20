"""
Tests for agent/sdk_patch.py — monkey-patch that skips unknown SDK message types.
"""

import importlib
import types
import pytest


class FakeMessageParseError(Exception):
    pass


def _make_fake_module(original_fn):
    """Create a fake message_parser module with a controllable parse_message."""
    mod = types.ModuleType("claude_code_sdk._internal.message_parser")
    mod.parse_message = original_fn
    mod.MessageParseError = FakeMessageParseError
    return mod


def test_patched_parse_passes_through_normal_messages():
    """Known message types should be returned unchanged."""
    def original(data):
        return {"type": "assistant", "content": "hello"}

    import sys
    fake_mod = _make_fake_module(original)
    sys.modules["claude_code_sdk._internal.message_parser"] = fake_mod

    # Re-import to apply patch
    import agent.sdk_patch as sp
    importlib.reload(sp)

    result = fake_mod.parse_message({"type": "assistant"})
    assert result == {"type": "assistant", "content": "hello"}

    # Cleanup
    del sys.modules["claude_code_sdk._internal.message_parser"]


def test_patched_parse_returns_none_for_unknown_message_type():
    """Unknown message types (like rate_limit_event) should return None, not raise."""
    def original(data):
        raise FakeMessageParseError("Unknown message type: rate_limit_event")

    import sys
    fake_mod = _make_fake_module(original)
    sys.modules["claude_code_sdk._internal.message_parser"] = fake_mod

    import agent.sdk_patch as sp
    importlib.reload(sp)

    result = fake_mod.parse_message({"type": "rate_limit_event"})
    assert result is None

    del sys.modules["claude_code_sdk._internal.message_parser"]


def test_patched_parse_reraises_non_unknown_errors():
    """MessageParseError that isn't about unknown types should still be raised."""
    def original(data):
        raise FakeMessageParseError("Malformed JSON payload")

    import sys
    fake_mod = _make_fake_module(original)
    sys.modules["claude_code_sdk._internal.message_parser"] = fake_mod

    import agent.sdk_patch as sp
    importlib.reload(sp)

    with pytest.raises(FakeMessageParseError, match="Malformed JSON"):
        fake_mod.parse_message({"bad": "data"})

    del sys.modules["claude_code_sdk._internal.message_parser"]
