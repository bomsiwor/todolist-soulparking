from typing import List
from app.todo.entity.todo_entity import Todo, TodoIn
from ulid import ULID
from datetime import datetime
from core.helper.datetime import formatDateTime


class TodoRepository:
    def __init__(self, todos: List[Todo]) -> None:
        self.entity = todos

    def get_all(self) -> List[Todo]:
        result = [todo for todo in self.entity if not todo.deleted_at]

        return result

    def get_todo_by_id(self, todo_id: str) -> Todo | None:
        for todo in self.entity:
            if todo.id == todo_id and not todo.deleted_at:
                return todo

        return None

    def insert(self, todo_data: TodoIn) -> Todo:
        todo_id = ULID().__str__()
        todo = Todo(
            id=todo_id,
            title=todo_data.title,
            description=todo_data.description,
            created_at=str(formatDateTime(datetime.now())),
            updated_at=str(formatDateTime(datetime.now())),
        )

        self.entity.append(todo)

        return todo

    def update(self, *, todo_id: str, todo_data: TodoIn) -> Todo | None:
        for todo in self.entity:
            if todo.id == todo_id and not todo.deleted_at:
                # Update data if todo is found by ID
                todo.updated_at = str(formatDateTime(datetime.now()))
                todo.title = todo_data.title
                todo.description = todo_data.description

                return todo

        return None

    def delete(self, *, todo_id: str) -> Todo | None:
        for todo in self.entity:
            if todo.id == todo_id and not todo.deleted_at:
                # Update data if todo is found by ID
                todo.deleted_at = str(formatDateTime(datetime.now()))

                return todo

        return None
