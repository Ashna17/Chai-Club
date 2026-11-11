CREATE Extension IF NOT EXISTS postgis;
CREATE Extension IF NOT EXISTS vector;

CREATE table IF NOT EXISTS connect_profiles (
    user_id VARCHAR(64) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(10) NOT NULL CHECK (role IN ('host', 'guest')),
    location geography(Point, 4326) NOT NULL,
    topic text NOT NULL,
    embedding vector(384) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_connect_profiles_location ON connect_profiles USING GIST (location);
CREATE INDEX IF NOT EXISTS idx_connect_profiles_embedding ON connect_profiles USING hnsw (embedding vector_cosine_ops) WITH (m = 16, ef_construction = 64);