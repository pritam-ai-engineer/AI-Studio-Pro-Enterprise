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

        # -----------------------
        # Clean Data
        # -----------------------

        name = name.strip()

        nickname = nickname.strip()

        personality = personality.strip()

        description = description.strip()

        voice = voice.strip()

        avatar = avatar.strip()

        tags = tags.strip()

        # -----------------------
        # Validation
        # -----------------------

        if not name:

            raise ValueError(
                "Character name is required."
            )

        # -----------------------
        # Create Model
        # -----------------------

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

    def get_all_characters(self):

        return self.repository.get_all()