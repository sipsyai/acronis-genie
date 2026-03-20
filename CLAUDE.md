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
