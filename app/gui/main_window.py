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


class MainWindow(QMainWindow):
    """
    Enterprise Main Window.
    Responsible only for assembling UI components.
    """

    def __init__(self):
        super().__init__()

        self.configure_window()

        self.build_ui()

        self.create_connections()

    # -----------------------------------------------------

    def configure_window(self):
        """
        Configure application window.
        """

        self.setWindowTitle(WINDOW_TITLE)

        self.resize(
            WINDOW_WIDTH,
            WINDOW_HEIGHT,
        )

    # -----------------------------------------------------

    def build_ui(self):
        """
        Build main layout.
        """

        central = QWidget()

        self.setCentralWidget(central)

        self.main_layout = QVBoxLayout()

        central.setLayout(self.main_layout)

    # -----------------------------------------------------

    def create_connections(self):
        """
        Placeholder for signal-slot connections.
        """

        pass


# ---------------------------------------------------------


def main():

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())