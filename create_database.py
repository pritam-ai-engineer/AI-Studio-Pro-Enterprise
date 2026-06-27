"""
============================================================
AI Studio Pro Enterprise

Module      : Database Creator
Purpose     : Create Enterprise SQLite Database
Author      : Pritam Kumar
Version     : 0.3.0
============================================================
"""

import sqlite3

from app.config.settings import DATABASE_PATH


def create_database():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
    DROP TABLE IF EXISTS characters
    """)

    cursor.execute("""
    CREATE TABLE characters(

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

    connection.commit()

    connection.close()

    print("Enterprise Database Created Successfully.")


if __name__ == "__main__":

    create_database()