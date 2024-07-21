from fastapi import FastAPI

from app.db import models, engine, Base
from app.api.v1 import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(version="1.0.0", debug=True, title="Todo API", description="APIs for Todo App")

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {
        "message": "Welcome to ToDo API"
    }
