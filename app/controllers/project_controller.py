from app.services.project_service import ProjectService


class ProjectController:

    def __init__(self):
        self.service = ProjectService()

    def get_projects(self):
        return self.service.get_projects()

    def create_project(self, name):
        return self.service.create_project(name)

    def get_project_count(self):
        return self.service.get_project_count()