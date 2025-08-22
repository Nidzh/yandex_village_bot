import asyncio
import datetime
from io import BytesIO
from zoneinfo import ZoneInfo

from aiogram import F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from src.apps.user.schemas import AnswerCreate
from src.apps.user.service import UserService
from src.db.context import get_session
from src.integrations.s3_client import upload_fileobj_to_s3
from src.tgbot.formatter import _B
from src.tgbot.handlers.main import main

router = Router()


class AnswerState(StatesGroup):
    FAIRYTALE = State()
    COCKTAIL = State()
    CHRONICLE = State()
    COSTUME = State()


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
        case "chronicle":
            await state.set_state(AnswerState.CHRONICLE)
            title = f"✍️ Отлично! Теперь пришли одно сообщение со своими ответами:"
        case "costume":
            await state.set_state(AnswerState.COSTUME)
            title = f"👌 Отлично! Теперь отправь одно фото своего костюма 📸"

    await callback.message.answer(title)


@router.message(AnswerState.FAIRYTALE)
@router.message(AnswerState.COCKTAIL)
@router.message(AnswerState.CHRONICLE)
async def admin_answer(message, state, text, media):
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
    await asyncio.sleep(3)
    await main(message, state, text, media)


@router.message(AnswerState.COSTUME)
async def costume_answer(message: Message, state, text, media):
    data = await state.get_data()
    question_code = data['question_code']

    if not message.photo:
        await message.answer("❌ Ответ должен быть фотографией")
        return

    # самое большое фото
    photo = message.photo[-1]
    tg_file = await message.bot.get_file(photo.file_id)

    # создаём in-memory буфер
    buf = BytesIO()
    await message.bot.download(tg_file, destination=buf)

    user_id = message.from_user.id
    ts = datetime.datetime.now(ZoneInfo("Europe/Moscow")).strftime("%Y%m%d_%H%M%S")
    key = f"{user_id}_{ts}.jpg"
    upload_fileobj_to_s3(buf, key)

    async for session in get_session():
        await UserService(session=session).create_answer(
            AnswerCreate(
                user_id=message.from_user.id,
                question_code=question_code,
                answer=key,
            )
        )

    await message.answer(f"✨ Теперь вы участник конкурса, удачи!")
    await state.clear()
    await asyncio.sleep(3)
    await main(message, state, text, media)
