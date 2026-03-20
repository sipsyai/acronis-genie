"""
Monkey-patch the Claude Code SDK message parser to skip unknown message types
(e.g. rate_limit_event) instead of raising MessageParseError.

Import this module before using the SDK.
"""

import claude_code_sdk._internal.message_parser as _mp

_original_parse = _mp.parse_message


def _patched_parse(data):
    try:
        return _original_parse(data)
    except _mp.MessageParseError as e:
        if "Unknown message type" in str(e):
            return None  # Skip unknown types
        raise


_mp.parse_message = _patched_parse
