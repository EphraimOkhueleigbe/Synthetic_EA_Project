from database.repositories.backtest_repository import BacktestRepository


class BacktestService:

    def __init__(self):
        self.repository = BacktestRepository()

    def save_backtest(self, *args, **kwargs):
        return self.repository.save(*args, **kwargs)

    def get_backtests(self):
        return self.repository.get_all()

    def get_backtest_count(self):
        return self.repository.get_count()