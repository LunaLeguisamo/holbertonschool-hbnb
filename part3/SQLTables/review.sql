CREATE TABLE IF NOT EXISTS reviews (
    id CHAR(36) PRIMARY KEY,
    text TEXT,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    user_id CHAR(36),
    place_id CHAR(36),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (place_id) REFERENCES places(id),
    CONSTRAINT unique_review UNIQUE (user_id, place_id)
    );