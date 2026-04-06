from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import router
from app.infra.database import Base, engine
from app.services.scheduler_service import start_scheduler, stop_scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    start_scheduler()
    yield
    stop_scheduler()


app = FastAPI(lifespan=lifespan)

app.include_router(router)