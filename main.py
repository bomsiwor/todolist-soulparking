import uvicorn
from core.config import config


def main():
    uvicorn.run(
        "app.server:app",
        reload=True if config.APP_ENV != "production" else False,
        port=config.PORT,
    )


if __name__ == "__main__":
    main()
