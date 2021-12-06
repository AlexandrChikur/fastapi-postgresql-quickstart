from typing import Callable

from fastapi import FastAPI

from app.db.events import connect_to_db, disconnect_db


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        await connect_to_db(app)

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        await disconnect_db(app)

    return stop_app