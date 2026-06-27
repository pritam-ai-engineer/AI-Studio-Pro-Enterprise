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

    name: str

    nickname: str = ""

    personality: str = ""

    description: str = ""

    voice: str = ""

    avatar: str = ""

    tags: str = ""

    uuid: str = field(default_factory=lambda: str(uuid4()))

    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )

    updated_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )

    def validate(self):
        """
        Validate required fields.
        """

        if not self.name.strip():
            raise ValueError("Character name cannot be empty.")

        return True