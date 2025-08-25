from typing import List, Optional

from sqlalchemy.orm import Session

from app import models, schemas


def create_task(db: Session, task: schemas.TaskCreate) -> models.Task:
    db_task = models.Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_task(db: Session, task_id: str) -> Optional[models.Task]:
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_tasks(db: Session) -> List[models.Task]:
    return db.query(models.Task).all()


def update_task(db: Session, task_id: str, updates: schemas.TaskUpdate) -> Optional[models.Task]:
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        return None

    if updates.title is not None:
        db_task.title = updates.title
    if updates.description is not None:
        db_task.description = updates.description
    if updates.status is not None:
        db_task.status = updates.status

    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: str) -> bool:
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        return False
    db.delete(db_task)
    db.commit()
    return True
