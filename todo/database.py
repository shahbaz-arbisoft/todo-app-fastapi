import motor.motor_asyncio


def get_connection():
    client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
    db = client.tododb

    return db, client
