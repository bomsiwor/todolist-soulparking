from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from fastapi import APIRouter, Response
from ulid import ULID
from core.helper.responses import ErrorResponse, ResponseModel, SuccessResponse


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


@todo_router.get(
    "/{todo_id}",
    status_code=200,
    summary="Get Todo by ID",
    description="Get single Todo by given ID",
    response_model=ResponseModel[Todo | None],
)
def get_single_by_id(todo_id: str, response: Response):
    for todo in todos:
        if todo.id == todo_id:
            return SuccessResponse[Todo](data=todo)

    response.status_code = 404
    return ErrorResponse[None](message="Todo Not found", code=404, data=None)


@todo_router.post("/", response_model=ResponseModel[Todo], status_code=201)
def create(todo_data: TodoIn):
    todo_id = ULID().__str__()
    todo = Todo(
        id=todo_id,
        title=todo_data.title,
        description=todo_data.description,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    todos.append(todo)

    return SuccessResponse[Todo](code=201, data=todo, message="New Todo created!")


@todo_router.put(
    "/{todo_id}",
    status_code=200,
    summary="Update Todo by ID",
    description="Update todo data by given ID",
    response_model=ResponseModel[Todo | None],
)
def update_by_id(todo_id: str, todo_data: TodoIn, response: Response):
    for todo in todos:
        if todo.id == todo_id:
            # Update data if todo is found by ID
            todo.updated_at = datetime.now()
            todo.title = todo_data.title
            todo.description = todo_data.description

            return SuccessResponse[Todo](data=todo, message="Todo updated!")

    # Return 404 message if given ID is not found in list
    response.status_code = 404
    return ErrorResponse[None](message="Todo Not found", code=404, data=None)
