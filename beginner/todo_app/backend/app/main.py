from fastapi import FastAPI

app = FastAPI(version="1.0.0", debug=True, title="Todo API", description="APIs for Todo App")

@app.get("/")
def read_items():
    return [{"name": "Empanada"}, {"name": "Arepa"}]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
