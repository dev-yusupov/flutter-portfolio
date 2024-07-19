from pydantic import BaseModel

from sqlalchemy import Uuid

class TodoBase(BaseModel):
    title: str
    description: str
    completed: bool = False


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    pass


class TodoInDBBase(TodoBase):
    id: Uuid

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

