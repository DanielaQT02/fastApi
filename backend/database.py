from model import Todo
# https://motor.readthedocs.io/en/stable/
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://shayon:shayon@rest-api-shop.zh1ls.mongodb.net/fastAPITest?retryWrites=true&w=majority')
database = client.TodoList
collection = database.todo


async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find()
    async for documnet in cursor:
        todos.append(Todo(**documnet))
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document


async def update_todo(title, desc):
    await collection.update_one({'title': title}, {"$set": {
        "description": desc
    }})
    document = await collection.find_one({'title': title})
    return document

async def remove_todo(title):
    await collection.delete_one({'title': title})
    return True