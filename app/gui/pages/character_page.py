"""
============================================================
AI Studio Pro Enterprise

Module      : Character Page
Purpose     : Enterprise Character Manager
Author      : Pritam Kumar
Version     : 0.4.1
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

from app.controllers.character_controller import CharacterController
from app.gui.table_models.character_table_model import CharacterTableModel


class CharacterPage(QWidget):
    """
    Enterprise Character Manager
    """

    def __init__(self):

        super().__init__()

        self.model = CharacterTableModel()

        self.controller = CharacterController(self)

        self.build_ui()

        self.connect_signals()

    # --------------------------------------------------

    def build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(15, 15, 15, 15)

        layout.setSpacing(12)

        # ==================================================
        # Header
        # ==================================================

        header = QHBoxLayout()

        title = QLabel("Characters")

        title.setStyleSheet("""
            QLabel{
                font-size:30px;
                font-weight:bold;
            }
        """)

        self.new_button = QPushButton("➕ New Character")

        self.new_button.setMinimumHeight(40)

        self.new_button.setMinimumWidth(170)

        header.addWidget(title)

        header.addStretch()

        header.addWidget(self.new_button)

        # ==================================================
        # Search
        # ==================================================

        self.search = QLineEdit()

        self.search.setPlaceholderText("🔍 Search Characters...")

        self.search.setMinimumHeight(38)

        # ==================================================
        # Table
        # ==================================================

        self.table = QTableView()

        self.table.setModel(self.model)

        self.table.setAlternatingRowColors(True)

        self.table.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )

        self.table.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        self.table.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )

        self.table.setShowGrid(False)

        self.table.setSortingEnabled(True)

        self.table.setWordWrap(False)

        self.table.setCornerButtonEnabled(False)

        self.table.verticalHeader().setVisible(False)

        self.table.verticalHeader().setDefaultSectionSize(34)

        header_view = self.table.horizontalHeader()

        header_view.setStretchLastSection(True)

        header_view.setDefaultAlignment(
            self.table.horizontalHeader().defaultAlignment()
        )

        header_view.setSectionResizeMode(
            0,
            QHeaderView.Stretch
        )

        header_view.setSectionResizeMode(
            1,
            QHeaderView.ResizeToContents
        )

        header_view.setSectionResizeMode(
            2,
            QHeaderView.ResizeToContents
        )

        header_view.setSectionResizeMode(
            3,
            QHeaderView.ResizeToContents
        )

        header_view.setSectionResizeMode(
            4,
            QHeaderView.ResizeToContents
        )

        # ==================================================
        # Footer
        # ==================================================

        self.status = QLabel()

        self.status.setStyleSheet("""
            QLabel{
                color:gray;
                font-size:12px;
            }
        """)

        self.update_status()

        # ==================================================

        layout.addLayout(header)

        layout.addWidget(self.search)

        layout.addWidget(self.table)

        layout.addWidget(self.status)

    # --------------------------------------------------

    def connect_signals(self):

        self.new_button.clicked.connect(
            self.controller.new_character
        )

    # --------------------------------------------------

    def refresh(self):

        self.model.load()

        self.update_status()

    # --------------------------------------------------

    def update_status(self):

        count = self.model.rowCount()

        if count == 1:

            self.status.setText("1 Character")

        else:

            self.status.setText(f"{count} Characters")