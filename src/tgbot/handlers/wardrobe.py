from aiogram import F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.tgbot.formatter import _B
from src.tgbot.utils import smart_edit

router = Router()


@router.callback_query(F.data == "wardrobe")
async def wardrobe(callback, state, text, media):
    title = (
        f"👋 Привет! За одёжку не беспокойся.\n\n"
        f"🧥 Твой номер в гардеробе — {_B('5')}.\n"
        f"🎒 Можешь оставить свои вещи в {_B('Нарядильне')}.\n"
        f"🗺 Чтобы найти, где это, загляни в меню в раздел {_B('Карта')}.\n\n"
        f"🧠 А ещё я — учёный и подготовил для тебя дождевики и бахилы на случай непогоды.\n"
        f"🌧 Их ты тоже найдёшь в гардеробе."
    )

    kb = InlineKeyboardBuilder()
    kb.button(text=text.back, callback_data="main")
    kb.adjust(1)

    # await smart_edit(callback, title, kb, media=media.get("wardrobe.jpg"))
    await callback.answer("Раздел будет доступен в день фестиваля.", show_alert=True)
