from pydantic import BaseModel
from model.item import Item
from typing import List, Optional
from fastapi import Form

class Todo(BaseModel):
    id: Optional[int] = None
    item: str
    @classmethod
    
    def as_form(
        cls,
        item: str = Form(...)
    ):
        return cls(item=item)
