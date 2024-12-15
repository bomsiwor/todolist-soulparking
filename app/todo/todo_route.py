from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from fastapi import APIRouter


class Todo(BaseModel):
    id: str
    title: str
    description: str
    finished_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None


class TodoIn(BaseModel):
    title: str
    description: str


todos: List[Todo] = []

todo_router = APIRouter(prefix="/todo", tags=["todo"])
