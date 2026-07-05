from PySide6.QtWidgets import (
    QListWidget
)


class ProjectPanel(QListWidget):

    def __init__(self):

        super().__init__()

        self.addItem("Synthetic Quant")

        self.addItem("Demo Strategy")

        self.addItem("Optimization Tests")