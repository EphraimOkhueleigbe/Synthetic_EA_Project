from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout
)

from app.ui.project_panel import ProjectPanel
from app.ui.workspace import Workspace
from app.ui.menu_bar import build_menu
from app.ui.status_bar import build_status_bar


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("SyntheticQuant")

        self.resize(1600, 900)

        build_menu(self)
        build_status_bar(self)

        container = QWidget()

        self.setCentralWidget(container)

        layout = QHBoxLayout(container)

        self.project_panel = ProjectPanel()

        self.workspace = Workspace()

        layout.addWidget(
            self.project_panel,
            1
        )

        layout.addWidget(
            self.workspace,
            4
        )