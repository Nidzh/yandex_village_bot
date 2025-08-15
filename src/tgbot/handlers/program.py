from aiogram import F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.tgbot.formatter import _B
from src.tgbot.utils import smart_edit

router = Router()


@router.callback_query(F.data == "program")
async def program(callback, state, text, media):
    title = f"{_B('📅 Программа:')}\n\n"

    title += (
        f"15:00–15:10 — Телемост с Белградом, Приветствие руководителей\n"
        f"15:10–15:30 — Музыкальный сет от ТОПов\n"
        f"15:30–15:40 — Интерактивы с гостями\n"
        f"15:40–17:40 — Минута славы. Номера от сотрудников\n"
        f"17:40–18:00 — Интерактивы от ведущего\n"
        f"18:00–19:30 — DJ Сет\n"
        f"18:00–19:00 — Запуск воздушных змеев\n"
        f"19:30–19:40 — Телемост с Белградом, Награждение конкурса костюмов\n"
        f"19:40–20:30 — Группа “Хвоя”\n"
        f"20:30–20:40 — Сбор гостей на “Поляне притопа”\n"
        f"20:40–20:47 — Переход в Навь\n"
        f"20:47–21:00 — Танцы с Лешим"
    )

    kb = InlineKeyboardBuilder()
    kb.button(text=text.back, callback_data="main")
    kb.adjust(1)

    await smart_edit(callback, title, kb, media=media.get("main.png"))
