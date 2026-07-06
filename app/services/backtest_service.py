from database.repositories.backtest_repository import BacktestRepository


class BacktestService:

    def __init__(self):

        self.repository = BacktestRepository()

    # ==========================================
    # CREATE
    # ==========================================

    def create(self, *args, **kwargs):

        return self.repository.save(*args, **kwargs)

    # ==========================================
    # READ
    # ==========================================

    def get_all(self):

        return self.repository.get_all()

    def get_count(self):

        return self.repository.get_count()