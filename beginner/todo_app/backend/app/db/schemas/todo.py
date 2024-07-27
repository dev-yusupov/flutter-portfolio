from typing import Optional
from datetime import datetime

from pydantic import BaseModel

class TodoBase(BaseModel):
    task: str
    due_date: Optional[datetime] = None
    is_completed: Optional[bool] = False


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    pass


class TodoInDBBase(TodoBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Todo(TodoInDBBase):
    pass