from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton
)


class Navigation(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)

        self.dashboard_btn = QPushButton("🏠 Dashboard")
        self.projects_btn = QPushButton("📁 Projects")
        self.strategies_btn = QPushButton("📈 Strategies")
        self.backtests_btn = QPushButton("🧪 Backtests")
        self.optimizer_btn = QPushButton("⚙ Optimizer")
        self.reports_btn = QPushButton("📊 Reports")
        self.settings_btn = QPushButton("🔧 Settings")

        buttons = [

            self.dashboard_btn,

            self.projects_btn,

            self.strategies_btn,

            self.backtests_btn,

            self.optimizer_btn,

            self.reports_btn,

            self.settings_btn

        ]

        for button in buttons:

            button.setMinimumHeight(45)

            layout.addWidget(button)

        layout.addStretch()