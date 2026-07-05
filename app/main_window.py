from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout
)

from app.ui.project_panel import ProjectPanel


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("SyntheticQuant")

        self.resize(1600, 900)

        container = QWidget()

        self.setCentralWidget(container)

        layout = QHBoxLayout(container)

        self.project_panel = ProjectPanel()

        layout.addWidget(self.project_panel)