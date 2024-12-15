from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from fastapi import APIRouter

from core.helper.responses import ResponseModel, SuccessResponse


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


@todo_router.get("/", summary="Get all To Do", response_model=ResponseModel[List[Todo]])
def get_all():
    result = [todo for todo in todos if not todo.deleted_at]

    return SuccessResponse(data=result)
