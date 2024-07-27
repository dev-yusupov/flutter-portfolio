from sqlalchemy.orm import Session
from app.db.models import Todo
from app.db.schemas import TodoCreate, TodoUpdate
from app.dependencies.get_current_user import get_current_user

class TodoService:
    def get(self, db: Session, todo_id: int):
        return db.query(Todo).filter(Todo.id == todo_id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(Todo).offset(skip).limit(limit).all()

    def create(self, db: Session, todo: TodoCreate, user_id: int):
        db_todo = Todo(**todo.model_dump(), user_id=user_id)
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo

    def update(self, db: Session, db_todo: Todo, todo_update: TodoUpdate):
        for key, value in todo_update.model_dump().items():
            setattr(db_todo, key, value)
        db.commit()
        db.refresh(db_todo)
        return db_todo

    def delete(self, db: Session, db_todo: Todo):
        db.delete(db_todo)
        db.commit()
        return db_todo
