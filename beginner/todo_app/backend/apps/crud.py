from sqlalchemy.orm import Session
from sqlalchemy import Uuid

from . import models, schemas

def get_todos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Todo).offset(skip).limit(limit).all()

def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)

    return db_todo

def get_todo_by_id(db: Session, todo_id: Uuid):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def update_todo(db: Session, todo_id: Uuid, todo: schemas.TodoUpdate):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()

    if db_todo:
        db_todo.title = todo.title
        db_todo.description = todo.description
        db_todo.completed = todo.completed
        db.commit()
        db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: Uuid):
    db_todo = db.query(models.Todo).get(models.Todo.id == todo_id)
    if db_todo:
        db.delete(db_todo)
        db.refresh()

    return db_todo
