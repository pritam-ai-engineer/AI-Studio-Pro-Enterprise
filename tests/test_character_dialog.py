import sys

from PySide6.QtWidgets import QApplication

from app.gui.dialogs.character_dialog import CharacterDialog


def main():

    app = QApplication(sys.argv)

    dialog = CharacterDialog()

    dialog.exec()


if __name__ == "__main__":
    main()