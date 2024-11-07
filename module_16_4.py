from ast import Index

from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int


# Вывод данных о пользователях
@app.get("/users")
async def get_all_users() -> List[User]:
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
    id_new = len(users) + 1
    users.append(User(id = id_new, username = username, age = age))
    return f"User {id_new} is registered"

# Обновление данных о пользователе
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: Annotated[str, Path(min_length=5,
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
    try:
        users[user_id - 1] = User(id = user_id, username = username, age = age)
        return f"The user {user_id} is updated"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


# Удаление пользователя
@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    """
    :param user_id:
    """
    for i, user in enumerate(users):
        if user.id == user_id:
            return users.pop(i)
            # return f"User ID={user_id} deleted!"
    else:
        raise HTTPException(status_code=404, detail="User was not found")

