from typing import List
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
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

    # Override default validation error
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):
        reformatted_message: List[str] = []

        for pydantic_error in exc.errors():
            # Get loc (path of the error property) & message
            loc, msg = pydantic_error["loc"], pydantic_error["msg"]

            # Get path. First path is body / query / path
            filtered_loc = loc[1:] if loc[0] in ("body", "query", "path") else loc

            # Join path as string with dot
            field_string = ".".join(filtered_loc)
            message = field_string + " : " + msg

            # Append message to list
            reformatted_message.append(message)

        return ErrorResponse(
            message="Validation error", data=reformatted_message, code=422
        ).result()

    return app


app = create_app()
