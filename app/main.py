from fastapi import FastAPI

from app.api.routes import admin_router, auth_router, tasks_router
from app.db.database import Base, SessionLocal, engine
from app.models import Task, User
from app.repositories.user_repository import UserRepository

app = FastAPI(title="Task Tracker API", version="1.0.0")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        repo = UserRepository(db)
        admin = repo.get_by_username("admin")
        if not admin:
            repo.create(
                email="admin@example.com",
                username="admin",
                phone="+7-900-000-00-00",
                password="Admin123",
                role="admin",
            )
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Task Tracker API is running"}


app.include_router(auth_router)
app.include_router(tasks_router)
app.include_router(admin_router)
