from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
#from fastapi.staticfiles import StaticFiles
#from fastapi.routing import APIRouter

# Импортируем API-роутер для пользователей
from api.users import users_router

# Создаем экземпляр приложения
app = FastAPI()

# Подключаем шаблонизатор Jinja2
templates = Jinja2Templates(directory="templates")

# Подключаем статические файлы (если нужны)
#app.mount("/static", StaticFiles(directory="static"), name="static")

# Подключаем API-роутер для пользователей
app.include_router(users_router, prefix="/api")

# Эндпоинт для главной страницы
@app.get(
    "/",
    summary="Получение страницы index",
)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Главная страница"})

# Эндпоинт для страницы "О нас"
@app.get(
    "/about",
    summary="Получение странциы about",
)
async def read_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "title": "О нас"})