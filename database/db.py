import sqlite3
from pathlib import Path

DATABASE_NAME = "SyntheticQuant.db"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_PATH = PROJECT_ROOT / DATABASE_NAME


def get_connection():
    """
    Create and return a SQLite connection.
    """

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection