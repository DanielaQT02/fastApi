from model import Todo
from typing import List, Optional

# Base de datos simulada en memoria
todos_db: List[dict] = []


async def fetch_one_todo(title: str) -> Optional[dict]:
    """Obtener una tarea por título"""
    for todo in todos_db:
        if todo.get("title") == title:
            return todo
    return None


async def fetch_all_todos() -> List[Todo]:
    """Obtener todas las tareas"""
    todos = []
    for todo_dict in todos_db:
        todos.append(Todo(**todo_dict))
    return todos


async def create_todo(todo: dict) -> dict:
    """Crear una nueva tarea"""
    # Agregar a la lista
    todos_db.append(todo)
    return todo


async def update_todo(title: str, desc: str) -> Optional[dict]:
    """Actualizar descripción de una tarea"""
    for todo in todos_db:
        if todo.get("title") == title:
            todo["description"] = desc
            return todo
    return None


async def remove_todo(title: str) -> bool:
    """Eliminar una tarea"""
    for i, todo in enumerate(todos_db):
        if todo.get("title") == title:
            todos_db.pop(i)
            return True
    return False