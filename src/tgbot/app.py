import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramAPIError
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import Update
from fastapi import FastAPI, HTTPException, Request
from loguru import logger
from redis import Redis

from src.core.settings import settings
from src.tgbot.commands import set_commands
from src.tgbot.middlewares import MIDDLEWARES
from src.tgbot.router import MAIN_ROUTER
from src.tgbot.services.media_collector import upload_all_media, read_media_map


class TelegramBot:
    def __init__(self, token: str, fastapi_app: FastAPI, redis: Redis):
        self.bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        self.dp = Dispatcher(storage=RedisStorage(redis))
        self.fastapi_app = fastapi_app
        self.webhook_url = settings.bot.WEBHOOK_URL
        self.webhook_path = "/webhook"
        self.lock_file_path = "/tmp/webhook.lock"

    async def run(self):
        try:
            self._register_routers()
            self._register_global_middlewares()
            await set_commands(self.bot)
            await self._declare_fastapi_webhook_route()
            await self._set_webhook_with_file_lock()
            await upload_all_media(self.bot)
            await read_media_map(self.dp)
            logger.success("Телеграм-бот запущен")

        except TelegramAPIError as e:
            logger.error(f"Не удалось установить webhook: {e}")
            raise RuntimeError("Failed to set webhook")

    def _register_global_middlewares(self):
        for middleware in MIDDLEWARES:
            self.dp.message.outer_middleware(middleware)
            self.dp.callback_query.outer_middleware(middleware)
        logger.info("Глобальные миддлвары зарегистрированы")

    def _register_routers(self):
        self.dp.include_routers(*MAIN_ROUTER)
        logger.info("Роутеры зарегистрированы")

    async def _declare_fastapi_webhook_route(self):
        @self.fastapi_app.post(self.webhook_path, include_in_schema=False)
        async def webhook_handler(request: Request):
            try:
                update = Update.model_validate(await request.json(), context={"tgbot": self.bot})
                await self.dp.feed_update(self.bot, update)
            except TelegramAPIError as e:
                logger.error(f"Telegram API error: {e}")
                raise HTTPException(status_code=500, detail="Telegram API error")
            except Exception as e:
                logger.exception(f"Unhandled exception: {e}")
                raise HTTPException(status_code=500, detail="Internal Server Error")

    async def _set_webhook_with_file_lock(self):
        logger.info("Настройка вебхука...")

        if os.path.exists(self.lock_file_path):
            logger.info("Блокировка уже существует, пропускаем установку вебхука")
            return

        try:
            with open(self.lock_file_path, "w") as lock:
                lock.write("locked")

            current_webhook = await self.bot.get_webhook_info()
            if current_webhook.url != self.webhook_path:
                await self.bot.set_webhook(
                    url=self.webhook_url + self.webhook_path,
                    allowed_updates=self.dp.resolve_used_update_types(),
                    drop_pending_updates=True,
                )
            logger.info("Вебхук установлен")
            current_webhook = await self.bot.get_webhook_info()
            logger.debug("Текущий вебхук:", **current_webhook.model_dump())
        except TelegramAPIError as e:
            logger.error(f"Не удалось установить вебхук: {e}")
            raise RuntimeError("Failed to set webhook")

    async def stop(self):
        logger.info("Удаление вебхука и завершение работы бота...")
        try:
            await self.bot.delete_webhook()
            os.remove(self.lock_file_path)
            logger.info("Webhook удалён")
        finally:
            await self.bot.session.close()
            await self.dp.storage.close()
            logger.info("Бот остановлен")
