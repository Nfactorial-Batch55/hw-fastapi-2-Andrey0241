from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.templating import Jinja2Templates
from typing import List, Optional
from .users import create_users

users = create_users(100)  # Генерация списка пользователей
app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# 1. Маршрут для списка всех пользователей с пагинацией
@app.get("/users")
def get_users(request: Request, page: int = 1, limit: int = 10):
    start = (page - 1) * limit
    end = start + limit
    paginated_users = users[start:end]

    return templates.TemplateResponse("users/index.html", {
        "request": request,
        "users": paginated_users,
        "page": page,
        "limit": limit,
        "total_users": len(users)
    })


# 2. Маршрут для пользователя по id
@app.get("/users/{id}")
def get_user(request: Request, id: int):
    user = next((user for user in users if user["id"] == id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return templates.TemplateResponse("users/user.html", {
        "request": request,
        "user": user
    })
