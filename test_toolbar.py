import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow

from app.gui.widgets.toolbar import ToolbarWidget


def main():

    app = QApplication(sys.argv)

    window = QMainWindow()

    toolbar = ToolbarWidget(window)

    window.addToolBar(toolbar)

    window.resize(900, 500)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()