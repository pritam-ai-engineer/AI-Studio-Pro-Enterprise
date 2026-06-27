"""
============================================================
AI Studio Pro Enterprise

Workspace
============================================================
"""

from PySide6.QtWidgets import QStackedWidget


class Workspace(QStackedWidget):
    """
    Enterprise Workspace.

    Holds all application pages.
    """

    def __init__(self):

        super().__init__()

        self.initialize()

    def initialize(self):
        """
        Initialize workspace.
        """

        pass