from database.repositories.backtest_repository import BacktestRepository


class BacktestService:

    def __init__(self):

        self.repository = BacktestRepository()

    def create(self, backtest):

        return self.repository.create(backtest)

    def get_all(self):

        return self.repository.get_all()

    def get_by_project(self, project_id):

        return self.repository.get_by_project(project_id)

    def delete(self, backtest_id):

        self.repository.delete(backtest_id)

    def get_count(self):

        return self.repository.get_count()