from app.services.project_service import ProjectService


class ProjectController:

    def __init__(self):

        self.service = ProjectService()

    def get_projects(self):

        return self.service.get_all()

    def create_project(self, name):

        return self.service.create(name)

    def delete_project(self, project_id):

        return self.service.delete(project_id)