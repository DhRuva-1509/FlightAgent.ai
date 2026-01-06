import sqlite3
from pathlib import Path

# project root = parent of "database" folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "database" / "flights.db"

def get_connection():
    return sqlite3.connect(DB_PATH)
