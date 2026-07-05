from database.db import get_connection


class BaseRepository:
    """
    Base class for all repositories.

    Handles:
    - Opening the SQLite connection
    - Creating the cursor
    - Committing transactions
    - Rolling back transactions
    - Closing the connection
    """

    def __init__(self):
        self.connection = get_connection()
        self.cursor = self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def close(self):
        self.connection.close()