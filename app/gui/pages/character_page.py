"""
============================================================
AI Studio Pro Enterprise

Module      : Character Page
Purpose     : Character Management Page
Author      : Pritam Kumar
Version     : 0.3.1
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
    QHeaderView,
    QAbstractItemView,
)

from app.gui.table_models.character_table_model import CharacterTableModel


class CharacterPage(QWidget):
    """
    Enterprise Character Management Page.
    """

    def __init__(self):
        super().__init__()

        self.model = CharacterTableModel()

        self.build_ui()

    # ======================================================
    # Build User Interface
    # ======================================================

    def build_ui(self):

        main_layout = QVBoxLayout(self)

        # --------------------------------------------------
        # Header
        # --------------------------------------------------

        header_layout = QHBoxLayout()

        title = QLabel("Characters")

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        self.new_button = QPushButton("➕ New Character")

        self.new_button.setMinimumHeight(35)

        header_layout.addWidget(title)

        header_layout.addStretch()

        header_layout.addWidget(self.new_button)

        # --------------------------------------------------
        # Search Box
        # --------------------------------------------------

        self.search = QLineEdit()

        self.search.setPlaceholderText(
            "🔍 Search characters..."
        )

        self.search.setMinimumHeight(34)

        # --------------------------------------------------
        # Table
        # --------------------------------------------------

        self.table = QTableView()

        self.table.setModel(self.model)

        # Stretch columns
        header = self.table.horizontalHeader()

        header.setSectionResizeMode(
            QHeaderView.Stretch
        )

        header.setStretchLastSection(True)

        # Appearance
        self.table.verticalHeader().setVisible(False)

        self.table.setAlternatingRowColors(True)

        self.table.setShowGrid(False)

        self.table.setSortingEnabled(True)

        self.table.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )

        self.table.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        self.table.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )

        # --------------------------------------------------
        # Footer
        # --------------------------------------------------

        self.status = QLabel()

        self.update_status()

        # --------------------------------------------------
        # Layout
        # --------------------------------------------------

        main_layout.addLayout(header_layout)

        main_layout.addWidget(self.search)

        main_layout.addWidget(self.table)

        main_layout.addWidget(self.status)

    # ======================================================
    # Refresh
    # ======================================================

    def refresh(self):
        """
        Reload data from database.
        """

        self.model.load()

        self.update_status()

    # ======================================================
    # Status
    # ======================================================

    def update_status(self):

        count = self.model.rowCount()

        if count == 1:

            self.status.setText("1 Character")

        else:

            self.status.setText(f"{count} Characters")