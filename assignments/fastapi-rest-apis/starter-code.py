from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API")

# In-memory storage for tasks
tasks = [
    {"id": 1, "title": "Write report", "done": False},
]


class TaskCreate(BaseModel):
    title: str
    done: bool = False


class Task(TaskCreate):
    id: int


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks")
def list_tasks():
    return tasks


# TODO: Add POST /tasks
# TODO: Add GET /tasks/{task_id}
# TODO: Add PUT or PATCH /tasks/{task_id}
# TODO: Add DELETE /tasks/{task_id}
