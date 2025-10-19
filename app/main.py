from fastapi import FastAPI

from app.routers.users import router as users_router
from app.routers.tasks import router as tasks_router

from app.db.database import Base, engine

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Todo API"
)

app.include_router(users_router)
app.include_router(tasks_router)
