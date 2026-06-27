"""
============================================================
AI Studio Pro Enterprise

Module      : Toolbar
Purpose     : Enterprise Toolbar
Author      : Pritam Kumar
Version     : 0.2.0
============================================================
"""

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QToolBar


class ToolbarWidget(QToolBar):
    """
    Enterprise Toolbar.
    """

    def __init__(self, parent=None):
        super().__init__("Main Toolbar", parent)

        self.build_toolbar()

    def build_toolbar(self):

        self.addAction(QAction("🆕 New Project", self))

        self.addSeparator()

        self.addAction(QAction("👤 Character", self))

        self.addSeparator()

        self.addAction(QAction("🎬 Episode", self))

        self.addSeparator()

        self.addAction(QAction("🤖 Generate AI", self))

        self.addSeparator()

        self.addAction(QAction("🚀 Publish", self))