# Task Manager API

Простой CRUD API для управления задачами с веб-интерфейсом.  
Проект написан на **FastAPI**, использует **SQLite** и включает Swagger-документацию.  

---

## Основные возможности

- Создание, чтение, обновление и удаление задач (CRUD)
- Веб-интерфейс для взаимодействия через браузер
- Swagger UI для тестирования API
- Docker для быстрого развёртывания

---

## Структура проекта

task_manager/
├─ app/
│ ├─ routers/
│ │ └─ tasks.py # API роуты, реализуют CRUD
│ ├─ templates/
│ │ └─ index.html # Веб-интерфейс
│ ├─ database.py # Настройка SQLAlchemy
│ ├─ models.py # Модель Task
│ ├─ schemas.py # Pydantic схемы
│ └─ main.py # Точка входа FastAPI приложения
├─ data/
│ └─ test.db # SQLite база (создаётся автоматически)
├─ tests/
│ ├─ conftest.py
│ └─ test_tasks.py # Тесты
├─ requirements.txt # Python зависимости
├─ Dockerfile
├─ docker-compose.yml
└─ README.md
---

## Установка и запуск

### Локально (Python 3.10+)
1. Клонирование репозитория:
```bash
git clone <URL репозитория>
cd task_manager
```
2. Создание виртуального окружения:
```
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate.bat       # Windows
```
3. Устанавливка зависимостей:
```
pip install -r requirements.txt
```
4. Запуск сервера:
```
uvicorn app.main:app --reload
```
5. В браузере доступны ссылки:
* Сам трекер: http://127.0.0.1:8000
* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

### Через Docker
1. Сборка и запуск контейнера:
```
docker compose up --build
```
2. Сервер будет доступен по адресу:
http://127.0.0.1:8000
3. Данные SQLite сохраняются в папке data/test.db на хосте.

## Использование API

| HTTP Метод | Эндпоинт         | Описание                    |
|------------|-----------------|----------------------------|
| GET        | /api/tasks/      | Получить список всех задач  |
| GET        | /api/tasks/{id}  | Получить задачу по её ID   |
| POST       | /api/tasks/      | Создать новую задачу        |
| PUT        | /api/tasks/{id}  | Обновить существующую задачу|
| DELETE     | /api/tasks/{id}  | Удалить задачу по ID       |

## Тестирование
```
pip install pytest
pytest -v
```