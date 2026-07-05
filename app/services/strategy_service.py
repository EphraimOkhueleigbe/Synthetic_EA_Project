from database.repositories.strategy_repository import StrategyRepository


class StrategyService:

    def __init__(self):
        self.repository = StrategyRepository()

    def create_strategy(self, *args, **kwargs):
        return self.repository.create(*args, **kwargs)

    def get_strategies(self):
        return self.repository.get_all()

    def get_strategy_count(self):
        return self.repository.get_count()