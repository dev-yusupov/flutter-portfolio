from sqlalchemy import Column, String, Integer, DateTime

from app.db import Base

class Todo(Base):
    """
    Model to manage tasks
    """
    __tablename__ = "todos"
    id = Column("id", Integer, primary_key=True, index=True)
    task = Column("task", String(length=128), index=True)
    due_date = Column("due_date", DateTime)