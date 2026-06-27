import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow

from app.controllers.navigation_controller import NavigationController
from app.gui.ui_builder import UIBuilder


def main():
    app = QApplication(sys.argv)

    window = QMainWindow()

    sidebar, workspace = UIBuilder.build(window)

    NavigationController(sidebar, workspace)

    window.resize(1400, 900)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()