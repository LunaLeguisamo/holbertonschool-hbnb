CREATE TABLE IF NOT EXISTS places (
    id VARCHAR(36) PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    price DECIMAL(10, 2)
    latitude FLOAT,
    longitude FLOAT,
    owner_id VARCHAR(36),
    FOREIGN KEY (owner_id) REFERENCES users(id)
);