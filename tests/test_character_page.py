import sys

from PySide6.QtWidgets import QApplication

from app.gui.pages.character_page import CharacterPage


def main():

    app = QApplication(sys.argv)

    page = CharacterPage()

    page.resize(1200, 700)

    page.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()