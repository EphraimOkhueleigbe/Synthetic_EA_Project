from app.services.backtest_service import BacktestService


class BacktestController:

    def __init__(self):

        self.service = BacktestService()

    def create(self, backtest):

        return self.service.create(backtest)

    def get_all(self):

        return self.service.get_all()

    def get_by_project(self, project_id):

        return self.service.get_by_project(project_id)

    def delete(self, backtest_id):

        self.service.delete(backtest_id)

    def get_count(self):

        return self.service.get_count()