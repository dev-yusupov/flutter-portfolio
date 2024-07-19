from sqlalchemy import Column, Integer, String, Boolean, Uuid
from uuid import uuid4

from apps.database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid4, unique=True, nullable=False)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)

