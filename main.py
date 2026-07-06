import sys

from PySide6.QtWidgets import QApplication

from database.initialize import initialize

from app.main_window import MainWindow


def main():

    # ==========================================
    # Initialize Database
    # ==========================================

    initialize()

    # ==========================================
    # Start Application
    # ==========================================

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()