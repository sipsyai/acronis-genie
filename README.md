# Acronis Genie

AI-powered assistant for Acronis Cyber Protect Cloud, built with RAG (Retrieval-Augmented Generation).

## Overview

This project provides an intelligent Q&A system over the Acronis Cyber Protect Cloud documentation. It uses chunked markdown files optimized for RAG pipelines to deliver accurate, context-aware answers with a streaming chat UI.

## Architecture

- **Embedding:** Qwen3-Embedding-4B (GPU, port 8011)
- **Reranking:** BGE-Reranker-v2-M3 (GPU, port 8012)
- **Database:** PostgreSQL 16 + pgvector (cosine similarity search)
- **LLM:** Claude via claude-code-sdk
- **Frontend:** Single-page chat UI with real-time SSE streaming and RAG pipeline visualization

## Project Structure

```
acronis-genie/
├── agent/                  # FastAPI app + Claude SDK integration
│   ├── api.py              # REST + SSE streaming endpoints
│   ├── main.py             # Interactive CLI agent
│   ├── server.py           # MCP server (search_docs tool)
│   ├── tools.py            # RAG search tool (embedding + reranking)
│   ├── sdk_patch.py        # SDK message parser patch
│   └── static/index.html   # Chat UI
├── scripts/                # Data loading & evaluation scripts
│   ├── load_all_chunks.py  # Load markdown chunks into pgvector
│   ├── evaluate_qa.py      # QA evaluation pipeline
│   └── ...
├── db/
│   └── schema.sql          # PostgreSQL schema (chunks, qa_pairs, chat)
├── docs/                   # RAG-ready markdown chunks (by chapter)
├── data/                   # QA datasets, evaluation results
├── docker-compose.yml      # PostgreSQL + pgvector
├── requirements.txt        # Python dependencies
├── CLAUDE.md               # Claude Code SDK usage rules
└── README.md
```

## Setup

```bash
# 1. Start PostgreSQL with pgvector
docker-compose up -d

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Load documentation chunks (requires GPU server running)
python scripts/load_all_chunks.py

# 5. Start the web UI
uvicorn agent.api:app --host 0.0.0.0 --port 8080
```

Open http://localhost:8080 to use the chat interface.

## Documentation Source

The knowledge base is derived from the official Acronis Cyber Protect Cloud User Guide:

- **Version:** 26.02
- **Pages:** 1,542

## Data

- `data/qa_dataset_v2.json` — QA dataset for evaluation
- `data/qa_evaluation.json` — Evaluation results
- `data/verified_qa_pairs.json` — Verified QA pairs

## License

Private repository — internal use only.
