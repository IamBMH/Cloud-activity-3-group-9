from contextlib import asynccontextmanager

from fastapi import FastAPI
from tortoise import Tortoise

from app.config import TORTOISE_ORM
from app.authentication.api.router import router as auth_router
from app.files.api.router import router as files_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await Tortoise.init(config=TORTOISE_ORM)
    yield
    await Tortoise.close_connections()


app = FastAPI(
    title="Cloud Activity 3 API",
    lifespan=lifespan,
)

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(files_router, prefix="/files", tags=["Files"])