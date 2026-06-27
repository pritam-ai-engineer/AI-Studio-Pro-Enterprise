"""
============================================================
AI Studio Pro Enterprise

Database Manager
============================================================
"""

import sqlite3

from app.config.settings import DATABASE_PATH


class DatabaseManager:
    """
    Enterprise SQLite Database Manager.
    """

    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.connection.row_factory = sqlite3.Row

    def cursor(self):
        return self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()