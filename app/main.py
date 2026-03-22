# app/main.py
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.config import TORTOISE_ORM

from app.authentication.api.router import router as auth_router

app = FastAPI()

app.include_router(auth_router)

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=True,
)