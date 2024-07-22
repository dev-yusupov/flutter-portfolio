from fastapi import FastAPI

from app.db import models, engine, Base
from app.api.v1 import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(version="1.0.1", debug=True, title="Todo API from dev-yusupov", description="APIs for Todo App")

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {
        "message": "Welcome to ToDo API v1"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, host="0.0.0.0", port=8000, reload=True, log_level="info")