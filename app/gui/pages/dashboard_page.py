"""
=========================================================
AI Studio Pro Enterprise

Module      : Dashboard Page
Author      : Pritam Kumar
Version     : 1.0.0
=========================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QListWidget,
)


class DashboardPage(QWidget):
    """
    Enterprise Dashboard
    """

    def __init__(self):
        super().__init__()

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)

        # ------------------------
        # Title
        # ------------------------

        title = QLabel("AI Studio Pro Enterprise")

        font = QFont()

        font.setPointSize(20)

        font.setBold(True)

        title.setFont(font)

        title.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)

        layout.addSpacing(20)

        # ------------------------
        # KPI Cards
        # ------------------------

        cards = QHBoxLayout()

        cards.addWidget(self.create_card("Characters", "1"))

        cards.addWidget(self.create_card("Episodes", "0"))

        cards.addWidget(self.create_card("Prompts", "0"))

        cards.addWidget(self.create_card("Assets", "0"))

        layout.addLayout(cards)

        layout.addSpacing(30)

        # ------------------------
        # Recent Activity
        # ------------------------

        activity_title = QLabel("Recent Activity")

        activity_title.setFont(QFont("Segoe UI", 12))

        layout.addWidget(activity_title)

        activity = QListWidget()

        activity.addItem("✔ System Started")

        activity.addItem("✔ SQLite Connected")

        activity.addItem("✔ Git Connected")

        activity.addItem("✔ Ready to Create Projects")

        layout.addWidget(activity)

    def create_card(self, title, value):

        frame = QFrame()

        frame.setFrameShape(QFrame.StyledPanel)

        vbox = QVBoxLayout(frame)

        lbl_title = QLabel(title)

        lbl_title.setAlignment(Qt.AlignCenter)

        lbl_value = QLabel(value)

        font = QFont()

        font.setPointSize(22)

        font.setBold(True)

        lbl_value.setFont(font)

        lbl_value.setAlignment(Qt.AlignCenter)

        vbox.addWidget(lbl_title)

        vbox.addWidget(lbl_value)

        return frame