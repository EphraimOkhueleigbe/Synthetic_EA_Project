from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QListWidget,
    QSpinBox,
    QDoubleSpinBox,
    QMessageBox
)

from database.models.strategy import Strategy
from app.controllers.strategy_controller import StrategyController


class StrategyManager(QWidget):

    def __init__(self):

        super().__init__()

        self.controller = StrategyController()

        self.current_strategy = None

        self.build_ui()

        self.load_strategies()

    # =====================================================

    def build_ui(self):

        layout = QVBoxLayout(self)

        # ---------------------------------

        layout.addWidget(QLabel("Strategy Name"))

        self.name = QLineEdit()

        layout.addWidget(self.name)

        # ---------------------------------

        layout.addWidget(QLabel("D1 Fast EMA"))

        self.d1_fast = QSpinBox()

        self.d1_fast.setRange(1, 500)

        self.d1_fast.setValue(9)

        layout.addWidget(self.d1_fast)

        # ---------------------------------

        layout.addWidget(QLabel("D1 Slow EMA"))

        self.d1_slow = QSpinBox()

        self.d1_slow.setRange(1, 500)

        self.d1_slow.setValue(18)

        layout.addWidget(self.d1_slow)

        # ---------------------------------

        layout.addWidget(QLabel("M30 Fast EMA"))

        self.m30_fast = QSpinBox()

        self.m30_fast.setRange(1, 500)

        self.m30_fast.setValue(9)

        layout.addWidget(self.m30_fast)

        # ---------------------------------

        layout.addWidget(QLabel("M30 Slow EMA"))

        self.m30_slow = QSpinBox()

        self.m30_slow.setRange(1, 500)

        self.m30_slow.setValue(18)

        layout.addWidget(self.m30_slow)

        # ---------------------------------

        layout.addWidget(QLabel("Risk Formula"))

        self.risk = QLineEdit()

        self.risk.setText("Balance / 0.0008")

        layout.addWidget(self.risk)

        # ---------------------------------

        layout.addWidget(QLabel("Take Profit"))

        self.tp = QDoubleSpinBox()

        self.tp.setMaximum(100000000)

        self.tp.setValue(50000)

        layout.addWidget(self.tp)

        # ---------------------------------

        self.save_button = QPushButton("Save Strategy")

        layout.addWidget(self.save_button)

        # ---------------------------------

        layout.addWidget(QLabel("Strategies"))

        self.list = QListWidget()

        layout.addWidget(self.list)

        # ---------------------------------

        self.delete_button = QPushButton("Delete Selected")

        layout.addWidget(self.delete_button)

        # ---------------------------------

        self.save_button.clicked.connect(self.save_strategy)

        self.delete_button.clicked.connect(self.delete_strategy)

        self.list.itemClicked.connect(self.strategy_selected)

    # =====================================================

    def load_strategies(self):

        self.list.clear()

        self.strategies = self.controller.get_all()

        for strategy in self.strategies:

            self.list.addItem(strategy.name)

    # =====================================================

    def save_strategy(self):

        strategy = Strategy(

            project_id=1,

            name=self.name.text(),

            d1_fast_ema=self.d1_fast.value(),

            d1_slow_ema=self.d1_slow.value(),

            m30_fast_ema=self.m30_fast.value(),

            m30_slow_ema=self.m30_slow.value(),

            risk_formula=self.risk.text(),

            take_profit_value=self.tp.value()

        )

        self.controller.create(strategy)

        self.load_strategies()

        QMessageBox.information(

            self,

            "Saved",

            "Strategy saved successfully."

        )

    # =====================================================

    def strategy_selected(self, item):

        index = self.list.currentRow()

        strategy = self.strategies[index]

        self.current_strategy = strategy

        self.name.setText(strategy.name)

        self.d1_fast.setValue(strategy.d1_fast_ema)

        self.d1_slow.setValue(strategy.d1_slow_ema)

        self.m30_fast.setValue(strategy.m30_fast_ema)

        self.m30_slow.setValue(strategy.m30_slow_ema)

        self.risk.setText(strategy.risk_formula)

        self.tp.setValue(strategy.take_profit_value)

    # =====================================================

    def delete_strategy(self):

        if self.current_strategy is None:
            return

        self.controller.delete(self.current_strategy.id)

        self.current_strategy = None

        self.load_strategies()