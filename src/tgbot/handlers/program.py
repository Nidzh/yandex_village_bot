from aiogram import F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.tgbot.formatter import _B
from src.tgbot.utils import smart_edit

router = Router()


@router.callback_query(F.data == "program")
async def program(callback, state, text):
    title = f"{_B('~ Расписание выступлений на сцене ~')}"

    kb = InlineKeyboardBuilder()
    kb.button(text=text.back, callback_data="main")
    kb.adjust(1)

    await smart_edit(callback, title, kb)
