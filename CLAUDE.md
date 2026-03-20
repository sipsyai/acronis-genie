# Acronis Agent — Development Rules

## SDK Usage — CRITICAL

**Always use `ClaudeSDKClient`** (async context manager), never `query()`.

```python
# CORRECT
async with ClaudeSDKClient(options=options) as client:
    await client.query("prompt")
    async for msg in client.receive_response():
        ...

# WRONG — do NOT use
async for msg in query(prompt="...", options=options):
    ...
```

**Why:** `query()` has transport timing issues with SDK MCP servers. `ClaudeSDKClient` manages lifecycle properly.

**Always handle `rate_limit_event`:**
```python
try:
    async for msg in client.receive_response():
        ...
except Exception as e:
    if "Unknown message type" not in str(e):
        raise
```

## Language Policy

**All code, comments, prompts, documentation, commit messages, and technical writing in this project MUST be in English.** No Turkish in any project files — the entire codebase is English-only.

## Code Review Graph

The `code-review-graph` plugin is active. Use it for:

- **Before refactors/large changes:** `get_impact_radius` to analyze blast radius — see who calls the function you're changing.
- **After commits:** `review-delta` to detect breaking risk.
- **PR review:** `review-pr` for structural context.

**Don't use for:** Simple file search, explore, grep — Glob/Grep/Read are faster for those.
