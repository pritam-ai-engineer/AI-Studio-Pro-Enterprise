"""
============================================================
AI Studio Pro Enterprise

Module      : Character Table Model
Purpose     : Enterprise Character Table Model
Author      : Pritam Kumar
Version     : 0.4.1
============================================================
"""

from PySide6.QtCore import Qt, QAbstractTableModel

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

    # -------------------------------------------------

    def load(self):

        self.beginResetModel()

        self.characters = self.service.get_all_characters()

        self.endResetModel()

    # -------------------------------------------------

    def rowCount(self, parent=None):

        return len(self.characters)

    # -------------------------------------------------

    def columnCount(self, parent=None):

        return len(self.HEADERS)

    # -------------------------------------------------

    def headerData(self, section, orientation, role):

        if orientation == Qt.Horizontal:

            if role == Qt.DisplayRole:
                return self.HEADERS[section]

            if role == Qt.TextAlignmentRole:
                return Qt.AlignLeft | Qt.AlignVCenter

        if orientation == Qt.Vertical:

            if role == Qt.DisplayRole:
                return str(section + 1)

        return None

    # -------------------------------------------------

    def data(self, index, role):

        if not index.isValid():
            return None

        row = self.characters[index.row()]
        column = index.column()

        if role == Qt.DisplayRole:

            if column == 0:
                return row.get("name", "")

            elif column == 1:
                return row.get("personality", "")

            elif column == 2:
                return row.get("voice", "")

            elif column == 3:
                return row.get("tags", "")

            elif column == 4:
                return row.get("created_at", "")

        if role == Qt.TextAlignmentRole:
            return Qt.AlignLeft | Qt.AlignVCenter

        return None

    # -------------------------------------------------

    def refresh(self):
        """
        Reload data from database.
        """
        self.load()