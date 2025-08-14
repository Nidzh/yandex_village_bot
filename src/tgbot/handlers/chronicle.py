from aiogram import F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.tgbot.utils import smart_edit

router = Router()


@router.callback_query(F.data == "chronicle")
async def chronicle(callback, state, text):
    title = f"📖 Летопись будет доступна в день фестиваля."

    kb = InlineKeyboardBuilder()
    kb.button(text=text.back, callback_data="main")
    kb.adjust(1)

    await smart_edit(callback, title, kb)
