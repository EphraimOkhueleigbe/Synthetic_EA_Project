from database.repositories.base_repository import BaseRepository


class BacktestRepository(BaseRepository):

    def __init__(self):
        super().__init__()

    def save(
        self,
        project_id,
        starting_balance,
        ending_balance,
        net_profit,
        win_rate,
        profit_factor,
        max_drawdown,
        total_trades
    ):

        self.cursor.execute(
            """
            INSERT INTO backtests(

                project_id,
                starting_balance,
                ending_balance,
                net_profit,
                win_rate,
                profit_factor,
                max_drawdown,
                total_trades

            )

            VALUES(?,?,?,?,?,?,?,?)
            """,

            (
                project_id,
                starting_balance,
                ending_balance,
                net_profit,
                win_rate,
                profit_factor,
                max_drawdown,
                total_trades
            )
        )

        self.commit()

        return self.cursor.lastrowid

    def get_all(self):

        self.cursor.execute(
            """
            SELECT *
            FROM backtests
            ORDER BY created_at DESC
            """
        )

        return self.cursor.fetchall()