from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

app.mount("/", StaticFiles(directory="static", html=True), name="static")

tasks = []

class Task(BaseModel):
    task: str

@app.get("/api/tasks")
def get_tasks():
    return tasks

@app.post("/api/tasks")
def add_task(task: Task):
    tasks.append(task.task)
    return tasks  # return updated list

@app.delete("/api/tasks/{index}")
def delete_task(index: int):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        return tasks  # return updated list
    return {"error": "Invalid index"}
