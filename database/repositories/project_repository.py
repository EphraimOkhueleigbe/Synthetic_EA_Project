from database.repositories.base_repository import BaseRepository
from database.models.project import Project


class ProjectRepository(BaseRepository):

    def __init__(self):
        super().__init__()

    # ==========================================

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

    # ==========================================

    def get_all(self):

        self.cursor.execute(
            """
            SELECT *
            FROM projects
            ORDER BY created_at DESC
            """
        )

        rows = self.cursor.fetchall()

        return [
            Project.from_row(row)
            for row in rows
        ]

    # ==========================================

    def update(self, project_id, name):

        self.cursor.execute(
            """
            UPDATE projects
            SET
                name = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (
                name,
                project_id
            )
        )

        self.commit()

    # ==========================================

    def delete(self, project_id):

        self.cursor.execute(
            """
            DELETE FROM projects
            WHERE id = ?
            """,
            (project_id,)
        )

        self.commit()

    # ==========================================

    def get_count(self):

        self.cursor.execute(
            """
            SELECT COUNT(*) AS total
            FROM projects
            """
        )

        return self.cursor.fetchone()["total"]