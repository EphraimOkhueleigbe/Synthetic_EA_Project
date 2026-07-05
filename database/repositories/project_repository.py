from database.repositories.base_repository import BaseRepository


class ProjectRepository(BaseRepository):

    def __init__(self):
        super().__init__()

    def create(self, name):

        self.cursor.execute(
            """
            INSERT INTO projects(name)
            VALUES(?)
            """,
            (name,)
        )

        self.commit()

        return self.cursor.lastrowid

    def get_all(self):

        self.cursor.execute(
            """
            SELECT *

            FROM projects

            ORDER BY created_at DESC
            """
        )

        return self.cursor.fetchall()

    def get_count(self):

        self.cursor.execute(
            """
            SELECT COUNT(*) AS total

            FROM projects
            """
        )

        return self.cursor.fetchone()["total"]