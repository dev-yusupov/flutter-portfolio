from fastapi import APIRouter

router = APIRouter()

@router.get("/todo/")
def get_todo():
    return {
        "todo": "Todo"
    }