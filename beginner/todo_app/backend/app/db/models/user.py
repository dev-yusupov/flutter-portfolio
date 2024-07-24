from sqlalchemy import Column, String, Integer

from app.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column('id', Integer, primary_key=True, index=True)
    username = Column("username", String(64), unique=True, index=True)
    password = Column(String)