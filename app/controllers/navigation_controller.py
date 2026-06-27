"""
============================================================
Navigation Controller
============================================================
"""

from PySide6.QtCore import QObject


class NavigationController(QObject):
    """
    Controls page navigation.
    """

    def __init__(self, sidebar, workspace):
        super().__init__()

        self.sidebar = sidebar

        self.workspace = workspace

        self.sidebar.currentRowChanged.connect(
            self.workspace.setCurrentIndex
        )