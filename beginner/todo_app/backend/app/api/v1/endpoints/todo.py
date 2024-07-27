from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.schemas import TodoCreate, TodoUpdate, TodoBase
from app.db.base import get_db
from app.services.todo_service import TodoService
from app.dependencies.get_current_user import get_current_user
from app.db.models import User

router = APIRouter()

todo_service = TodoService()

@router.post("/", response_model=TodoBase, summary="Create a new todo.")
def create_todo_endpoint(todo: TodoCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return todo_service.create(db, todo, user_id=current_user.id)

@router.get("/{todo_id}", response_model=TodoBase, summary="Get a todo by ID.")
def read_todo_endpoint(todo_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_todo = todo_service.get(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    if db_todo.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this todo")
    return db_todo

@router.get("/", response_model=list[TodoBase], summary="Get a list of todos.")
def read_todos_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(TodoBase).filter(TodoBase.user_id == current_user.id).offset(skip).limit(limit).all()

@router.put("/{todo_id}", response_model=TodoBase, summary="Update a todo by ID.")
def update_todo_endpoint(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_todo = todo_service.get(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    if db_todo.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this todo")
    return todo_service.update(db, db_todo, todo)

@router.delete("/{todo_id}", response_model=TodoBase, summary="Delete a todo by ID.")
def delete_todo_endpoint(todo_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_todo = todo_service.get(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    if db_todo.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this todo")
    return todo_service.delete(db, db_todo)
