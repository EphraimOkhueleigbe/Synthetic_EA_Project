from services.backtest_service import BacktestService


class BacktestController:

    def __init__(self):

        self.service = BacktestService()

    def run(

        self,

        strategy,

        symbol,

        timeframe,

        candles

    ):

        return self.service.run_backtest(

            strategy,

            symbol,

            timeframe,

            candles

        )