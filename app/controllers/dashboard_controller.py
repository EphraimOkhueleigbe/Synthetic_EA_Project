from database.repository import Repository


class DashboardController:

    def __init__(self):

        self.repo = Repository()

    def load_statistics(self):

        return {

            "projects":
                self.repo.get_project_count(),

            "strategies":
                self.repo.get_strategy_count(),

            "backtests":
                self.repo.get_backtest_count(),

            "optimizations":
                self.repo.get_optimization_count()

        }