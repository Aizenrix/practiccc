# Task Tracker API

Backend-приложение на FastAPI для регистрации пользователей, авторизации по JWT и управления задачами.  
Проект был переразложен из одного файла в понятную модульную структуру с разделением на модели, схемы, репозитории, сервисы, зависимости и роуты.

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

- login: `admin`
- password: `Admin123`

## Скриншоты

Добавьте скриншоты в папку `README_assets/` и обновите пути ниже:

1. Swagger `/docs`  
   `README_assets/swagger_docs.png`
2. Успешная регистрация пользователя  
   `README_assets/register_success.png`
3. Успешный вход и получение токена  
   `README_assets/login_success.png`
4. Запрос `GET /auth/me` с токеном  
   `README_assets/auth_me.png`
5. Создание задачи  
   `README_assets/task_create.png`
6. Список задач  
   `README_assets/task_list.png`
7. Доступ администратора к `/admin/users`  
   `README_assets/admin_users.png`
8. Работа контейнера после запуска  
   `README_assets/docker_running.png`

Когда файлы будут готовы, можно вставить их прямо в README через markdown-картинки.
