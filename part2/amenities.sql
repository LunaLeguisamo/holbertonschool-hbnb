CREATE TABLE IF NOT EXISTS amenities (
    id CHAR(36) PRIMARY KEY unique_id,
    name VARCHAR(255) UNIQUE
);