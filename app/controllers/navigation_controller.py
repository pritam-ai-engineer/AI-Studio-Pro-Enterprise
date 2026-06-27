"""
============================================================
AI Studio Pro Enterprise

Module      : Navigation Controller
Purpose     : Handles page navigation
Author      : Pritam Kumar
Version     : 0.2.0-alpha
============================================================
"""

from PySide6.QtCore import QObject


class NavigationController(QObject):
    """
    Handles navigation between pages.
    """

    def __init__(self, stacked_widget):
        super().__init__()

        self.stacked_widget = stacked_widget

    def show_page(self, index: int):
        """
        Display page by index.
        """
        self.stacked_widget.setCurrentIndex(index)