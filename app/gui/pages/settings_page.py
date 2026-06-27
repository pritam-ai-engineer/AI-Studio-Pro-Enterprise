"""
AI Studio Pro Enterprise
Character Page
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class CharacterPage(QWidget):
    """Character management page."""

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Settings")

        font = QFont()
        font.setPointSize(20)
        font.setBold(True)

        title.setFont(font)
        title.setAlignment(Qt.AlignCenter)

        layout.addStretch()
        layout.addWidget(title)
        layout.addStretch()