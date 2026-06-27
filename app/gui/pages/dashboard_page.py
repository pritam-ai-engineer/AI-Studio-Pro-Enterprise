"""
============================================================
Dashboard Page
============================================================
"""

from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout

from app.gui.pages.base_page import BasePage


class DashboardPage(BasePage):

    PAGE_TITLE = "Dashboard"

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("AI Studio Pro Enterprise")

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        layout.addWidget(
            QLabel("Welcome to AI Studio Pro Enterprise")
        )

        layout.addStretch()

        self.setLayout(layout)