from fastapi import APIRouter

from .endpoints import auth, todo

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(todo.router, prefix="/todo", tags=["todo"])