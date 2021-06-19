from bson import ObjectId

from todo.database import get_connection


async def todo_list():
    db, client = get_connection()
    todos = list()
    cursor = db.todo.find({})
    async for document in cursor:
        todos.append(document)
    client.close()
    return todos


async def todo_create(todo):
    db, client = get_connection()
    result = await db.todo.insert_one(dict(todo))
    document = await db.todo.find_one({"_id": result.inserted_id})
    client.close()
    return document


async def todo_retrieve(id):
    db, client = get_connection()
    document = await db.todo.find_one({"_id": ObjectId(id)})
    client.close()
    return document


async def todo_update(id, todo):
    db, client = get_connection()
    todo = todo.dict(exclude_unset=True)
    await db.todo.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(todo)
        })
    document = await db.todo.find_one({"_id": ObjectId(id)})
    client.close()
    return document


async def todo_delete(id):
    db, client = get_connection()
    await db.todo.delete_one({"_id": ObjectId(id)})
    client.close()
    return True
