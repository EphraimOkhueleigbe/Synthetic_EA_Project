from database.repositories.base_repository import BaseRepository


class StrategyRepository(BaseRepository):

    def __init__(self):
        super().__init__()

    def create(
        self,
        project_id,
        name,
        ema_fast,
        ema_slow,
        risk_formula,
        take_profit
    ):

        self.cursor.execute(
            """
            INSERT INTO strategies(

                project_id,
                name,
                ema_fast,
                ema_slow,
                risk_formula,
                take_profit

            )

            VALUES(?,?,?,?,?,?)
            """,
            (
                project_id,
                name,
                ema_fast,
                ema_slow,
                risk_formula,
                take_profit
            )
        )

        self.commit()

        return self.cursor.lastrowid

    def get_all(self):

        self.cursor.execute("""
            SELECT *
            FROM strategies
            ORDER BY created_at DESC
        """)

        return self.cursor.fetchall()

    def get_count(self):

        self.cursor.execute("""
            SELECT COUNT(*) AS total
            FROM strategies
        """)

        return self.cursor.fetchone()["total"]