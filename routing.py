from fastapi import FastAPI
from src.telegram.callback import telegram


def create_routing(app: FastAPI):
    app.include_router(telegram.router)
