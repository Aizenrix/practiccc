# Task Tracker API

Backend-приложение на FastAPI для регистрации пользователей, авторизации по JWT и управления задачами

## Структура проекта

```text
.
├── app
│   ├── api
│   │   ├── deps.py
│   │   └── routes
│   │       ├── admin.py
│   │       ├── auth.py
│   │       └── tasks.py
│   ├── core
│   │   ├── config.py
│   │   └── security.py
│   ├── db
│   │   ├── database.py
│   │   └── redis_client.py
│   ├── models
│   │   ├── task.py
│   │   └── user.py
│   ├── repositories
│   │   ├── task_repository.py
│   │   └── user_repository.py
│   ├── schemas
│   │   ├── auth.py
│   │   ├── task.py
│   │   └── user.py
│   ├── services
│   │   ├── auth_service.py
│   │   └── task_service.py
│   └── main.py
├── README_assets
├── Dockerfile
├── docker-compose.yml
├── main.py
└── requirements.txt
```

## Запуск без Docker

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Swagger будет доступен по адресу [http://localhost:8000/docs](http://localhost:8000/docs)

## Запуск через Docker

```bash
docker compose up --build
```

После старта:

- backend: `http://localhost:8000`
- swagger: `http://localhost:8000/docs`
- redis: `localhost:6379`

## Основные маршруты

### Auth

- `POST /auth/register` регистрация пользователя
- `POST /auth/login` вход и получение JWT токена
- `GET /auth/me` получение текущего пользователя

### Tasks

- `POST /tasks/` создание задачи
- `GET /tasks/` список задач текущего пользователя
- `GET /tasks/{task_id}` просмотр одной задачи
- `PATCH /tasks/{task_id}` обновление задачи
- `DELETE /tasks/{task_id}` удаление задачи

### Admin

- `GET /admin/users` список пользователей, только для роли admin

## Данные администратора по умолчанию

login: `admin`
password: `Admin123`



## скрины
! [SWG] (/README_assets/swg/dc.png)