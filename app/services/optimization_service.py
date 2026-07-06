from database.repositories.optimization_repository import OptimizationRepository


class OptimizationService:

    def __init__(self):

        self.repository = OptimizationRepository()

    # ==========================================
    # READ
    # ==========================================

    def get_count(self):

        return self.repository.get_count()