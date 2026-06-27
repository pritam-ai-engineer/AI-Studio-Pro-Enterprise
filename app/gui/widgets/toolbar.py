"""
=========================================================
AI Studio Pro Enterprise

Module      : Toolbar Widget
Author      : Pritam Kumar
Version     : 1.0.0
Description : Professional application toolbar
=========================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QToolBar


class ToolbarWidget(QToolBar):
    """
    Main application toolbar.
    """

    def __init__(self, parent=None):
        super().__init__("Main Toolbar", parent)

        self.setMovable(False)
        self.setFloatable(False)

        self.setToolButtonStyle(
            Qt.ToolButtonTextUnderIcon
        )

        self.build_toolbar()

    def build_toolbar(self):
        """
        Create toolbar buttons.
        """

        actions = [
            "New Project",
            "New Character",
            "New Episode",
            "Generate AI",
            "Publish"
        ]

        for text in actions:
            action = QAction(text, self)
            self.addAction(action)