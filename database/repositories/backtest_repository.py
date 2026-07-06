from database.repositories.base_repository import BaseRepository
from database.models.backtest import Backtest


class BacktestRepository(BaseRepository):

    def __init__(self):
        super().__init__()

    # ==========================================
    # CREATE
    # ==========================================

    def create(self, backtest: Backtest):

        self.cursor.execute(
            """
            INSERT INTO backtests(

                project_id,
                strategy_id,
                symbol,
                start_date,
                end_date,
                status

            )

            VALUES(?,?,?,?,?,?)
            """,

            (

                backtest.project_id,
                backtest.strategy_id,
                backtest.symbol,
                backtest.start_date,
                backtest.end_date,
                backtest.status

            )

        )

        self.commit()

        return self.cursor.lastrowid

    # ==========================================
    # READ
    # ==========================================

    def get_all(self):

        self.cursor.execute("""

            SELECT *

            FROM backtests

            ORDER BY created_at DESC

        """)

        rows = self.cursor.fetchall()

        return [

            Backtest.from_row(row)

            for row in rows

        ]

    def get_by_project(self, project_id):

        self.cursor.execute("""

            SELECT *

            FROM backtests

            WHERE project_id=?

            ORDER BY created_at DESC

        """, (project_id,))

        rows = self.cursor.fetchall()

        return [

            Backtest.from_row(row)

            for row in rows

        ]

    def get_count(self):

        self.cursor.execute("""

            SELECT COUNT(*) AS total

            FROM backtests

        """)

        return self.cursor.fetchone()["total"]

    # ==========================================
    # DELETE
    # ==========================================

    def delete(self, backtest_id):

        self.cursor.execute("""

            DELETE

            FROM backtests

            WHERE id=?

        """, (backtest_id,))

        self.commit()