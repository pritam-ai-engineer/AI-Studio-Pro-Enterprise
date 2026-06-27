"""
=========================================================
AI Studio Pro Enterprise

Module      : Main Window
Author      : Pritam Kumar
Version     : 1.0.0

Description :
Main application window.
Responsible only for assembling the UI.
No business logic belongs here.
=========================================================
"""

import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QWidget,
    QVBoxLayout,
)

from app.config.settings import (
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    WINDOW_WIDTH,
)


class MainWindow(QMainWindow):
    """
    Main application window.
    """

    def __init__(self):
        super().__init__()

        self.configure_window()

        self.build_ui()

    def configure_window(self):
        """
        Configure the main application window.
        """

        self.setWindowTitle(WINDOW_TITLE)

        self.resize(
            WINDOW_WIDTH,
            WINDOW_HEIGHT,
        )

    def build_ui(self):
        """
        Build the initial UI.
        """

        central = QWidget()

        self.setCentralWidget(central)

        layout = QVBoxLayout()

        central.setLayout(layout)

        title = QLabel("AI Studio Pro Enterprise")

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        info = QLabel(
            "Application Shell Loading..."
        )

        layout.addWidget(info)


def main():
    """
    Application entry point.
    """

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())