"""
MCP server: acronis_kb — exposes search_docs tool to the Claude agent.
"""

from claude_code_sdk import create_sdk_mcp_server
from agent.tools import search_docs

_server = create_sdk_mcp_server(
    name="acronis_kb",
    tools=[search_docs],
)


def get_server():
    return _server


def get_tool_names() -> list[str]:
    return ["mcp__acronis_kb__search_docs"]
