"""
AI Studio Pro Enterprise
Main Window
"""

import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from app.config.settings import APP_NAME
from app.config.settings import WINDOW_HEIGHT
from app.config.settings import WINDOW_WIDTH
from app.config.settings import WINDOW_TITLE


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(WINDOW_TITLE)

        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        central = QWidget()

        self.setCentralWidget(central)

        layout = QVBoxLayout()

        central.setLayout(layout)

        title = QLabel(APP_NAME)

        title.setStyleSheet("""
            font-size:32px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        version = QLabel("Enterprise Edition v1.0")

        layout.addWidget(version)

        status = QLabel("System Ready")

        layout.addWidget(status)


def main():

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())