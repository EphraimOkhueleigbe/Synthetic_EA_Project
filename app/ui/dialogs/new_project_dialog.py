from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout
)


class NewProjectDialog(QDialog):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Create Project")

        self.resize(350, 150)

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Project Name"))

        self.name_edit = QLineEdit()

        layout.addWidget(self.name_edit)

        buttons = QHBoxLayout()

        self.cancel_button = QPushButton("Cancel")

        self.create_button = QPushButton("Create")

        buttons.addStretch()

        buttons.addWidget(self.cancel_button)

        buttons.addWidget(self.create_button)

        layout.addLayout(buttons)

        self.cancel_button.clicked.connect(self.reject)

        self.create_button.clicked.connect(self.accept)

    @property
    def project_name(self):

        return self.name_edit.text().strip()