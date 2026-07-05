from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QInputDialog,
)

from app.controllers.project_controller import ProjectController


class ProjectPanel(QWidget):

    def __init__(self):

        super().__init__()

        self.controller = ProjectController()

        layout = QVBoxLayout(self)

        title = QLabel("Projects")

        layout.addWidget(title)

        self.project_list = QListWidget()

        layout.addWidget(self.project_list)

        self.new_button = QPushButton("New Project")

        layout.addWidget(self.new_button)

        self.new_button.clicked.connect(
            self.new_project
        )

        self.refresh()

    # =========================================

    def refresh(self):

        self.project_list.clear()

        self.projects = self.controller.get_projects()

        for project in self.projects:

            self.project_list.addItem(
                project.name
            )

    # =========================================

    def new_project(self):

        name, ok = QInputDialog.getText(

            self,

            "New Project",

            "Project Name"

        )

        if not ok:
            return

        if not name.strip():
            return

        self.controller.create_project(name)

        self.refresh()