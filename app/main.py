from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.database import Base, engine
from app.routers import tasks
from app import models

# Создание таблиц (для учебных целей)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

# Подключение роутера
app.include_router(tasks.router)

# Шаблоны
templates = Jinja2Templates(directory="app/templates")


# -------------------------
# Root endpoint
# -------------------------
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
