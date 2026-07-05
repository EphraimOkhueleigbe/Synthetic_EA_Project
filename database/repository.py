from database.db import get_connection


class Repository:

    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    # ==========================================
    # PROJECTS
    # ==========================================

    def create_project(self, name):

        self.cursor.execute(
            """
            INSERT INTO projects(name)
            VALUES(?)
            """,
            (name,)
        )

        self.conn.commit()

        return self.cursor.lastrowid

    def get_projects(self):

        self.cursor.execute(
            """
            SELECT *
            FROM projects
            ORDER BY created_at DESC
            """
        )

        return self.cursor.fetchall()

    # ==========================================
    # BACKTESTS
    # ==========================================

    def save_backtest(

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

        self.conn.commit()

        return self.cursor.lastrowid

    def get_backtests(self):

        self.cursor.execute(
            """
            SELECT *
            FROM backtests
            ORDER BY created_at DESC
            """
        )

        return self.cursor.fetchall()

    # ==========================================
    # TRADES
    # ==========================================

    def save_trade(

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

        self.conn.commit()

    def get_trades(self, backtest_id):

        self.cursor.execute(

            """

            SELECT *

            FROM trades

            WHERE backtest_id=?

            """,

            (backtest_id,)

        )

        return self.cursor.fetchall()