"""
============================================================
AI Studio Pro Enterprise

Module      : Menu Bar
Purpose     : Main application menu
Author      : Pritam Kumar
Version     : 0.2.0
============================================================
"""

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar


class MenuBarWidget(QMenuBar):
    """
    Enterprise Menu Bar.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.build_menu()

    def build_menu(self):
        """
        Create application menus.
        """

        # ----------------------------
        # File Menu
        # ----------------------------

        file_menu = self.addMenu("File")

        file_menu.addAction(QAction("New Project", self))
        file_menu.addAction(QAction("Open Project", self))
        file_menu.addSeparator()
        file_menu.addAction(QAction("Exit", self))

        # ----------------------------
        # Edit Menu
        # ----------------------------

        edit_menu = self.addMenu("Edit")

        edit_menu.addAction(QAction("Undo", self))
        edit_menu.addAction(QAction("Redo", self))

        # ----------------------------
        # View Menu
        # ----------------------------

        self.addMenu("View")

        # ----------------------------
        # AI Menu
        # ----------------------------

        self.addMenu("AI")

        # ----------------------------
        # Publish Menu
        # ----------------------------

        self.addMenu("Publish")

        # ----------------------------
        # Help Menu
        # ----------------------------

        self.addMenu("Help")