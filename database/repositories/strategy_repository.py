from database.repositories.base_repository import BaseRepository
from database.models.strategy import Strategy


class StrategyRepository(BaseRepository):

    def __init__(self):
        super().__init__()

    # ==========================================
    # CREATE
    # ==========================================

    def create(self, strategy: Strategy):

        self.cursor.execute(
            """
            INSERT INTO strategies(

                project_id,
                name,

                d1_fast_ema,
                d1_slow_ema,

                m30_fast_ema,
                m30_slow_ema,

                risk_formula,

                stop_loss_type,
                stop_loss_value,

                take_profit_type,
                take_profit_value,

                trade_direction,

                active

            )

            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,

            (

                strategy.project_id,
                strategy.name,

                strategy.d1_fast_ema,
                strategy.d1_slow_ema,

                strategy.m30_fast_ema,
                strategy.m30_slow_ema,

                strategy.risk_formula,

                strategy.stop_loss_type,
                strategy.stop_loss_value,

                strategy.take_profit_type,
                strategy.take_profit_value,

                strategy.trade_direction,

                strategy.active

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

            FROM strategies

            ORDER BY name

        """)

        rows = self.cursor.fetchall()

        return [

            Strategy.from_row(row)

            for row in rows

        ]

    def get_by_project(self, project_id):

        self.cursor.execute("""

            SELECT *

            FROM strategies

            WHERE project_id=?

            ORDER BY name

        """, (project_id,))

        rows = self.cursor.fetchall()

        return [

            Strategy.from_row(row)

            for row in rows

        ]

    def get_count(self):

        self.cursor.execute("""

            SELECT COUNT(*) AS total

            FROM strategies

        """)

        return self.cursor.fetchone()["total"]

    # ==========================================
    # UPDATE
    # ==========================================

    def update(self, strategy: Strategy):

        self.cursor.execute("""

            UPDATE strategies

            SET

                name=?,

                d1_fast_ema=?,
                d1_slow_ema=?,

                m30_fast_ema=?,
                m30_slow_ema=?,

                risk_formula=?,

                stop_loss_type=?,
                stop_loss_value=?,

                take_profit_type=?,
                take_profit_value=?,

                trade_direction=?,

                active=?

            WHERE id=?

        """,

        (

            strategy.name,

            strategy.d1_fast_ema,
            strategy.d1_slow_ema,

            strategy.m30_fast_ema,
            strategy.m30_slow_ema,

            strategy.risk_formula,

            strategy.stop_loss_type,
            strategy.stop_loss_value,

            strategy.take_profit_type,
            strategy.take_profit_value,

            strategy.trade_direction,

            strategy.active,

            strategy.id

        ))

        self.commit()

    # ==========================================
    # DELETE
    # ==========================================

    def delete(self, strategy_id):

        self.cursor.execute("""

            DELETE

            FROM strategies

            WHERE id=?

        """, (strategy_id,))

        self.commit()