from aiogram import F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.tgbot.formatter import _B
from src.tgbot.utils import smart_edit

router = Router()


@router.callback_query(F.data == "transfer")
async def transfer(callback, state, text, media):
    title = (
        f"🚌 {_B('Дорогие друзья!')} Добраться до Open Air Яндекс Вертикалей можно на комфортных автобусах.\n\n"
        f"📍 Место отбытия — Метро “Ховрино” Автомобильная парковка у выхода №4.\n\n"
        f"⏰ {_B('Время отбытия:')}\n"
        f"12:30 — 1 рейс\n"
        f"13:00 — 2 рейс\n"
        f"13:30 — 3 рейс\n"
        f"14:00 — 4 рейс"
    )

    kb = InlineKeyboardBuilder()
    kb.button(text="📍 Я.Карты", url="https://yandex.ru/maps/-/CHtbR2kH")
    kb.button(text="🔍 Высокое разрешение", url="https://clck.ru/3Ng96j")
    kb.button(text=text.back, callback_data="main")
    kb.adjust(1)

    await smart_edit(callback, title, kb, media=media.get("transfer.jpg"))
