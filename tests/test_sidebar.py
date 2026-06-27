import sys

from PySide6.QtWidgets import QApplication

from app.gui.widgets.sidebar import SidebarWidget


def main():

    app = QApplication(sys.argv)

    sidebar = SidebarWidget()

    sidebar.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()