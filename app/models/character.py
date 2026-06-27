"""
============================================================
AI Studio Pro Enterprise

Character Model
============================================================
"""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class Character:
    """
    Enterprise Character Model.
    """

    # -----------------------------------------------------
    # Database Primary Key
    # -----------------------------------------------------

    id: int | None = None

    # -----------------------------------------------------
    # Character Information
    # -----------------------------------------------------

    name: str = ""

    nickname: str = ""

    personality: str = ""

    description: str = ""

    voice: str = ""

    avatar: str = ""

    tags: str = ""

    # -----------------------------------------------------
    # System Information
    # -----------------------------------------------------

    uuid: str = field(
        default_factory=lambda: str(uuid4())
    )

    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )

    updated_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )

    # -----------------------------------------------------
    # Validation
    # -----------------------------------------------------

    def validate(self):
        """
        Validate character data.
        """

        self.name = self.name.strip()

        self.nickname = self.nickname.strip()

        self.personality = self.personality.strip()

        self.description = self.description.strip()

        self.voice = self.voice.strip()

        self.avatar = self.avatar.strip()

        self.tags = self.tags.strip()

        if not self.name:

            raise ValueError(
                "Character name cannot be empty."
            )

        return True

    # -----------------------------------------------------
    # Touch
    # -----------------------------------------------------

    def touch(self):
        """
        Update modification timestamp.
        """

        self.updated_at = datetime.now().isoformat(
            timespec="seconds"
        )

    # -----------------------------------------------------
    # String Representation
    # -----------------------------------------------------

    def __str__(self):

        return f"{self.name}"

    def __repr__(self):

        return (
            f"Character("
            f"id={self.id}, "
            f"name='{self.name}')"
        )