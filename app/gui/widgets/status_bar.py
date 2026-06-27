"""
============================================================
AI Studio Pro Enterprise

Enterprise Status Bar
============================================================
"""

from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QStatusBar


class StatusBarWidget(QStatusBar):
    """
    Enterprise Status Bar.
    """

    def __init__(self):

        super().__init__()

        self.initialize()

    def initialize(self):

        self.database_label = QLabel("🟢 SQLite Connected")

        self.git_label = QLabel("🌿 Git Ready")

        self.ai_label = QLabel("🤖 AI Idle")

        self.version_label = QLabel("v0.2.0-alpha")

        self.addWidget(self.database_label)

        self.addPermanentWidget(self.git_label)

        self.addPermanentWidget(self.ai_label)

        self.addPermanentWidget(self.version_label)