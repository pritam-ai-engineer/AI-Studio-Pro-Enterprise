"""
============================================================
AI Studio Pro Enterprise

Module      : Application Entry Point
Purpose     : Launch AI Studio Pro Enterprise
Author      : Pritam Kumar
Version     : 0.2.0-beta
============================================================
"""

import sys

from PySide6.QtWidgets import QApplication

from app.gui.main_window import MainWindow
from app.gui.styles.theme_manager import ThemeManager


def main():
    """
    Application entry point.
    """

    app = QApplication(sys.argv)

    # Apply default theme
    ThemeManager.apply_light(app)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()