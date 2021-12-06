from fastapi import FastAPI

from app.api.routes.api import router as api_router
from app.core.config import settings
from app.core.events import create_start_app_handler, create_stop_app_handler


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.title,
        description=settings.description,
        version=settings.version,
        debug=settings.debug,
    )

    application.include_router(api_router, prefix=settings.API_PREFIX)

    application.add_event_handler("startup", create_start_app_handler(application))
    application.add_event_handler("shutdown", create_stop_app_handler(application))

    return application


app = get_application()