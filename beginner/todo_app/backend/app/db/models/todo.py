from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func

from app.db import Base

class Todo(Base):
    """
    Model to manage tasks

    Fields:
    - id: Primary key, unique identifier for each task.
    - task: Description of the task, must not be null.
    - due_date: The date by which the task should be completed, can be null.
    - created_at: Timestamp when the task was created.
    - updated_at: Timestamp when the task was last updated.
    - is_completed: Status of the task, whether it is completed or not.
    - user_id: Foreign key linking the task to a specific user.
    """

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    task = Column("task", String(length=128), index=True)
    due_date = Column("due_date", DateTime, nullable=True)
    is_completed = Column(Boolean, default=False, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)


    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
