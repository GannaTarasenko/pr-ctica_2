import sqlite3


def clreate_tables(path: str = './database.db'):
    with sqlite3.connect(path) as conn:
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(32),
            email VARCHAR(100) UNIQUE
            )
            """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS topics  (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            TOPIC VARCHAR(256) UNIQUE,
            author_id INTEGER,
            FOREIGN KEY(author_id) REFERENCES users(id)
                ON DELETE CASCADE
            )
            """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(250),
            text_field TEXT,
            author_id INTEGER,
            FOREIGN KEY(author_id) REFERENCES users(id)
                ON DELETE CASCADE
            )
            """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text_field TEXT,
            author_id INTEGER,
            post_id INTEGER,
            FOREIGN KEY(author_id) REFERENCES users(id)
                ON DELETE CASCADE,
            FOREIGN KEY(post_id) REFERENCES posts(id)
                ON DELETE CASCADE
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS post_topics (
            post_id INTEGER NOT NULL,
            topic_id INTEGER NOT NULL,
            FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
            FOREIGN KEY (topic_id) REFERENCES topics(id) ON DELETE CASCADE,
            PRIMARY KEY (post_id, topic_id)
            )
        """)


if __name__ == "__main__":
    clreate_tables()
