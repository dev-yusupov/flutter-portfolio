from sqlalchemy.orm import Session

from app.db.models import Todo
from app.db.schemas import TodoCreate, TodoUpdate

def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id==todo_id).first()

def get_todos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Todo).offset(skip).limit(limit=limit).all()

def create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh()

    return db_todo

def update_todo(db: Session, db_todo: Todo, todo_update: TodoUpdate):
    for key, value in todo_update.model_dump().items():
        setattr(db_todo, key, value)

    db.commit()
    db.refresh(db_todo)

    return db_todo

def delete_todo(db: Session, db_todo: Todo):
    db.delete(db_todo)
    db.commit()

    return db_todo