from typing import Optional

from pydantic import BaseModel


class Todo(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class TodoCreate(Todo):
    title: str
