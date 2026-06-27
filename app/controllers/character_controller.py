"""
============================================================
AI Studio Pro Enterprise

Module      : Character Controller
Purpose     : Coordinate Character Module
Author      : Pritam Kumar
Version     : 0.4.0
============================================================
"""

from app.gui.dialogs.character_dialog import CharacterDialog


class CharacterController:
    """
    Controller for Character Management.
    """

    def __init__(self, page):

        self.page = page

    # -----------------------------------------------------

    def new_character(self):

        dialog = CharacterDialog()

        if dialog.exec():

            self.page.refresh()