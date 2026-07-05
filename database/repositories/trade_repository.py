from database.repositories.base_repository import BaseRepository


class TradeRepository(BaseRepository):

    def __init__(self):
        super().__init__()

    def save(
        self,
        backtest_id,
        direction,
        entry,
        exit_price,
        stop_loss,
        take_profit,
        result,
        profit
    ):

        self.cursor.execute(
            """
            INSERT INTO trades(

                backtest_id,
                direction,
                entry_price,
                exit_price,
                stop_loss,
                take_profit,
                result,
                profit

            )

            VALUES(?,?,?,?,?,?,?,?)
            """,

            (
                backtest_id,
                direction,
                entry,
                exit_price,
                stop_loss,
                take_profit,
                result,
                profit
            )
        )

        self.commit()

    def get_all(self, backtest_id):

        self.cursor.execute(
            """
            SELECT *

            FROM trades

            WHERE backtest_id=?
            """,

            (backtest_id,)
        )

        return self.cursor.fetchall()