"""
============================================================
AI Studio Pro Enterprise

Module      : Main Window
Purpose     : Enterprise Application Shell
Author      : Pritam Kumar
Version     : 0.2.0
============================================================
"""

import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
)

from app.config.settings import (
    WINDOW_TITLE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)

from app.gui.widgets.menu_bar import MenuBarWidget


class MainWindow(QMainWindow):
    """
    Enterprise Main Window.

    Responsible only for assembling UI components.
    """

    def __init__(self):
        super().__init__()

        self.configure_window()
        self.build_ui()
        self.create_menu()
        self.create_connections()

    # -------------------------------------------------

    def configure_window(self):
        """
        Configure application window.
        """

        self.setWindowTitle(WINDOW_TITLE)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

    # -------------------------------------------------

    def build_ui(self):
        """
        Build the central widget.
        """

        central_widget = QWidget()

        self.setCentralWidget(central_widget)

        self.main_layout = QVBoxLayout()

        central_widget.setLayout(self.main_layout)

    # -------------------------------------------------

    def create_menu(self):
        """
        Create application menu bar.
        """

        self.menu_bar = MenuBarWidget(self)

        self.setMenuBar(self.menu_bar)

    # -------------------------------------------------

    def create_connections(self):
        """
        Placeholder for future signal-slot connections.
        """

        pass


# =========================================================
# Application Entry
# =========================================================

def main():
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()