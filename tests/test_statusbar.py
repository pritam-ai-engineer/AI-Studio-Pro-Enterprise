import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow

from app.gui.widgets.status_bar import StatusBarWidget


def main():

    app = QApplication(sys.argv)

    window = QMainWindow()

    status = StatusBarWidget()

    window.setStatusBar(status)

    window.resize(900, 600)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()