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
-- Note: pgvector HNSW/IVFFlat indexes max 2000 dims; Qwen3 uses 2560. Exact scan is used.

-- FTS support for chunks
ALTER TABLE chunks ADD COLUMN IF NOT EXISTS fts tsvector;
CREATE INDEX IF NOT EXISTS idx_chunks_fts ON chunks USING gin (fts);
CREATE OR REPLACE FUNCTION chunks_fts_update() RETURNS trigger AS $$
BEGIN
    NEW.fts := to_tsvector('english', COALESCE(NEW.content, ''));
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
DROP TRIGGER IF EXISTS chunks_fts_trigger ON chunks;
CREATE TRIGGER chunks_fts_trigger BEFORE INSERT OR UPDATE ON chunks
FOR EACH ROW EXECUTE FUNCTION chunks_fts_update();

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

-- Scraped web doc chunks with embeddings
CREATE TABLE IF NOT EXISTS web_chunks (
    id SERIAL PRIMARY KEY,
    page_slug TEXT NOT NULL,           -- "about-cyber-disaster-recovery-cloud.html"
    page_title TEXT NOT NULL,          -- TOC title
    page_url TEXT NOT NULL,            -- full Acronis URL
    section_heading TEXT,              -- H2/H3 heading for this chunk
    chunk_index INTEGER DEFAULT 0,     -- order within page
    content TEXT NOT NULL,
    word_count INTEGER,
    category TEXT,                     -- derived from slug prefix
    source_domain TEXT DEFAULT 'cyber_protection',  -- cyber_protection | cyber_cloud | developer | integrations | kb | youtube | blog
    embedding vector(2560),
    created_at TIMESTAMP DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_web_chunks_slug ON web_chunks (page_slug);

-- FTS support for web_chunks
ALTER TABLE web_chunks ADD COLUMN IF NOT EXISTS fts tsvector;
CREATE INDEX IF NOT EXISTS idx_web_chunks_fts ON web_chunks USING gin (fts);
CREATE OR REPLACE FUNCTION web_chunks_fts_update() RETURNS trigger AS $$
BEGIN
    NEW.fts := to_tsvector('english', COALESCE(NEW.content, ''));
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
DROP TRIGGER IF EXISTS web_chunks_fts_trigger ON web_chunks;
CREATE TRIGGER web_chunks_fts_trigger BEFORE INSERT OR UPDATE ON web_chunks
FOR EACH ROW EXECUTE FUNCTION web_chunks_fts_update();

-- Resume tracking for scraper
CREATE TABLE IF NOT EXISTS web_scrape_progress (
    page_slug TEXT PRIMARY KEY,
    page_url TEXT NOT NULL,
    source_domain TEXT DEFAULT 'cyber_protection',  -- which doc set
    status TEXT DEFAULT 'pending',     -- pending | scraped | failed
    error_message TEXT,
    scraped_at TIMESTAMP
);

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
