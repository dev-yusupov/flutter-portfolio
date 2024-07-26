from pydantic import BaseModel

class TodoBase(BaseModel):
    task: str
    