import asyncio

from aiogram import F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.apps.user.service import UserService
from src.db.context import get_session
from src.tgbot.formatter import _Q, _B
from src.tgbot.handlers.start import choice_city
from src.tgbot.utils import smart_edit

router = Router()


@router.callback_query(F.data == "main")
@router.message(Command("main"))
async def main(message, state, text, media):
    await state.clear()

    async for session in get_session():
        user = await UserService(session=session).get_user_by_id(message.from_user.id)
        if not user.city:
            await choice_city(message, state, text)
            return

        if user.city == 'belgrad':
            title = (
                f"📅 Все подробности мы раскроем 22 августа.\n\n"
                f"🤝 Встречаемся в {_B('«Балдёжкино»')}!"
            )
            await message.answer(title)
            return

    title = f"{_B('📍 Главное меню:')}"

    #  Формируем клавиатуру.
    kb = InlineKeyboardBuilder()
    kb.button(text="🗺️ Карта", callback_data="map")
    kb.button(text="🚖 Трансфер", callback_data="transfer")
    kb.button(text="📅 Программа", callback_data="program")
    kb.button(text="🎯 Активности", callback_data="activity")
    kb.button(text="🧥 Гардероб", callback_data="wardrobe")
    kb.button(text="📜 Летопись", callback_data="chronicle")
    kb.button(text="🐱 Котопомощь", callback_data="help")

    kb.adjust( 2, 2, 2, 1)

    await smart_edit(message, title, kb, media=media.get("main.png"))
