from aiogram import F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.state import State, StatesGroup

from src.apps.user.schemas import AnswerCreate
from src.apps.user.service import UserService
from src.db.context import get_session
from src.tgbot.formatter import _B
from src.tgbot.utils import smart_edit

router = Router()



class AnswerState(StatesGroup):
    FAIRYTALE = State()
    COCKTAIL = State()


@router.callback_query(F.data.startswith('answer:'))
async def answer_fairytale(callback, state, text, media):
    await callback.answer()

    data = callback.data.split(':')
    question_code = data[1]
    await state.set_data({"question_code": question_code})

    match question_code:
        case "fairytale":
            await state.set_state(AnswerState.FAIRYTALE)
            title = (
                f"😺 {_B('Кот Учёный')} навострил уши!\n\n"
                "✍️ Напиши все свои ответы одним сообщением:"
            )
        case "cocktail":
            await state.set_state(AnswerState.COCKTAIL)
            title = (
                f"😺 {_B('Кот Учёный')} ждёт твой креатив!\n\n"
                "✍️ Пришли рецепт целиком в одном сообщении:"
            )


    await callback.message.answer(title)


@router.message(AnswerState.FAIRYTALE)
@router.message(AnswerState.COCKTAIL)
async def admin_answer(message, state):
    data = await state.get_data()
    question_code = data['question_code']

    if not message.text:
        await message.answer("❌ Ответ должен быть текстом.")
        return

    async for session in get_session():
        await UserService(session=session).create_answer(
            AnswerCreate(
                user_id=message.from_user.id,
                question_code=question_code,
                answer=message.text,
            )
        )

    await message.answer("📜 Ответ записан в летопись!")
    await state.clear()

