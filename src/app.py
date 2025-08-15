import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from loguru import logger

from src.apps.router import router
from src.core.openapi import config
from src.core.settings import settings
from src.integrations.redis.client import redis_client
from src.middleware.cors import setup_cors
from src.middleware.exceptions import setup_exception_handlers
from src.middleware.logging import setup_logging
from src.middleware.monitoring import setup_monitoring_and_healthcheck
from src.middleware.pagination import setup_pagination
from src.scheduler.app import scheduler
from src.tgbot.app import TelegramBot


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Настройка кэширования
    FastAPICache.init(RedisBackend(redis=redis_client), prefix="cache")

    # Запуск периодических задач
    if settings.scheduler.RUN:
        scheduler.start()


    bot_task = None
    if settings.bot.RUN:
        async def _start_bot():
            await asyncio.sleep(5)
            try:
                await bot.run()
            except Exception as e:
                logger.exception("Ошибка при запуске бота: {}", e)

        bot_task = asyncio.create_task(_start_bot())

    logger.success("Приложение запущено")
    try:
        yield
    finally:
        if settings.bot.RUN:
            if bot_task:
                bot_task.cancel()
            await bot.stop()
        if settings.scheduler.RUN:
            scheduler.shutdown()
        logger.success("Приложение остановлено")


app = FastAPI(lifespan=lifespan, **config)
bot = TelegramBot(token=settings.bot.TOKEN, redis=redis_client, fastapi_app=app)
app.include_router(router, prefix="/api")

# Конфигурация приложения
setup_cors(app)
setup_logging(app)
setup_pagination(app)
setup_exception_handlers(app)
setup_monitoring_and_healthcheck(app)