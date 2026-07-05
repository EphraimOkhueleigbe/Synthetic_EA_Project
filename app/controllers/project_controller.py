from database.repository import Repository


class ProjectController:

    def __init__(self):
        self.repo = Repository()

    def get_projects(self):
        return self.repo.get_projects()

    def create_project(self, name, description=""):
        return self.repo.create_project(
            name=name,
            description=description
        )

    def delete_project(self, project_id):
        return self.repo.delete_project(project_id)