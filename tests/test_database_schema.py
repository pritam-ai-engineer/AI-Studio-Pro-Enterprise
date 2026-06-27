import sqlite3

from app.config.settings import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()

cursor.execute("PRAGMA table_info(characters)")

print("\nCurrent Character Table\n")

for column in cursor.fetchall():
    print(column)

connection.close()