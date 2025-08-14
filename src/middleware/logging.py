import sys
import traceback

from fastapi import FastAPI
from loguru import logger

from src.core.settings import settings


def setup_logging(app: FastAPI):
    logger.remove(0)

    logger.add(
        sink=sys.stdout,
        level=settings.config.LOG_LEVEL.upper(),
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message} {extra}</level>",
    )

    def exception_handler(exc_type, exc_value, exc_traceback):
        # Если исключение уже было перехвачено, просто игнорируем
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        # Логируем необработанное исключение
        logger.exception(
            "System exception",
            exc_type=exc_type,
            exc_value=exc_value,
            exc_traceback=traceback.format_tb(exc_traceback),
        )

    sys.excepthook = exception_handler
