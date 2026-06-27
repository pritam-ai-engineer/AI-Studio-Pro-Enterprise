"""
=========================================================
AI Studio Pro Enterprise

Module      : Status Bar
Author      : Pritam Kumar
Version     : 1.0.0
=========================================================
"""

from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QStatusBar


class StatusBarWidget(QStatusBar):
    """
    Enterprise Status Bar
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.build_statusbar()

    def build_statusbar(self):

        self.dbLabel = QLabel("🟢 SQLite Connected")

        self.gitLabel = QLabel("🟢 Git Connected")

        self.aiLabel = QLabel("🟡 AI Idle")

        self.versionLabel = QLabel("Version 1.0")

        self.addWidget(self.dbLabel)

        self.addPermanentWidget(self.gitLabel)

        self.addPermanentWidget(self.aiLabel)

        self.addPermanentWidget(self.versionLabel)