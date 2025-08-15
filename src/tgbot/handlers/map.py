from aiogram import F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.tgbot.formatter import _B
from src.tgbot.utils import smart_edit

router = Router()


@router.callback_query(F.data == "map")
async def map(callback, state, text, media):
    title = (
        f"🗺 На карте ты найдёшь все ключевые точки фестиваля.\n\n"
        f"🎧 По пути тебя будут сопровождать голосовые подсказки и навигационные указатели.\n\n"
        f"🚶‍♂️ Исследуй маршрут и выбирай направления в {_B('сказочном путешествии')}."
    )

    kb = InlineKeyboardBuilder()
    kb.button(text="🔍 Высокое разрешение", url="https://clck.ru/3NfkxE")
    kb.button(text=text.back, callback_data="main")
    kb.adjust(1)

    await smart_edit(callback, title, kb, media=media.get("map.png"))
