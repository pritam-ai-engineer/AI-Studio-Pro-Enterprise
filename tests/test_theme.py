import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QLabel

from app.gui.styles.theme_manager import ThemeManager


def main():

    app = QApplication(sys.argv)

    ThemeManager.apply_dark(app)

    label = QLabel("Dark Theme Working")

    label.resize(500, 120)

    label.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()