from database.repositories.optimization_repository import OptimizationRepository


class OptimizationService:

    def __init__(self):
        self.repository = OptimizationRepository()

    def get_optimization_count(self):
        return self.repository.get_count()