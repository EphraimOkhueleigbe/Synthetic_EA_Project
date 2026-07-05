from database.repositories.project_repository import ProjectRepository
from database.repositories.strategy_repository import StrategyRepository
from database.repositories.backtest_repository import BacktestRepository
from database.repositories.optimization_repository import OptimizationRepository


class DashboardController:

    def __init__(self):

        self.project_repo = ProjectRepository()
        self.strategy_repo = StrategyRepository()
        self.backtest_repo = BacktestRepository()
        self.optimization_repo = OptimizationRepository()

    def load_statistics(self):

        return {

            "projects": self.project_repo.get_count(),

            "strategies": self.strategy_repo.get_count(),

            "backtests": self.backtest_repo.get_count(),

            "optimizations": self.optimization_repo.get_count()

        }