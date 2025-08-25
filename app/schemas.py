from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "created"


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None


class Task(TaskBase):
    id: UUID

    class Config:
        from_attributes = True  # заменяет orm_mode в Pydantic v2
