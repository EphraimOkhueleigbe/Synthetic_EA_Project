from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton
)


class NewProjectDialog(QDialog):

    def __init__(self, project_name=""):

        super().__init__()

        self.project_name = ""

        # ==========================================
        # Create or Rename Mode
        # ==========================================

        self.rename_mode = bool(project_name)

        if self.rename_mode:
            self.setWindowTitle("Rename Project")
            button_text = "Save"
        else:
            self.setWindowTitle("New Project")
            button_text = "Create"

        self.resize(400, 250)

        layout = QVBoxLayout(self)

        # Project Name

        layout.addWidget(QLabel("Project Name"))

        self.name_edit = QLineEdit()

        self.name_edit.setText(project_name)

        layout.addWidget(self.name_edit)

        # Description (reserved for future use)

        layout.addWidget(QLabel("Description"))

        self.description_edit = QTextEdit()

        layout.addWidget(self.description_edit)

        # Buttons

        buttons = QHBoxLayout()

        self.cancel_button = QPushButton("Cancel")

        self.action_button = QPushButton(button_text)

        buttons.addStretch()

        buttons.addWidget(self.cancel_button)

        buttons.addWidget(self.action_button)

        layout.addLayout(buttons)

        self.cancel_button.clicked.connect(self.reject)

        self.action_button.clicked.connect(self.save)

    # ==========================================

    def save(self):

        self.project_name = self.name_edit.text().strip()

        self.accept()