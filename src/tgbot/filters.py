from aiogram.filters import BaseFilter
from aiogram.types import Message

from src.apps.user.service import UserService
from src.db.context import get_session


class AdminFilter(BaseFilter):
    async def __call__(self, obj: Message) -> bool:
        async for session in get_session():
            admin_ids = await UserService(session=session).get_admin_ids()
            return obj.from_user.id in admin_ids
