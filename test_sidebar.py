import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow

from app.gui.widgets.sidebar import SidebarWidget

app = QApplication(sys.argv)

window = QMainWindow()

sidebar = SidebarWidget()

window.setCentralWidget(sidebar)

window.resize(300, 600)

window.show()

app.exec()