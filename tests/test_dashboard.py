import sys
from PySide6.QtWidgets import QApplication

from app.gui.pages.dashboard_page import DashboardPage


def main():
    app = QApplication(sys.argv)

    page = DashboardPage()

    page.resize(900, 600)

    page.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()