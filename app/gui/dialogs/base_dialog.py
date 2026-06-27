"""
============================================================
AI Studio Pro Enterprise

Module      : Base Dialog
Purpose     : Enterprise Dialog Base Class
Author      : Pritam Kumar
Version     : 0.3.2
============================================================
"""

from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
)


class BaseDialog(QDialog):
    """
    Base dialog used by all dialogs in the application.
    """

    def __init__(self, title="Dialog"):

        super().__init__()

        self.setWindowTitle(title)

        self.resize(650, 500)

        self.main_layout = QVBoxLayout(self)

        self.content_layout = QVBoxLayout()

        self.main_layout.addLayout(self.content_layout)

        self.create_buttons()

    def create_buttons(self):

        layout = QHBoxLayout()

        layout.addStretch()

        self.save_button = QPushButton("💾 Save")

        self.cancel_button = QPushButton("Cancel")

        layout.addWidget(self.save_button)

        layout.addWidget(self.cancel_button)

        self.main_layout.addLayout(layout)

        self.cancel_button.clicked.connect(self.reject)