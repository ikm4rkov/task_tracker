from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/api/tasks", tags=["tasks"])


# CREATE
@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)) -> models.Task:
    db_task = models.Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


# READ (list)
@router.get("/", response_model=List[schemas.Task])
def get_tasks(db: Session = Depends(get_db)) -> List[models.Task]:
    return db.query(models.Task).all()


# READ (single)
@router.get("/{task_id}", response_model=schemas.Task)
def get_task(task_id: str, db: Session = Depends(get_db)) -> models.Task:
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# UPDATE
@router.put("/{task_id}", response_model=schemas.Task)
def update_task(
    task_id: str, task_update: schemas.TaskUpdate, db: Session = Depends(get_db)
) -> models.Task:
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    for key, value in task_update.model_dump(exclude_unset=True).items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task


# DELETE
@router.delete("/{task_id}")
def delete_task(task_id: str, db: Session = Depends(get_db)) -> dict[str, bool]:
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return {"ok": True}
