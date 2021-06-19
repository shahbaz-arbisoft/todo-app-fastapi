import motor.motor_asyncio
from models import Todo

client = motor.motor_asyncio.AsyncIOMotorClient()

db = client.tododb
collection = db.todo


async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    import pdb;pdb.set_trace()
    async for document in cursor:
        todos.append(Todo(**document))
    return todos


async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document


async def retrieve_todo(title):
    document = await collection.find_one({"title": title})
    return document


async def update_todo(title, description):
    await collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = await collection.find_one({"title": title})
    return document


async def delete_todo(title):
    await collection.delete_one({"title": title})
    return True
