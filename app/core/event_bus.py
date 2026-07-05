from PySide6.QtCore import QObject, Signal


class EventBus(QObject):

    project_created = Signal()

    project_selected = Signal(int)

    backtest_completed = Signal()

    optimization_completed = Signal()

    strategy_saved = Signal()


event_bus = EventBus()