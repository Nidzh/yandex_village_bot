from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat, BotCommandScopeDefault
from loguru import logger

from src.apps.user.service import UserService
from src.db.context import get_session

USER_COMMANDS = [
    BotCommand(command="main", description="Главное меню"),
    BotCommand(command="city", description="Выбрать город"),
]

ADMIN_COMMANDS = (
    USER_COMMANDS
    + [
        # BotCommand(command="admin", description="Меню администратора"),
    ]
)


async def set_commands(bot: Bot):
    """Устанавливает команды для пользователей и администраторов."""
    try:
        await set_user_commands(bot)
        await set_admin_commands(bot)
        logger.info("Все команды меню успешно установлены")
    except Exception as e:
        logger.error(f"Ошибка установки команд: {e}")


async def set_user_commands(bot: Bot):
    """Устанавливает команды для пользователей."""
    try:
        await bot.set_my_commands(USER_COMMANDS, BotCommandScopeDefault())
    except Exception as e:
        logger.error(f"Ошибка установки команд для пользователей: {e}")


async def set_admin_commands(bot: Bot):
    """Устанавливает команды для администраторов."""
    async for session in get_session():
        service = UserService(session=session)
        admin_ids = await service.get_admin_ids()
        for admin_id in admin_ids:
            try:
                await bot.set_my_commands(ADMIN_COMMANDS, BotCommandScopeChat(chat_id=admin_id))
            except Exception as e:
                logger.error(f"Ошибка установки команд для администратора {admin_id}: {e}")
