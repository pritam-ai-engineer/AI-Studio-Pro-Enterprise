"""
============================================================
AI Studio Pro Enterprise

Enterprise Sidebar
============================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidget
from PySide6.QtWidgets import QListWidgetItem


class SidebarWidget(QListWidget):

    def __init__(self):

        super().__init__()

        self.initialize()

    def initialize(self):

        self.setMinimumWidth(220)

        self.setMaximumWidth(260)

        self.setAlternatingRowColors(True)

        self.setSelectionMode(
            QListWidget.SingleSelection
        )

        self.add_pages()

    def add_pages(self):

        pages = [

            "🏠 Dashboard",

            "👤 Characters",

            "🎬 Episodes",

            "📝 Prompts",

            "🖼 Assets",

            "📊 Analytics",

            "⚙ Settings"

        ]

        for page in pages:

            self.addItem(
                QListWidgetItem(page)
            )

        self.setCurrentRow(0)