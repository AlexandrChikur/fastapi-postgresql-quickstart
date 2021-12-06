import asyncpg
from fastapi import FastAPI
from loguru import logger

from app.core.config import settings


async def connect_to_db(app: FastAPI) -> None:
    logger.info(f"Connecting to the {settings.database_url}")
    app.state.pool = await asyncpg.create_pool(str(settings.database_url))
    logger.info("Connection established successfully")


async def disconnect_db(app: FastAPI) -> None:
    logger.info(f"Connecting to the {settings.database_url} closing ...")
    await app.state.pool.close()

    logger.info("Connection was closed successfully")