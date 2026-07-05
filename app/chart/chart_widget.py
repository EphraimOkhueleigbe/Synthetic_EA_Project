import pyqtgraph as pg

from PySide6.QtWidgets import QWidget, QVBoxLayout


class ChartWidget(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)

        self.plot = pg.PlotWidget()

        self.plot.showGrid(x=True, y=True)

        layout.addWidget(self.plot)

    def clear(self):

        self.plot.clear()