from app.todo.entity.todo_entity import TodoIn
from app.todo.repository.todo_repository import TodoRepository
from core.helper.datetime import formatDateTime
from datetime import datetime


class TodoUsecase:
    def __init__(self, repo: TodoRepository) -> None:
        self.repo = repo

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, *, todo_id: str):
        return self.repo.get_todo_by_id(todo_id=todo_id)

    def create(self, *, data: TodoIn):
        return self.repo.insert(data)

    def update(self, *, todo_id: str, todo_data: TodoIn):
        return self.repo.update(todo_id=todo_id, todo_data=todo_data)

    def delete(self, *, todo_id: str):
        return self.repo.delete(todo_id=todo_id)

    def finish(self, *, todo_id: str):
        # Get todo data by ID
        todo = self.repo.get_todo_by_id(todo_id=todo_id)

        # return none if data not found
        # Raise exception for next update
        if not todo:
            return None

        # Raise exceptiionn if todo already finished
        if todo.finished_at:
            return None

        # Update finished at & updated at
        todo.finished_at = str(formatDateTime(datetime.now()))
        todo.updated_at = str(formatDateTime(datetime.now()))

        return todo
