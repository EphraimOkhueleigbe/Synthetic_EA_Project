from database.repositories.base_repository import BaseRepository


class OptimizationRepository(BaseRepository):

    def __init__(self):
        super().__init__()

    def get_count(self):

        self.cursor.execute("""
            SELECT COUNT(*) AS total
            FROM optimizations
        """)

        return self.cursor.fetchone()["total"]