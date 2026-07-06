from app.services.project_service import ProjectService
from app.services.strategy_service import StrategyService
from app.services.backtest_service import BacktestService
from app.services.optimization_service import OptimizationService


class DashboardController:

    def __init__(self):

        self.project_service = ProjectService()
        self.strategy_service = StrategyService()
        self.backtest_service = BacktestService()
        self.optimization_service = OptimizationService()

    # ==========================================

    def load_statistics(self):

        return {
            "projects": self.project_service.get_count(),
            "strategies": self.strategy_service.get_count(),
            "backtests": self.backtest_service.get_count(),
            "optimizations": self.optimization_service.get_count(),
        }