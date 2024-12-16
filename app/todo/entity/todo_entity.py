from typing import List, Optional
from pydantic import BaseModel, Field


class Todo(BaseModel):
    id: str
    title: str = Field(title="Title")
    description: str
    finished_at: Optional[str] = Field(serialization_alias="finishedAt", default=None)
    created_at: str = Field(serialization_alias="createdAt")
    updated_at: str = Field(serialization_alias="updatedAt")
    deleted_at: Optional[str] = Field(serialization_alias="deletedAt", default=None)


class TodoIn(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=5)


todos: List[Todo] = []
