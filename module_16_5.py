from fastapi import FastAPI, Path, HTTPException, status, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Annotated
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
users = []

class User(BaseModel):
    id: int
    username: str
    age: int


# Вывод данных о пользователях
@app.get("/")
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get('/user/{user_id}')
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse('users.html', {'request':request, 'user': users[user_id-1]})
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")

# Создание нового пользователя
@app.post("/user/{username}/{age}", status_code=status.HTTP_201_CREATED)
async def create_user(request: Request, username: Annotated[str, Path(min_length=5,
                                                      max_length=20,
                                                      description='Enter username',
                                                      example='UrbanUser')],
                      age: int = Path(ge=18,
                                        le=120,
                                        description='Enter age',
                                        example='24')) -> HTMLResponse:
    """
    :param username:
    :param age:
    """
    if users:
        id_new = max(users, key= lambda m: m.id).id + 1
    else:
        id_new = 1
#    id_new = len(users) + 1
    users.append(User(id = id_new, username = username, age = age))
    return templates.TemplateResponse("users.html", {"request": request, "users": users})
        # f"User {id_new} is registered"

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

