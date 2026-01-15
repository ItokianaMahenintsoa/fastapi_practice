from typing import List
from pydantic import BaseModel
from model.todoItem import TodoItem


class TodoItems(BaseModel):
    todos: List[TodoItem]
    class Config: 
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1"
                    }, 
                    {
                        "item": "Example schema 2"
                    }
                ]
            }
        }