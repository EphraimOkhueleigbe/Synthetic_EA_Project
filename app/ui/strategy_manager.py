from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QSpinBox,
    QDoubleSpinBox,
    QMessageBox
)

from PySide6.QtCore import Qt

from database.models.strategy import Strategy

from app.controllers.strategy_controller import StrategyController
from app.core.app_state import app_state


class StrategyManager(QWidget):

    def __init__(self):

        super().__init__()

        self.controller = StrategyController()

        self.current_strategy = None

        self.strategies = []

        self.build_ui()

        app_state.project_changed.connect(
            self.project_changed
        )

        self.disable_editor()

    # ======================================================

    def build_ui(self):

        layout = QVBoxLayout(self)

        header = QHBoxLayout()

        self.title = QLabel("Strategies")

        self.title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        header.addWidget(self.title)

        header.addStretch()

        layout.addLayout(header)

        layout.addWidget(QLabel("Strategy Name"))

        self.name = QLineEdit()

        layout.addWidget(self.name)

        layout.addWidget(QLabel("D1 Fast EMA"))

        self.d1_fast = QSpinBox()

        self.d1_fast.setRange(1, 500)

        self.d1_fast.setValue(9)

        layout.addWidget(self.d1_fast)

        layout.addWidget(QLabel("D1 Slow EMA"))

        self.d1_slow = QSpinBox()

        self.d1_slow.setRange(1, 500)

        self.d1_slow.setValue(18)

        layout.addWidget(self.d1_slow)

        layout.addWidget(QLabel("M30 Fast EMA"))

        self.m30_fast = QSpinBox()

        self.m30_fast.setRange(1, 500)

        self.m30_fast.setValue(9)

        layout.addWidget(self.m30_fast)

        layout.addWidget(QLabel("M30 Slow EMA"))

        self.m30_slow = QSpinBox()

        self.m30_slow.setRange(1, 500)

        self.m30_slow.setValue(18)

        layout.addWidget(self.m30_slow)

        layout.addWidget(QLabel("Risk Formula"))

        self.risk = QLineEdit("Balance / 0.0008")

        layout.addWidget(self.risk)

        layout.addWidget(QLabel("Take Profit"))

        self.tp = QDoubleSpinBox()

        self.tp.setMaximum(100000000)

        self.tp.setValue(50000)

        layout.addWidget(self.tp)

        buttons = QHBoxLayout()

        self.save_button = QPushButton("Save Strategy")

        self.delete_button = QPushButton("Delete Strategy")

        buttons.addWidget(self.save_button)

        buttons.addWidget(self.delete_button)

        layout.addLayout(buttons)

        layout.addWidget(QLabel("Strategies"))

        self.list = QListWidget()

        layout.addWidget(self.list)

        self.save_button.clicked.connect(
            self.save_strategy
        )

        self.delete_button.clicked.connect(
            self.delete_strategy
        )

        self.list.itemClicked.connect(
            self.strategy_selected
        )

    # ======================================================

    def project_changed(self, project):

        print()
        print("=" * 50)
        print("StrategyManager.project_changed() called")
        print("Project:", project)
        print("=" * 50)

        if project is None:

            self.disable_editor()

            self.list.clear()

            self.title.setText("Strategies")

            return

        self.title.setText(
            f"Strategies - {project.name}"
        )

        self.enable_editor()

        print("Save Enabled:", self.save_button.isEnabled())

        self.load_strategies()
    # ======================================================

    def load_strategies(self):

        self.list.clear()

        print("=" * 50)
        print("Loading strategies for project:", app_state.current_project.id)

        self.strategies = self.controller.get_by_project(
            app_state.current_project.id
        )

        print("Strategies found:", len(self.strategies))
        print("=" * 50)

        for strategy in self.strategies:

            item = QListWidgetItem(strategy.name)

            item.setData(Qt.UserRole, strategy)

            self.list.addItem(item)

    # ======================================================

    def save_strategy(self):

        if app_state.current_project is None:
            return

        strategy = Strategy(

            project_id=app_state.current_project.id,

            name=self.name.text(),

            d1_fast_ema=self.d1_fast.value(),

            d1_slow_ema=self.d1_slow.value(),

            m30_fast_ema=self.m30_fast.value(),

            m30_slow_ema=self.m30_slow.value(),

            risk_formula=self.risk.text(),

            take_profit_value=self.tp.value()

        )

        print("=" * 50)
        print("Saving Strategy")
        print("Project ID:", strategy.project_id)
        print("Strategy:", strategy.name)
        print("=" * 50)

        self.controller.create(strategy)

        self.load_strategies()

        QMessageBox.information(
            self,
            "Saved",
            "Strategy saved successfully."
        )

    # ======================================================

    def strategy_selected(self, item):

        strategy = item.data(Qt.UserRole)

        self.current_strategy = strategy

        self.name.setText(strategy.name)

        self.d1_fast.setValue(strategy.d1_fast_ema)

        self.d1_slow.setValue(strategy.d1_slow_ema)

        self.m30_fast.setValue(strategy.m30_fast_ema)

        self.m30_slow.setValue(strategy.m30_slow_ema)

        self.risk.setText(strategy.risk_formula)

        self.tp.setValue(strategy.take_profit_value)

    # ======================================================

    def delete_strategy(self):

        if self.current_strategy is None:

            QMessageBox.information(
                self,
                "No Strategy",
                "Please select a strategy."
            )

            return

        self.controller.delete(self.current_strategy.id)

        self.current_strategy = None

        self.load_strategies()

    # ======================================================

    def disable_editor(self):

        self.save_button.setEnabled(False)

        self.delete_button.setEnabled(False)

        self.list.setEnabled(False)

        self.title.setText(
            "Strategies\n\nNo active project selected."
        )

    # ======================================================

    def enable_editor(self):

        self.save_button.setEnabled(True)

        self.delete_button.setEnabled(True)

        self.list.setEnabled(True)