from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

# Вывод данных о пользователях
@app.get("/users")
async def get_all_users() -> dict:
    return users

# Создание нового пользователя
@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5,
                                                      max_length=20,
                                                      description='Enter username',
                                                      example='UrbanUser')],
                      age: int = Path(ge=18,
                                        le=120,
                                        description='Enter age',
                                        example='24')) -> str:
    """
    :param username:
    :param age:
    """
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

# Обновление данных о пользователе
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: Annotated[str, Path(min_length=5,
                                                      max_length=20,
                                                      description='Enter username',
                                                      example='UrbanUser')],
                      age: int = Path(ge=18,
                                        le=120,
                                        description='Enter age',
                                        example='24')) -> str:
    """
    :param user_id:
    :param username:
    :param age:
    """
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

# Удаление пользователя
@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    """
    :param user_id:
    """
    if user_id in users:
        users.pop(user_id)
        return f"User {user_id} has been deleted"
    else:
        return "Пользователь не найден."

