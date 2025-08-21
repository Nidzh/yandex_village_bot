from aiogram import F, Router
from aiogram.types import InputFile, FSInputFile, CallbackQuery, InputMediaPhoto
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.apps.user.service import UserService
from src.db.context import get_session
from src.tgbot.formatter import _B
from src.tgbot.utils import smart_edit

router = Router()


@router.callback_query(F.data == "wardrobe")
async def wardrobe(callback: CallbackQuery, state, text, media):
    async for session in get_session():
        user = await UserService(session=session).get_user_by_id(callback.from_user.id)
        if user.wardrobe_ticket:
            wardrobe_ticket = user.wardrobe_ticket
        else:
            wardrobe_ticket = await UserService(session=session).create_wardrobe_ticket(callback.from_user.id)

    if not wardrobe_ticket:
        return

    if wardrobe_ticket <= 500:
        zone = "Нарядильне"
    else:
        zone = "Игрищах"

    title = (
        f"👋 Привет! За одёжку не беспокойся.\n\n"
        f"🧥 Твой номер в гардеробе — {_B(wardrobe_ticket)}.\n\n"
        f"🎒 Можешь оставить свои вещи в {_B(zone)}.\n"
        f"🗺 Чтобы найти, где это, загляни в меню в раздел {_B('Карта')}.\n\n"
        f"🌧 А ещё я — учёный и подготовил для тебя дождевики и бахилы на случай непогоды."
        f"Их ты тоже найдёшь в гардеробе."
    )

    kb = InlineKeyboardBuilder()
    kb.button(text="🗺️ Карта", callback_data="map")
    kb.button(text=text.back, callback_data="main")
    kb.adjust(1)

    file = FSInputFile(f"media/wardrobe/wardrobe_{wardrobe_ticket}.jpg")
    await callback.message.edit_media(
        media=InputMediaPhoto(
            media=file,
            caption=title,
        ),
        reply_markup=kb.as_markup()
    )
