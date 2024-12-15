from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from core.config import config
from core.helper.responses import ErrorResponse
from starlette.exceptions import HTTPException
from app.routes import api_router


def create_middleware() -> list[Middleware]:
    middlewares = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]

    return middlewares


def create_app() -> FastAPI:
    # Create FastAPI instance
    # Use value from config
    app = FastAPI(
        title=config.APP_NAME,
        version="1.0.0",
        debug=config.DEBUG,
        docs_url=None if config.APP_ENV == "production" else "/docs",
        middleware=create_middleware(),
    )

    # Include router from routes
    app.include_router(api_router)

    # Override the default exception handler
    # Remember to use starlette exception
    # Using fastapi exception won't work (or I have not know)
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        if exc.status_code == 404:
            return ErrorResponse(message="Resource not found, guys.", code=404).result()
        return ErrorResponse(message=str(exc.detail), code=exc.status_code).result()

    return app


app = create_app()
