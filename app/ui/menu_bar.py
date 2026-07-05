from PySide6.QtGui import QAction


def build_menu(window):

    menu_bar = window.menuBar()

    # File
    file_menu = menu_bar.addMenu("File")

    new_project = QAction("New Project", window)
    open_project = QAction("Open Project", window)
    exit_action = QAction("Exit", window)

    file_menu.addAction(new_project)
    file_menu.addAction(open_project)
    file_menu.addSeparator()
    file_menu.addAction(exit_action)

    exit_action.triggered.connect(window.close)

    # Project
    menu_bar.addMenu("Project")

    # Backtest
    menu_bar.addMenu("Backtest")

    # Optimizer
    menu_bar.addMenu("Optimizer")

    # Reports
    menu_bar.addMenu("Reports")

    # Settings
    menu_bar.addMenu("Settings")

    # Help
    menu_bar.addMenu("Help")