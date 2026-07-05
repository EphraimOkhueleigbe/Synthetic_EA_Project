from app.services.backtest_service import BacktestService


class ApplicationController:

    def __init__(self):

        self.backtest_service = BacktestService()