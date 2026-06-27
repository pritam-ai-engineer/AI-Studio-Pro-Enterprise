import sys

from PySide6.QtWidgets import QApplication

from app.gui.dialogs.base_dialog import BaseDialog


def main():

    app = QApplication(sys.argv)

    dialog = BaseDialog("Enterprise Base Dialog")

    dialog.exec()


if __name__ == "__main__":

    main()