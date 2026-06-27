import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow

from app.gui.widgets.menu_bar import MenuBarWidget


def main():

    app = QApplication(sys.argv)

    window = QMainWindow()

    menu = MenuBarWidget(window)

    window.setMenuBar(menu)

    window.resize(900, 600)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()