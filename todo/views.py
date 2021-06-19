from fastapi import APIRouter

router = APIRouter()


@router.get('/todo/')
async def get_all_todos():
	response = await fetch_all_todos()
    return response


@router.post('/todo/')
async def create_todo():
	response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@router.get("/todo/{id}")
async def retrieve_todo(id):
	response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")


@router.put("/todo/{id}")
async def update_todo(id):
	response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")


@router.delete("/todo/{id}")
async def delete_todo(id):
	response = await remove_todo(title)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {title}")
