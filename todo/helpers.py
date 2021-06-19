from models import Todo
from database import get_connection


async def fetch_all_todos():
	db, client = get_connection()
    todos = []
    cursor = db.todo.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    client.close()
    return todos


async def create_todo(todo):
	db, client = get_connection()
    document = todo
    result = await db.todo.insert_one(document)
    client.close()
    return document


async def retrieve_todo(title):
	db, client = get_connection()
    document = await db.todo.find_one({"title": title})
    client.close()
    return document


async def update_todo(title, description):
	db, client = get_connection()
    await db.todo.update_one({"title": title}, {"$set": {"description": description}})
    document = await db.todo.find_one({"title": title})
    client.close()
    return document


async def delete_todo(title):
	db, client = get_connection()
    await db.todo.delete_one({"title": title})
    client.close()
    return True
