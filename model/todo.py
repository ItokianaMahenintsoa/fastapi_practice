from pydantic import BaseModel
from model.item import Item

class Todo(BaseModel):
    id: int
    item: Item
