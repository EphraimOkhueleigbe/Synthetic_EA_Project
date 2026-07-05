from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QGridLayout,
    QVBoxLayout
)

from PySide6.QtCore import Qt

from app.controllers.dashboard_controller import DashboardController
from app.ui.widgets.stat_card import StatCard


class Dashboard(QWidget):

    def __init__(self):

        super().__init__()

        self.controller = DashboardController()

        layout = QVBoxLayout(self)

        title = QLabel("SyntheticQuant Dashboard")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            font-size:30px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        grid = QGridLayout()

        self.project_card = StatCard("Projects")

        self.strategy_card = StatCard("Strategies")

        self.backtest_card = StatCard("Backtests")

        self.optimization_card = StatCard("Optimizations")

        grid.addWidget(self.project_card,0,0)
        grid.addWidget(self.strategy_card,0,1)
        grid.addWidget(self.backtest_card,1,0)
        grid.addWidget(self.optimization_card,1,1)

        layout.addLayout(grid)

        self.refresh()

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