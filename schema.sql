DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    score INTEGER DEFAULT 0,
    click_power INTEGER DEFAULT 1
);

INSERT INTO users (username, password, score, click_power)
VALUES ('admin', 'admin', 1000, 10);