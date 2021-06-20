from fastapi import APIRouter, HTTPException

from todo.helpers import todo_list, todo_create, todo_retrieve, todo_update, todo_delete
from todo.models import Todo, TodoCreate
from todo.serializers import ToDosSerializer, ToDoSerializer

router = APIRouter()


@router.get('/todo/')
async def get_all_todos():
    response = await todo_list()
    return ToDosSerializer(response)


@router.post('/todo/')
async def create_todo(todo: TodoCreate):
    response = await todo_create(todo)
    if response:
        return ToDoSerializer(response)
    raise HTTPException(400, "Something went wrong")


@router.get("/todo/{id}")
async def retrieve_todo(id):
    response = await todo_retrieve(id)
    if response:
        return ToDoSerializer(response)
    raise HTTPException(404, f"There is no todo with this id {id}")


@router.put("/todo/{id}")
async def update_todo(id, todo: Todo):
    response = await todo_update(id, todo)
    if response:
        return ToDoSerializer(response)
    raise HTTPException(404, f"There is no todo with this id {id}")


@router.delete("/todo/{id}")
async def delete_todo(id):
    response = await todo_delete(id)
    if response:
        return "ToDo Successfully Deleted"
    raise HTTPException(404, f"There is no todo with this id {id}")
