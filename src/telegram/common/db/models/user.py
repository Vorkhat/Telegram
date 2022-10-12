from src.telegram.common.db.base import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    state = Column(String)
    position = Column(String)
