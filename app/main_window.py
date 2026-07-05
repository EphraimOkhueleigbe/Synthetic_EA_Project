from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout
)

from app.ui.navigation import Navigation
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

        self.navigation = Navigation()

        self.workspace = Workspace()

        layout.addWidget(self.navigation, 1)

        layout.addWidget(self.workspace, 5)

        self.navigation.dashboard_btn.clicked.connect(
            lambda: (
                print("Dashboard"),
                self.workspace.show_page(Workspace.DASHBOARD)
            )
        )

        self.navigation.projects_btn.clicked.connect(
            lambda: self.workspace.show_page(Workspace.PROJECTS)
        )

        self.navigation.strategies_btn.clicked.connect(
            lambda: self.workspace.show_page(Workspace.STRATEGIES)
        )

        self.navigation.backtests_btn.clicked.connect(
            lambda: self.workspace.show_page(Workspace.BACKTESTS)
        )

        self.navigation.optimizer_btn.clicked.connect(
            lambda: self.workspace.show_page(Workspace.OPTIMIZER)
        )

        self.navigation.reports_btn.clicked.connect(
            lambda: self.workspace.show_page(Workspace.REPORTS)
        )

        self.navigation.settings_btn.clicked.connect(
            lambda: self.workspace.show_page(Workspace.SETTINGS)
        )