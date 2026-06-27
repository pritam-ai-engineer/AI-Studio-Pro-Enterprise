"""
============================================================
Character Repository
============================================================
"""

from app.database.database_manager import DatabaseManager
from app.models.character import Character


class CharacterRepository:
    """
    Character database operations.
    """

    def __init__(self):

        self.db = DatabaseManager()

        self.create_table()

    def create_table(self):

        cursor = self.db.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS characters(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            uuid TEXT UNIQUE,

            name TEXT NOT NULL,

            nickname TEXT,

            personality TEXT,

            description TEXT,

            voice TEXT,

            avatar TEXT,

            tags TEXT,

            created_at TEXT,

            updated_at TEXT

        )
        """)

        self.db.commit()

    def create(self, character: Character):

        character.validate()

        cursor = self.db.cursor()

        cursor.execute("""

        INSERT INTO characters(

            uuid,
            name,
            nickname,
            personality,
            description,
            voice,
            avatar,
            tags,
            created_at,
            updated_at

        )

        VALUES(?,?,?,?,?,?,?,?,?,?)

        """,

        (

            character.uuid,
            character.name,
            character.nickname,
            character.personality,
            character.description,
            character.voice,
            character.avatar,
            character.tags,
            character.created_at,
            character.updated_at

        ))

        self.db.commit()

        return cursor.lastrowid

    def get_all(self):

        cursor = self.db.cursor()

        cursor.execute("""

        SELECT *

        FROM characters

        ORDER BY name

        """)

        return cursor.fetchall()