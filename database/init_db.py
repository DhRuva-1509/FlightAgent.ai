import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "flights.db"

def run_sql_file(path):
    with open(path, "r") as f:
        return f.read()


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        cursor.executescript(run_sql_file(BASE_DIR / "schema.sql"))
        cursor.executescript(run_sql_file(BASE_DIR / "seed_data.sql"))

        conn.commit()

    print("Database initialized successfully.")


if __name__ == "__main__":
    init_db()
