from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QStackedWidget,
    QLabel
)

from app.ui.dashboard import Dashboard


class Workspace(QWidget):

    DASHBOARD = 0
    PROJECTS = 1
    STRATEGIES = 2
    BACKTESTS = 3
    OPTIMIZER = 4
    REPORTS = 5
    SETTINGS = 6

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)

        self.stack = QStackedWidget()

        layout.addWidget(self.stack)

        self.dashboard = Dashboard()

        self.projects = QLabel("Projects Page")

        self.strategies = QLabel("Strategies Page")

        self.backtests = QLabel("Backtests Page")

        self.optimizer = QLabel("Optimizer Page")

        self.reports = QLabel("Reports Page")

        self.settings = QLabel("Settings Page")

        self.stack.addWidget(self.dashboard)
        self.stack.addWidget(self.projects)
        self.stack.addWidget(self.strategies)
        self.stack.addWidget(self.backtests)
        self.stack.addWidget(self.optimizer)
        self.stack.addWidget(self.reports)
        self.stack.addWidget(self.settings)

        self.show_page(self.DASHBOARD)

    # ======================================

    def show_page(self, page):

        print(f"Switching to page: {page}")

        self.stack.setCurrentIndex(page)

        print(f"Current index: {self.stack.currentIndex()}")