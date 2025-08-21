from aiogram import F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.tgbot.formatter import _B
from src.tgbot.utils import smart_edit

router = Router()


@router.callback_query(F.data == "chronicle")
async def chronicle(callback, state, text, media):
    title = (
        f"📖 Друзья мои, сегодня мы вместе создадим {_B('летопись нашей сказки')}.\n\n"
        f"Ответь на следующие вопросы {_B('одним сообщением')} и оставь свой след "
        f"в общей истории {_B('Open Air Яндекс Вертикалей')}:\n\n"
        f"1️⃣ Какое у вас настроение сегодня?\n"
        f"2️⃣ Что вас больше всего впечатлило во время Яви?\n"
        f"3️⃣ Какой момент стал самым запоминающимся в Нави?\n"
        f"4️⃣ Поделитесь интересной историей, которую вы пережили на Open Air.\n"
        f"5️⃣ Опишите прошедший день в 3 словах.\n\n"
        f"✍️ Чтобы твои ответы засчитались, нажми кнопку {_B('📱 Готов(а) отвечать')} ниже, "
        f"а потом пришли одно сообщение с ответами.\n\n"
        f"⚠️ Сообщения, отправленные до нажатия кнопки, не учитываются."
    )

    kb = InlineKeyboardBuilder()
    kb.button(text="📱 Готов(а) отвечать", callback_data="answer:chronicle")
    kb.button(text=text.back, callback_data="main")
    kb.adjust(1)

    await smart_edit(callback, title, kb, media=media.get("main.png"))
