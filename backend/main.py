from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from database import (fetch_one_todo, fetch_all_todos, create_todo, update_todo, remove_todo)
from model import Todo

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def read_post():
    return {"Ping": "Something"}

@app.get('/api/todo', status_code=status.HTTP_200_OK)
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get('/api/todo/{title}', response_model=Todo, status_code=status.HTTP_200_OK)
async def get_todo_by_id(title: str):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No existe la tarea: {title}")


@app.post('/api/todo', response_model=Todo, status_code=status.HTTP_201_CREATED)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Error al crear la tarea")

@app.put('/api/todo/{title}', response_model=Todo, status_code=status.HTTP_200_OK)
async def put_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No existe la tarea: {title}")

@app.delete('/api/todo/{title}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(title: str):
    response = await remove_todo(title)
    if response:
        return None
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No existe la tarea: {title}")



