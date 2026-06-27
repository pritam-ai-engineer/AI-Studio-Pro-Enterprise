"""
============================================================
AI Studio Pro Enterprise

Module      : Filter Proxy Model
Purpose     : Live Search Filtering
Author      : Pritam Kumar
Version     : 0.3.4
============================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtCore import QSortFilterProxyModel


class CharacterFilterProxyModel(QSortFilterProxyModel):
    """
    Filter model for Character Table.
    """

    def __init__(self):

        super().__init__()

        self.setFilterCaseSensitivity(Qt.CaseInsensitive)

        self.setFilterKeyColumn(-1)

    def filterAcceptsRow(self, source_row, source_parent):

        if not self.filterRegularExpression().pattern():

            return True

        model = self.sourceModel()

        keyword = self.filterRegularExpression().pattern().lower()

        for column in range(model.columnCount()):

            index = model.index(source_row, column)

            value = str(model.data(index)).lower()

            if keyword in value:

                return True

        return False