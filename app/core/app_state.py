from PySide6.QtCore import QObject, Signal


class AppState(QObject):

    project_changed = Signal(object)

    strategy_changed = Signal(object)

    backtest_changed = Signal(object)

    def __init__(self):

        super().__init__()

        self.current_project = None

        self.current_strategy = None

        self.current_backtest = None

    # =========================================

    def set_current_project(self, project):

        self.current_project = project

        self.project_changed.emit(project)

    # =========================================

    def set_current_strategy(self, strategy):

        self.current_strategy = strategy

        self.strategy_changed.emit(strategy)

    # =========================================

    def set_current_backtest(self, backtest):

        self.current_backtest = backtest

        self.backtest_changed.emit(backtest)


app_state = AppState()