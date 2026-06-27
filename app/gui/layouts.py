"""
============================================================
Application Layouts
============================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSplitter


class MainSplitter(QSplitter):
    """
    Main application splitter.
    """

    def __init__(self):
        super().__init__(Qt.Horizontal)

        self.setChildrenCollapsible(False)

        self.setStretchFactor(0, 1)

        self.setStretchFactor(1, 5)