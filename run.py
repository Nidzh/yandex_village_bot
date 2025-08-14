import uvicorn

from src.core.settings import settings

if __name__ == "__main__":
    uvicorn.run(
        "src.app:app",
        host=settings.config.HOST,
        port=settings.config.PORT,
        workers=settings.config.WORKERS_COUNT,
        log_level="info",
        loop="uvloop",
        http="httptools",
    )
