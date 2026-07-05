from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout
)

from app.ui.dashboard import Dashboard


class Workspace(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)

        self.dashboard = Dashboard()

        layout.addWidget(
            self.dashboard
        )