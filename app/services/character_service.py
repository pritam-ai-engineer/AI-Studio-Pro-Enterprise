"""
============================================================
AI Studio Pro Enterprise

Character Service
============================================================
"""

from app.database.character_repository import CharacterRepository
from app.models.character import Character


class CharacterService:
    """
    Character business logic.
    """

    def __init__(self):

        self.repository = CharacterRepository()

    # -----------------------------------------------------
    # Create Character
    # -----------------------------------------------------

    def create_character(
        self,
        name,
        nickname="",
        personality="",
        description="",
        voice="",
        avatar="",
        tags=""
    ):

        name = name.strip()
        nickname = nickname.strip()
        personality = personality.strip()
        description = description.strip()
        voice = voice.strip()
        avatar = avatar.strip()
        tags = tags.strip()

        if not name:

            raise ValueError(
                "Character name is required."
            )

        character = Character(

            name=name,

            nickname=nickname,

            personality=personality,

            description=description,

            voice=voice,

            avatar=avatar,

            tags=tags

        )

        return self.repository.create(character)

    # -----------------------------------------------------
    # Get All Characters
    # -----------------------------------------------------

    def get_all_characters(self):

        return self.repository.get_all()

    # -----------------------------------------------------
    # Get Character
    # -----------------------------------------------------

    def get_character(self, character_id):

        return self.repository.get_by_id(character_id)

    # -----------------------------------------------------
    # Update Character
    # -----------------------------------------------------

    def update_character(
        self,
        character_id,
        name,
        nickname="",
        personality="",
        description="",
        voice="",
        avatar="",
        tags=""
    ):

        name = name.strip()
        nickname = nickname.strip()
        personality = personality.strip()
        description = description.strip()
        voice = voice.strip()
        avatar = avatar.strip()
        tags = tags.strip()

        if not name:

            raise ValueError(
                "Character name is required."
            )

        character = Character(

            id=character_id,

            name=name,

            nickname=nickname,

            personality=personality,

            description=description,

            voice=voice,

            avatar=avatar,

            tags=tags

        )

        return self.repository.update(character)

    # -----------------------------------------------------
    # Delete Character
    # -----------------------------------------------------

    def delete_character(self, character_id):

        return self.repository.delete(character_id)