from collections.abc import Awaitable, Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from src.apps.user.service import UserService
from src.db.context import get_session
from src.tgbot.localization.manager import TextManager


class LocalizationMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        async for session in get_session():
            user_service = UserService(session=session)
            lang_code = await user_service.get_user_language_code(user_id=event.from_user.id)
            data["text"] = TextManager(lang_code=lang_code)

        return await handler(event, data)


# Список глобальных middleware
MIDDLEWARES = [
    LocalizationMiddleware(),
]
