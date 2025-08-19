from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.apps.user.schemas import UserCreate, UserUpdateSchema
from src.apps.user.service import UserService
from src.db.context import get_session
from src.tgbot.formatter import _B
from src.tgbot.handlers.welcome import welcome
from src.tgbot.utils import smart_edit

router = Router()


@router.message(CommandStart())
async def start(message: Message, state, text):
    await state.clear()

    user = UserCreate(
        id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        username=message.from_user.username,
        language_code=message.from_user.language_code,
    )

    # Создание или обновление пользователя
    async for session in get_session():
        await UserService(session=session).create_or_update_user(user)

    await choice_city(message, state, text)
    await message.delete()

@router.message(Command("city"))
async def choice_city(message: Message, state, text):
    title = f"{_B('🎉 Добро пожаловать в чат-бот Open Air Яндекс Вертикалей!')}\n\nВыберите свой город:"

    kb = InlineKeyboardBuilder()
    kb.button(text="🇷🇺 Москва", callback_data="city:moscow")
    kb.button(text="🇷🇸 Белград", callback_data="city:belgrad")
    kb.adjust(2)

    await message.answer(title, reply_markup=kb.as_markup())


@router.callback_query(F.data.startswith("city:"))
async def set_city(callback: CallbackQuery, state: FSMContext, text):
    await callback.answer()
    city = callback.data.split(":")[1]

    user_update_data = UserUpdateSchema(
        id=callback.from_user.id,
        city=city,
    )

    async for session in get_session():
        await UserService(session=session).update_user(user_update_data)

    await welcome(callback, state, text)
