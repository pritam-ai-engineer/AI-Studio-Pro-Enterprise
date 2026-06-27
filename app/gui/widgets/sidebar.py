"""
=========================================================
AI Studio Pro Enterprise
Sidebar Widget

Author : Pritam Kumar
Architecture : Enterprise
Version : 1.0
=========================================================
"""

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QListWidget
from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtWidgets import QSizePolicy


class SidebarWidget(QListWidget):
    """
    Enterprise Sidebar Navigation
    """

    page_selected = Signal(str)

    def __init__(self):
        super().__init__()

        self.setMinimumWidth(220)
        self.setMaximumWidth(250)

        self.setSizePolicy(
            QSizePolicy.Fixed,
            QSizePolicy.Expanding
        )

        self.build_sidebar()

        self.currentTextChanged.connect(self.page_selected.emit)

    def build_sidebar(self):
        """
        Build navigation items
        """

        pages = [
            "🏠 Dashboard",
            "👤 Characters",
            "🎬 Episodes",
            "💬 Prompts",
            "🖼 Assets",
            "🤖 AI Tools",
            "📊 Analytics",
            "⚙ Settings"
        ]

        for page in pages:
            self.addItem(QListWidgetItem(page))

        self.setCurrentRow(0)