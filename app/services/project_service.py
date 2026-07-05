from database.repositories.project_repository import ProjectRepository


class ProjectService:

    def __init__(self):
        self.repository = ProjectRepository()

    def create_project(self, name):

        return self.repository.create(name)

    def get_projects(self):

        return self.repository.get_all()

    def get_project_count(self):

        return self.repository.get_count()