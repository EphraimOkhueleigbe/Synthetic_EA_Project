from app.services.strategy_service import StrategyService


class StrategyController:

    def __init__(self):

        self.service = StrategyService()

    def create(self, strategy):

        return self.service.create(strategy)

    def get_all(self):

        return self.service.get_all()

    def get_by_project(self, project_id):

        return self.service.get_by_project(project_id)

    def update(self, strategy):

        self.service.update(strategy)

    def delete(self, strategy_id):

        self.service.delete(strategy_id)

    def get_count(self):

        return self.service.get_count()