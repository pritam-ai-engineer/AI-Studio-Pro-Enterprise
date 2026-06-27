import sys

from PySide6.QtWidgets import QApplication

from app.gui.workspace import Workspace


app = QApplication(sys.argv)

workspace = Workspace()

workspace.show()

app.exec()