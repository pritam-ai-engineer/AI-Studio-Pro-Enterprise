"""
Database Models
"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database.database import Base


class Character(Base):

    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)

    name = Column(String, unique=True)

    folder = Column(String)

    personality = Column(String)

    voice = Column(String)

    status = Column(String)