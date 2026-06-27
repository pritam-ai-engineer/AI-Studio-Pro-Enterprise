"""
Base page for all application pages.
"""

from PySide6.QtWidgets import QWidget


class BasePage(QWidget):
    """
    Parent class for all pages.
    """

    PAGE_TITLE = "Base Page"

    def __init__(self):
        super().__init__()