from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton
)


class NewProjectDialog(QDialog):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("New Project")

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Project Name"))

        self.name = QLineEdit()

        layout.addWidget(self.name)

        layout.addWidget(QLabel("Description"))

        self.description = QTextEdit()

        layout.addWidget(self.description)

        create_button = QPushButton("Create")

        create_button.clicked.connect(self.accept)

        layout.addWidget(create_button)