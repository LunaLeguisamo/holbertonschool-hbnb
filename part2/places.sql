CREATE TABLE IF NOT EXISTS places (
    id VARCHAR(36) PRIMARY KEY (UUID format),
    title VARCHAR(255),
    description VARCHAR(255),
    price DECIMAL(10, 2)
    latitude FLOAT
    longitude FLOAT
    owner_id VARCHAR(36)
);