from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

users_router = APIRouter()
"""
Создаем вложенный роутер для пользователей
"""

class UserBase(BaseModel):
    id: int
    name: str
    email: str
"""
Модель данных пользователя с использованием Pydantic
"""

fake_users_db = [
    {"id": 1, "name": "Александр", "email": "alex@example.com"},
    {"id": 2, "name": "Мария", "email": "maria@example.com"},
    {"id": 3, "name": "Иван", "email": "ivan@example.com"}
]
"""
Фиктивные данные для демонстрации
"""

@users_router.get(
    "/users/",
    response_model=List[UserBase],
    summary="Получение списка всех зарегистрированных пользователей",
)
async def read_users():
    """
    Представление для чтения списка пользователей
    """
    return fake_users_db

@users_router.post(
    "/users/",
    response_model=UserBase,
    summary="Создание нового пользователя",
)
async def create_user(user: UserBase):
    """
    Представление для создания нового пользователя
    """
    new_id = max(u["id"] for u in fake_users_db) + 1
    new_user = {"id": new_id, "name": user.name, "email": user.email}
    fake_users_db.append(new_user)
    return new_user


@users_router.get(
    "/users/{user_id}",
    response_model=UserBase,
    summary="Получение информации о пользователе",
)
async def read_user(user_id: int):
    """
    Представление для получения информации о пользователе
    """
    user = next((u for u in fake_users_db if u["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user


@users_router.delete(
    "/users/{user_id}",
    response_model=dict,
    summary="Удаление пользователя",
)
async def delete_user(user_id: int):
    """
    Представление для удаления пользвоателя по ID
    """
    global fake_users_db
    initial_length = len(fake_users_db)
    fake_users_db = [u for u in fake_users_db if u["id"] != user_id]

    # Проверяем, был ли пользователь удален
    if len(fake_users_db) == initial_length:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    return {"message": "Пользователь успешно удален"}