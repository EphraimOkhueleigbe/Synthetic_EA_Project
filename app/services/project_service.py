from database.repositories.project_repository import ProjectRepository


class ProjectService:

    def __init__(self):

        self.repository = ProjectRepository()

    def get_all(self):

        return self.repository.get_all()

    def create(self, name):

        return self.repository.create(name)

    def update(self, project_id, name):

        return self.repository.update(
            project_id,
            name
        )

    def delete(self, project_id):

        return self.repository.delete(project_id)

    def get_count(self):

        return self.repository.get_count()