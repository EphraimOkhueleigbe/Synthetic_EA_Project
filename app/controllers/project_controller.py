from app.services.project_service import ProjectService


class ProjectController:

    def __init__(self):

        self.service = ProjectService()

    def create(self, name):

        return self.service.create(name)

    def get_all(self):

        return self.service.get_all()

    def delete(self, project_id):

        return self.service.delete(project_id)

    def get_count(self):

        return self.service.get_count()