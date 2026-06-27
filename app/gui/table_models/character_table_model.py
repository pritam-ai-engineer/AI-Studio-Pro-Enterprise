"""
============================================================
AI Studio Pro Enterprise

Module      : Character Table Model
Purpose     : Display Characters inside QTableView
Author      : Pritam Kumar
Version     : 0.3.0
============================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtCore import QAbstractTableModel

from app.services.character_service import CharacterService


class CharacterTableModel(QAbstractTableModel):
    """
    Enterprise Character Table Model.
    """

    HEADERS = [
        "Name",
        "Personality",
        "Voice",
        "Tags",
        "Created"
    ]

    def __init__(self):

        super().__init__()

        self.service = CharacterService()

        self.characters = []

        self.load()

    # --------------------------------------------------

    def load(self):

        self.beginResetModel()

        self.characters = self.service.get_all_characters()

        self.endResetModel()

    # --------------------------------------------------

    def rowCount(self, parent=None):

        return len(self.characters)

    # --------------------------------------------------

    def columnCount(self, parent=None):

        return len(self.HEADERS)

    # --------------------------------------------------

    def headerData(
        self,
        section,
        orientation,
        role
    ):

        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:

            return self.HEADERS[section]

        return str(section + 1)

    # --------------------------------------------------

    def data(
        self,
        index,
        role
    ):

        if not index.isValid():

            return None

        if role != Qt.DisplayRole:

            return None

        row = self.characters[index.row()]

        column = index.column()

        if column == 0:
            return row["name"]

        elif column == 1:
            return row["personality"]

        elif column == 2:
            return row["voice"]

        elif column == 3:
            return row["tags"]

        elif column == 4:
            return row["created_at"]

        return None