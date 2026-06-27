"""
============================================================
AI Studio Pro Enterprise

Character Page
============================================================
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QTableView,
)


class CharacterPage(QWidget):
    """
    Character Management Page.
    """

    def __init__(self):
        super().__init__()

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)

        # -----------------------------
        # Header
        # -----------------------------

        header = QHBoxLayout()

        title = QLabel("Characters")

        title.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
        """)

        self.new_button = QPushButton("➕ New Character")

        header.addWidget(title)

        header.addStretch()

        header.addWidget(self.new_button)

        # -----------------------------
        # Search
        # -----------------------------

        self.search = QLineEdit()

        self.search.setPlaceholderText(
            "Search characters..."
        )

        # -----------------------------
        # Table
        # -----------------------------

        self.table = QTableView()

        # -----------------------------
        # Footer
        # -----------------------------

        self.status = QLabel("0 Characters")

        layout.addLayout(header)

        layout.addWidget(self.search)

        layout.addWidget(self.table)

        layout.addWidget(self.status)