from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QStackedWidget,
    QLabel
)

from app.ui.dashboard import Dashboard
from app.ui.project_manager import ProjectManager
from app.ui.strategy_manager import StrategyManager
from app.ui.backtest_manager import BacktestManager


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

        # =====================================
        # Real Pages
        # =====================================

        self.dashboard = Dashboard()

        self.projects = ProjectManager()

        self.strategies = StrategyManager()

        self.backtests = BacktestManager()

        # =====================================
        # Placeholder Pages
        # =====================================

        self.optimizer = QLabel("Optimizer Page")

        self.reports = QLabel("Reports Page")

        self.settings = QLabel("Settings Page")

        # =====================================
        # Stack
        # =====================================

        self.stack.addWidget(self.dashboard)

        self.stack.addWidget(self.projects)

        self.stack.addWidget(self.strategies)

        self.stack.addWidget(self.backtests)

        self.stack.addWidget(self.optimizer)

        self.stack.addWidget(self.reports)

        self.stack.addWidget(self.settings)

        self.show_page(self.DASHBOARD)

    # =====================================

    def show_page(self, page):

        self.stack.setCurrentIndex(page)