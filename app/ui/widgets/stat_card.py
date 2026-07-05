from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QFrame
)


class StatCard(QFrame):

    def __init__(self, title, value="0"):

        super().__init__()

        self.setFrameShape(QFrame.Box)

        self.setStyleSheet("""
            QFrame{
                border-radius:8px;
                border:1px solid #444;
                background:#2d2d2d;
            }
        """)

        layout = QVBoxLayout(self)

        self.title = QLabel(title)

        self.title.setAlignment(Qt.AlignCenter)

        self.value = QLabel(value)

        self.value.setAlignment(Qt.AlignCenter)

        self.value.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        layout.addWidget(self.title)
        layout.addWidget(self.value)

    def set_value(self, value):

        self.value.setText(str(value))