from database.repositories.strategy_repository import StrategyRepository


class StrategyService:

    def __init__(self):

        self.repository = StrategyRepository()

    # ==========================================
    # CREATE
    # ==========================================

    def create(self, strategy):

        return self.repository.create(strategy)

    # ==========================================
    # READ
    # ==========================================

    def get_all(self):

        return self.repository.get_all()

    def get_by_project(self, project_id):

        return self.repository.get_by_project(project_id)

    def get_count(self):

        return self.repository.get_count()

    # ==========================================
    # UPDATE
    # ==========================================

    def update(self, strategy):

        self.repository.update(strategy)

    # ==========================================
    # DELETE
    # ==========================================

    def delete(self, strategy_id):

        self.repository.delete(strategy_id)