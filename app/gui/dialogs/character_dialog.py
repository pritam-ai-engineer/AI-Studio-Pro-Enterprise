"""
============================================================
AI Studio Pro Enterprise

Module      : Character Dialog
Purpose     : Create New Character
Author      : Pritam Kumar
Version     : 0.3.2
============================================================
"""

from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QTextEdit,
    QMessageBox,
)

from app.gui.dialogs.base_dialog import BaseDialog
from app.services.character_service import CharacterService


class CharacterDialog(BaseDialog):
    """
    Dialog for creating a new character.
    """

    def __init__(self):

        super().__init__("New Character")

        self.service = CharacterService()

        self.build_form()

        self.save_button.clicked.connect(self.save_character)

    # ---------------------------------------------------------
    # Build Form
    # ---------------------------------------------------------

    def build_form(self):

        # Name

        self.content_layout.addWidget(QLabel("Name *"))

        self.name = QLineEdit()

        self.content_layout.addWidget(self.name)

        # Nickname

        self.content_layout.addWidget(QLabel("Nickname"))

        self.nickname = QLineEdit()

        self.content_layout.addWidget(self.nickname)

        # Personality

        self.content_layout.addWidget(QLabel("Personality"))

        self.personality = QLineEdit()

        self.content_layout.addWidget(self.personality)

        # Voice

        self.content_layout.addWidget(QLabel("Voice"))

        self.voice = QLineEdit()

        self.content_layout.addWidget(self.voice)

        # Tags

        self.content_layout.addWidget(QLabel("Tags"))

        self.tags = QLineEdit()

        self.content_layout.addWidget(self.tags)

        # Description

        self.content_layout.addWidget(QLabel("Description"))

        self.description = QTextEdit()

        self.description.setMinimumHeight(120)

        self.content_layout.addWidget(self.description)

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

    def save_character(self):

        try:

            self.service.create_character(

                name=self.name.text(),

                nickname=self.nickname.text(),

                personality=self.personality.text(),

                description=self.description.toPlainText(),

                voice=self.voice.text(),

                tags=self.tags.text(),

            )

            QMessageBox.information(

                self,

                "Success",

                "Character saved successfully."

            )

            self.accept()

        except Exception as error:

            QMessageBox.warning(

                self,

                "Error",

                str(error)

            )