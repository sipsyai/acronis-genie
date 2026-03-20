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

## Code Review Graph

Bu projede `code-review-graph` plugin'i aktif. Aşağıdaki durumlarda kullan:

- **Refactor/büyük değişiklik öncesi:** `get_impact_radius` ile etki analizi yap — değişeceğin fonksiyonu kimin çağırdığını, nereleri etkileyeceğini gör.
- **Commit sonrası:** `review-delta` ile blast-radius analizi çalıştır — kırılma riski olan yerleri tespit et.
- **PR review:** `review-pr` ile yapısal bağlam içinde review yap.

**Kullanma:** Basit dosya arama, explore, grep işleri için — bunlar zaten Glob/Grep/Read ile daha hızlı.
