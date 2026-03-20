CREATE EXTENSION IF NOT EXISTS vector;

-- Documentation chunks with embeddings
CREATE TABLE chunks (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    section TEXT,
    subsection TEXT,
    content TEXT NOT NULL,
    page_range TEXT,
    tags TEXT[],
    source_file TEXT,
    word_count INTEGER,
    embedding vector(2560),
    doc_url TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
CREATE INDEX ON chunks USING hnsw (embedding vector_cosine_ops);

-- Chat sessions
CREATE TABLE IF NOT EXISTS chat_sessions (
    id TEXT PRIMARY KEY,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    message_count INTEGER DEFAULT 0
);

-- Chat messages
CREATE TABLE IF NOT EXISTS chat_messages (
    id SERIAL PRIMARY KEY,
    session_id TEXT REFERENCES chat_sessions(id) ON DELETE CASCADE,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    sources JSONB DEFAULT '[]',
    created_at TIMESTAMP DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_chat_messages_session ON chat_messages(session_id);

-- Q&A dataset pairs
CREATE TABLE IF NOT EXISTS qa_pairs (
    id TEXT PRIMARY KEY,
    chunk_id INTEGER,
    source_file TEXT,
    section TEXT,
    question TEXT NOT NULL,
    ideal_answer TEXT NOT NULL,
    type TEXT,
    difficulty TEXT,
    quality_score INTEGER,
    cosine_score REAL,
    reranker_score REAL,
    correct_source_in_top1 BOOLEAN,
    correct_source_in_top3 BOOLEAN,
    verified BOOLEAN DEFAULT FALSE,
    embedding vector(2560),
    doc_url TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_qa_pairs_embedding ON qa_pairs USING ivfflat (embedding vector_cosine_ops) WITH (lists = 20);

-- Q&A evaluation results
CREATE TABLE IF NOT EXISTS qa_evaluations (
    id SERIAL PRIMARY KEY,
    qa_id TEXT,
    rag_answer TEXT,
    rag_sources JSONB DEFAULT '[]',
    cosine_score REAL,
    reranker_score REAL,
    correct_source_top1 BOOLEAN,
    correct_source_top3 BOOLEAN,
    eval_correctness INTEGER,
    eval_completeness INTEGER,
    eval_relevance INTEGER,
    eval_hallucination INTEGER,
    eval_overall INTEGER,
    eval_issues TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
