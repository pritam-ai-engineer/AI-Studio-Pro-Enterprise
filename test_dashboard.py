import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow

from app.gui.pages.dashboard_page import DashboardPage


def main():

    app = QApplication(sys.argv)

    window = QMainWindow()

    dashboard = DashboardPage()

    window.setCentralWidget(dashboard)

    window.resize(1200, 700)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()