from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QGridLayout,
    QVBoxLayout
)

from PySide6.QtCore import Qt

from app.controllers.dashboard_controller import DashboardController
from app.ui.widgets.stat_card import StatCard
from app.core.app_state import app_state


class Dashboard(QWidget):

    def __init__(self):

        super().__init__()

        self.controller = DashboardController()

        layout = QVBoxLayout(self)

        # ==========================================
        # Dashboard Title
        # ==========================================

        self.title = QLabel("SyntheticQuant Dashboard")

        self.title.setAlignment(Qt.AlignCenter)

        self.title.setStyleSheet("""
            font-size:30px;
            font-weight:bold;
        """)

        layout.addWidget(self.title)

        # ==========================================
        # Statistics Grid
        # ==========================================

        grid = QGridLayout()

        self.project_card = StatCard("Projects")
        self.strategy_card = StatCard("Strategies")
        self.backtest_card = StatCard("Backtests")
        self.optimization_card = StatCard("Optimizations")

        grid.addWidget(self.project_card, 0, 0)
        grid.addWidget(self.strategy_card, 0, 1)
        grid.addWidget(self.backtest_card, 1, 0)
        grid.addWidget(self.optimization_card, 1, 1)

        layout.addLayout(grid)

        # ==========================================
        # Initial Load
        # ==========================================

        self.refresh()

        # ==========================================
        # Listen for Active Project Changes
        # ==========================================

        app_state.project_changed.connect(
            self.project_changed
        )

    # ==========================================

    def refresh(self):

        stats = self.controller.load_statistics()

        self.project_card.set_value(
            stats["projects"]
        )

        self.strategy_card.set_value(
            stats["strategies"]
        )

        self.backtest_card.set_value(
            stats["backtests"]
        )

        self.optimization_card.set_value(
            stats["optimizations"]
        )

    # ==========================================

    def project_changed(self, project):

        if project is None:

            self.title.setText(
                "SyntheticQuant Dashboard\n\nNo Project Selected"
            )

            print()

            print("=" * 50)

            print("Dashboard: No Active Project")

            print("=" * 50)

            print()

            return

        self.title.setText(
            f"SyntheticQuant Dashboard\n\nCurrent Project: {project.name}"
        )

        print()

        print("=" * 50)

        print("Dashboard received active project")

        print(f"Project: {project.name}")

        print("=" * 50)

        print()