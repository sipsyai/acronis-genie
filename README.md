# Acronis Genie

AI-powered assistant for Acronis Cyber Protect Cloud, built with RAG (Retrieval-Augmented Generation).

## Overview

This project provides an intelligent Q&A system over the Acronis Cyber Protect Cloud documentation. It uses chunked markdown files optimized for RAG pipelines to deliver accurate, context-aware answers.

## Project Structure

```
acronis-genie/
├── cyber-protect-cloud-docs/   # RAG-ready markdown chunks (by chapter)
├── data/                       # QA datasets, evaluation results
├── .gitignore
└── README.md
```

## Documentation Source

The knowledge base is derived from the official Acronis Cyber Protect Cloud User Guide:

- **Download:** [Acronis Cyber Protect Cloud User Guide (PDF)](https://www.acronis.com/download/docs/cpc/userguide/)
- **Version:** 26.02
- **Pages:** 1,542

## Data

- `data/qa_dataset_v2.json` — QA dataset for evaluation
- `data/qa_evaluation.json` — Evaluation results
- `data/verified_qa_pairs.json` — Verified QA pairs

## License

Private repository — internal use only.
