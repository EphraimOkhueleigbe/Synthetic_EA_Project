from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
    QComboBox,
    QDateEdit
)

from PySide6.QtCore import Qt, QDate

from app.controllers.backtest_controller import BacktestController
from app.controllers.strategy_controller import StrategyController
from app.core.app_state import app_state

from database.models.backtest import Backtest


class BacktestManager(QWidget):

    def __init__(self):

        super().__init__()

        self.backtest_controller = BacktestController()
        self.strategy_controller = StrategyController()

        self.backtests = []
        self.strategies = []

        self.current_backtest = None

        self.build_ui()

        app_state.project_changed.connect(
            self.project_changed
        )

        self.disable_editor()

    # =====================================================

    def build_ui(self):

        layout = QVBoxLayout(self)

        header = QHBoxLayout()

        self.title = QLabel("Backtests")

        self.title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        header.addWidget(self.title)

        header.addStretch()

        layout.addLayout(header)

        # ---------------------------------------

        layout.addWidget(QLabel("Strategy"))

        self.strategy_combo = QComboBox()

        layout.addWidget(self.strategy_combo)

        # ---------------------------------------

        layout.addWidget(QLabel("Symbol"))

        self.symbol_combo = QComboBox()

        self.symbol_combo.addItems([

            "Drift Switch Index 10"

        ])

        layout.addWidget(self.symbol_combo)

        # ---------------------------------------

        layout.addWidget(QLabel("Start Date"))

        self.start_date = QDateEdit()

        self.start_date.setCalendarPopup(True)

        self.start_date.setDate(
            QDate.currentDate().addYears(-1)
        )

        layout.addWidget(self.start_date)

        # ---------------------------------------

        layout.addWidget(QLabel("End Date"))

        self.end_date = QDateEdit()

        self.end_date.setCalendarPopup(True)

        self.end_date.setDate(
            QDate.currentDate()
        )

        layout.addWidget(self.end_date)

        # ---------------------------------------

        buttons = QHBoxLayout()

        self.save_button = QPushButton("Save Backtest")

        self.delete_button = QPushButton("Delete")

        buttons.addWidget(self.save_button)

        buttons.addWidget(self.delete_button)

        layout.addLayout(buttons)

        # ---------------------------------------

        layout.addWidget(QLabel("Saved Backtests"))

        self.list = QListWidget()

        layout.addWidget(self.list)

        # ---------------------------------------

        self.save_button.clicked.connect(
            self.save_backtest
        )

        self.delete_button.clicked.connect(
            self.delete_backtest
        )

        self.list.itemClicked.connect(
            self.backtest_selected
        )

    # =====================================================

    def project_changed(self, project):

        if project is None:

            self.disable_editor()

            self.list.clear()

            return

        self.enable_editor()

        self.title.setText(
            f"Backtests - {project.name}"
        )

        self.load_strategies()

        self.load_backtests()

    # =====================================================

    def load_strategies(self):

        self.strategy_combo.clear()

        self.strategies = self.strategy_controller.get_by_project(
            app_state.current_project.id
        )

        for strategy in self.strategies:

            self.strategy_combo.addItem(
                strategy.name,
                strategy.id
            )

    # =====================================================

    def load_backtests(self):

        self.list.clear()

        self.backtests = self.backtest_controller.get_by_project(
            app_state.current_project.id
        )

        for bt in self.backtests:

            item = QListWidgetItem(

                f"{bt.symbol} ({bt.status})"

            )

            item.setData(Qt.UserRole, bt)

            self.list.addItem(item)

    # =====================================================

    def save_backtest(self):

        if self.strategy_combo.count() == 0:

            QMessageBox.information(

                self,

                "No Strategies",

                "Create a strategy first."

            )

            return

        backtest = Backtest(

            project_id=app_state.current_project.id,

            strategy_id=self.strategy_combo.currentData(),

            symbol=self.symbol_combo.currentText(),

            start_date=self.start_date.date().toString(
                "yyyy-MM-dd"
            ),

            end_date=self.end_date.date().toString(
                "yyyy-MM-dd"
            )

        )

        self.backtest_controller.create(backtest)

        self.load_backtests()

    # =====================================================

    def backtest_selected(self, item):

        self.current_backtest = item.data(Qt.UserRole)

    # =====================================================

    def delete_backtest(self):

        if self.current_backtest is None:

            return

        self.backtest_controller.delete(
            self.current_backtest.id
        )

        self.current_backtest = None

        self.load_backtests()

    # =====================================================

    def disable_editor(self):

        self.save_button.setEnabled(False)

        self.delete_button.setEnabled(False)

        self.strategy_combo.setEnabled(False)

        self.symbol_combo.setEnabled(False)

        self.start_date.setEnabled(False)

        self.end_date.setEnabled(False)

        self.list.setEnabled(False)

    # =====================================================

    def enable_editor(self):

        self.save_button.setEnabled(True)

        self.delete_button.setEnabled(True)

        self.strategy_combo.setEnabled(True)

        self.symbol_combo.setEnabled(True)

        self.start_date.setEnabled(True)

        self.end_date.setEnabled(True)

        self.list.setEnabled(True)