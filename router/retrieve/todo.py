from fastapi import APIRouter, Path
from model.todoItems import TodoItems

todo_router_retrieve = APIRouter()
todo_list = []

@todo_router_retrieve.get("/retrieve_todo", response_model=TodoItems)
async def retrieve_todo() -> dict:
    return {
        "todos": todo_list
    }