from aiogram import F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.state import State, StatesGroup

from src.tgbot.formatter import _B
from src.tgbot.utils import smart_edit

router = Router()



class FeedbackState(StatesGroup):
    ANSWER_FAIRTALE = State()
    ANSWER_COCKTAIL = State()


@router.callback_query(F.data == "answer_fairytale")
async def answer_fairytale(callback, state, text, media):
    title = f"🎲 {_B('Кот Учёный')} слушает внимательно!\n\n✍️ Напиши все ответы одним сообщением 👇"


@router.callback_query(F.data == "answer_cocktails")
async def answer_cocktails(callback, state, text, media):
    ...