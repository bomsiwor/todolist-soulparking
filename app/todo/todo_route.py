from typing import List
from fastapi import APIRouter, Response
from app.todo.entity.todo_entity import Todo, TodoIn, todos
from app.todo.repository.todo_repository import TodoRepository
from app.todo.usecase.todo_usecase import TodoUsecase
from core.helper.responses import ErrorResponse, ResponseModel, SuccessResponse

# Create instance of controller / usecase by injecting dependencies
todo_repo = TodoRepository(todos)
todo_usecase = TodoUsecase(todo_repo)

# Create instance of todo router
todo_router = APIRouter(prefix="/todos", tags=["todo"])


@todo_router.get(
    "/",
    summary="Get all To Do",
    description="Get all Todo data that still active or not deleted",
    response_model=ResponseModel[List[Todo]],
)
def get_all():
    result = todo_usecase.get_all()

    return SuccessResponse(data=result)


@todo_router.get(
    "/{todo_id}",
    status_code=200,
    summary="Get Todo by ID",
    description="Get single Todo by given ID that not deleted",
    response_model=ResponseModel[Todo],
)
def get_single_by_id(todo_id: str, response: Response):
    todo = todo_usecase.get_by_id(todo_id=todo_id)

    return SuccessResponse[Todo](code=200, data=todo, message="Todo data")


@todo_router.post(
    "/",
    summary="Create new To Do data",
    description="Create new To Do Data",
    response_model=ResponseModel[Todo],
    status_code=201,
)
def create(todo_data: TodoIn):
    todo = todo_usecase.create(data=todo_data)

    return SuccessResponse[Todo](code=201, data=todo, message="New Todo created!")


@todo_router.put(
    "/{todo_id}",
    status_code=200,
    summary="Update Todo by ID",
    description="Update todo data by given ID",
    response_model=ResponseModel[Todo],
)
def update_by_id(todo_id: str, todo_data: TodoIn, response: Response):
    todo = todo_usecase.update(todo_id=todo_id, todo_data=todo_data)

    if not todo:
        # Return 404 message if given ID is not found in list
        response.status_code = 404
        return ErrorResponse[None](message="Todo Not found", code=404, data=None)

    return SuccessResponse[Todo](data=todo, message="Todo updated!")


@todo_router.patch(
    "/{todo_id}/finish",
    status_code=200,
    summary="Mark To Do as finished",
    description="Update the todo as finished and update the finished_at field",
    response_model=ResponseModel[Todo],
)
def finish_todo(todo_id: str, response: Response):
    result = todo_usecase.finish(todo_id=todo_id)

    if not result:
        # Return 404 message if given ID is not found in list
        response.status_code = 404
        return ErrorResponse[None](message="Todo Not found", code=404, data=None)

    return SuccessResponse[Todo](data=result, message="Todo finished!")


@todo_router.delete(
    "/{todo_id}",
    status_code=200,
    summary="Delete To Do ",
    description="Delete todo by given ID",
    response_model=ResponseModel[None],
)
def delete(todo_id: str, response: Response):
    result = todo_usecase.delete(todo_id=todo_id)

    if not result:
        # Return 404 message if given ID is not found in list
        response.status_code = 404
        return ErrorResponse[None](message="Todo Not found", code=404, data=None)

    return SuccessResponse[None](message="Todo deleted!")
