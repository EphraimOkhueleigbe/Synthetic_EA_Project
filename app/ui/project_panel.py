from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QLineEdit
)

from app.controllers.project_controller import ProjectController
from app.dialogs.new_project_dialog import NewProjectDialog


class ProjectPanel(QWidget):

    project_selected = Signal(int)

    def __init__(self):

        super().__init__()

        self.controller = ProjectController()

        layout = QVBoxLayout(self)

        title = QLabel("Projects")

        title.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        self.search = QLineEdit()

        self.search.setPlaceholderText("Search project...")

        layout.addWidget(self.search)

        self.new_button = QPushButton("New Project")

        layout.addWidget(self.new_button)

        self.project_list = QListWidget()

        layout.addWidget(self.project_list)

        self.new_button.clicked.connect(
            self.create_project
        )

        self.project_list.itemClicked.connect(
            self.select_project
        )

        self.search.textChanged.connect(
            self.filter_projects
        )

        self.projects = []

        self.refresh()

    def refresh(self):

        self.projects = self.controller.get_projects()

        self.project_list.clear()

        for project in self.projects:

            self.project_list.addItem(
                project["name"]
            )

    def create_project(self):

        dialog = NewProjectDialog()

        if dialog.exec():

            self.controller.create_project(
                dialog.name.text(),
                dialog.description.toPlainText()
            )

            self.refresh()

    def select_project(self, item):

        index = self.project_list.row(item)

        project = self.projects[index]

        self.project_selected.emit(
            project["id"]
        )

    def filter_projects(self, text):

        self.project_list.clear()

        for project in self.projects:

            if text.lower() in project["name"].lower():

                self.project_list.addItem(
                    project["name"]
                )