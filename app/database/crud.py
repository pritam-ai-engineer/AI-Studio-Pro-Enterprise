"""
CRUD Operations
"""

from app.database.database import SessionLocal
from app.database.models import Character


def add_character(name):

    db = SessionLocal()

    character = Character(
        name=name,
        folder=name,
        personality="",
        voice="",
        status="Active"
    )

    db.add(character)

    db.commit()

    db.close()