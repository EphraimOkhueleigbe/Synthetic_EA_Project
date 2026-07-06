from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QMessageBox
)

from PySide6.QtCore import Qt

from app.controllers.project_controller import ProjectController
from app.ui.dialogs.new_project_dialog import NewProjectDialog
from app.core.app_state import app_state

class ProjectManager(QWidget):

    def __init__(self):

        super().__init__()

        self.controller = ProjectController()

        layout = QVBoxLayout(self)

        # ==========================================
        # Header
        # ==========================================

        header = QHBoxLayout()

        title = QLabel("Projects")

        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        self.new_button = QPushButton("New Project")

        header.addWidget(title)

        header.addStretch()

        header.addWidget(self.new_button)

        layout.addLayout(header)

        # ==========================================
        # Project List
        # ==========================================

        self.project_list = QListWidget()

        layout.addWidget(self.project_list)

        # ==========================================
        # Events
        # ==========================================

        self.new_button.clicked.connect(
            self.create_project
        )

        self.project_list.itemDoubleClicked.connect(
            self.open_project
        )

        self.refresh()

    # ==========================================

    def refresh(self):

        self.project_list.clear()

        projects = self.controller.get_projects()

        for project in projects:

            item = QListWidgetItem(project.name)

            # Store the whole Project object
            item.setData(Qt.UserRole, project)

            self.project_list.addItem(item)

    # ==========================================

    def create_project(self):

        dialog = NewProjectDialog()

        if dialog.exec():

            name = dialog.project_name

            if not name:

                QMessageBox.warning(
                    self,
                    "Invalid Name",
                    "Project name cannot be empty."
                )

                return

            self.controller.create_project(name)

            self.refresh()

    # ==========================================

    def selected_project(self):

        item = self.project_list.currentItem()

        if item is None:

            return None

        return item.data(Qt.UserRole)

    # ==========================================

    def open_project(self, item):

        project = item.data(Qt.UserRole)

        app_state.set_current_project(project)

        print()

        print("=" * 50)

        print(f"ACTIVE PROJECT: {project.name}")

        print(f"PROJECT ID: {project.id}")

        print("=" * 50)

        print()