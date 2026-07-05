from database.repositories.base_repository import BaseRepository


class BacktestRepository(BaseRepository):

    ...

    def get_all(self):

        self.cursor.execute(
            """
            SELECT *
            FROM backtests
            ORDER BY created_at DESC
            """
        )

        return self.cursor.fetchall()

    def get_count(self):

        self.cursor.execute(
            """
            SELECT COUNT(*) AS total
            FROM backtests
            """
        )

        return self.cursor.fetchone()["total"]