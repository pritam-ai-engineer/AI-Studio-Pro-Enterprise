"""
============================================================
AI Studio Pro Enterprise

Workspace
============================================================
"""

from PySide6.QtWidgets import QStackedWidget

from app.gui.pages.dashboard_page import DashboardPage


class Workspace(QStackedWidget):
    """
    Enterprise Workspace.
    Holds all application pages.
    """

    def __init__(self):
        super().__init__()

        self.dashboard_page = DashboardPage()

        self.addWidget(self.dashboard_page)

        self.setCurrentWidget(self.dashboard_page)