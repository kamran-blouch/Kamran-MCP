from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="Task Manager API", description="A simple task management API")

# In-memory database
tasks_db = []
task_id_counter = {"current": 1}


class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    completed: bool = False


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Task Manager API",
        "endpoints": {
            "GET /tasks": "Get all tasks",
            "GET /tasks/{task_id}": "Get a specific task",
            "POST /tasks": "Create a new task",
            "PUT /tasks/{task_id}": "Update a task",
            "DELETE /tasks/{task_id}": "Delete a task"
        }
    }


@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    """Get all tasks"""
    return tasks_db


@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """Get a specific task by ID"""
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    """Create a new task"""
    task_dict = task.dict()
    task_dict["id"] = task_id_counter["current"]
    task_id_counter["current"] += 1
    tasks_db.append(task_dict)
    return task_dict


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: TaskUpdate):
    """Update an existing task"""
    for i, task in enumerate(tasks_db):
        if task["id"] == task_id:
            update_data = task_update.dict(exclude_unset=True)
            tasks_db[i].update(update_data)
            return tasks_db[i]
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    """Delete a task"""
    for i, task in enumerate(tasks_db):
        if task["id"] == task_id:
            deleted_task = tasks_db.pop(i)
            return {"message": "Task deleted successfully", "task": deleted_task}
    raise HTTPException(status_code=404, detail="Task not found")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

