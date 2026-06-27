"""
============================================================
AI Studio Pro Enterprise

Module      : Character Controller
Purpose     : Coordinate Character Module
Author      : Pritam Kumar
Version     : 0.5.0
============================================================
"""

from app.gui.dialogs.character_dialog import CharacterDialog
from app.services.character_service import CharacterService


class CharacterController:
    """
    Controller for Character Management.
    """

    def __init__(self, page):

        self.page = page

        self.service = CharacterService()

    # -----------------------------------------------------
    # Create Character
    # -----------------------------------------------------

    def new_character(self):

        dialog = CharacterDialog()

        if dialog.exec():

            self.page.refresh()

    # -----------------------------------------------------
    # Edit Character
    # -----------------------------------------------------

    def edit_character(self, character_id):

        character = self.service.get_character(character_id)

        if character is None:

            return

        dialog = CharacterDialog(character)

        if dialog.exec():

            self.page.refresh()

    # -----------------------------------------------------
    # Delete Character
    # -----------------------------------------------------

    def delete_character(self, character_id):

        self.service.delete_character(character_id)

        self.page.refresh()