from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QListWidget,
    QMessageBox
)

from PySide6.QtCore import Qt

from app.controllers.project_controller import ProjectController
from app.ui.dialogs.new_project_dialog import NewProjectDialog


class ProjectManager(QWidget):

    def __init__(self):

        super().__init__()

        self.controller = ProjectController()

        layout = QVBoxLayout(self)

        # ----------------------------------------
        # Header
        # ----------------------------------------

        header = QHBoxLayout()

        title = QLabel("Projects")

        title.setAlignment(Qt.AlignLeft)

        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        self.new_button = QPushButton("New Project")

        header.addWidget(title)

        header.addStretch()

        header.addWidget(self.new_button)

        layout.addLayout(header)

        # ----------------------------------------
        # Project List
        # ----------------------------------------

        self.project_list = QListWidget()

        layout.addWidget(self.project_list)

        # ----------------------------------------
        # Events
        # ----------------------------------------

        self.new_button.clicked.connect(
            self.create_project
        )

        self.refresh()

    # ==========================================
    # Refresh
    # ==========================================

    def refresh(self):

        self.project_list.clear()

        projects = self.controller.get_projects()

        for project in projects:

            self.project_list.addItem(project.name)

    # ==========================================
    # Create Project
    # ==========================================

    def create_project(self):

        dialog = NewProjectDialog()

        if dialog.exec():

            name = dialog.project_name

            if not name:

                QMessageBox.warning(
                    self,
                    "Invalid Name",
                    "Please enter a project name."
                )

                return

            self.controller.create_project(name)

            self.refresh()