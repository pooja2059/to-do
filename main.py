from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

# Serve static files
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# In-memory task list
tasks = []

class Task(BaseModel):
    task: str

@app.get("/api/tasks")
def get_tasks():
    return tasks

@app.post("/api/tasks")
def add_task(task: Task):
    tasks.append(task.task)
    return {"message": "Task added"}

@app.delete("/api/tasks/{index}")
def delete_task(index: int):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        return {"message": "Task deleted"}
    return {"error": "Invalid index"}
