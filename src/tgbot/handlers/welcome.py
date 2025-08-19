from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.apps.user.service import UserService
from src.db.context import get_session
from src.tgbot.formatter import _B, _I
from src.tgbot.localization.manager import TextManager
from src.tgbot.utils import smart_edit

router = Router()


async def welcome(callback, state, text):
    async for session in get_session():
        user = await UserService(session=session).get_user_by_id(callback.from_user.id)

    if user.city == 'moscow':
        title = (f"{_B('Привет!')}  🐾  Это Кот Учёный.\n\nТы в чат-боте Open Air Вертикалей {_I('«Явь и Навь»')}.\n\nГотовы отправиться в"
                 f" {_B('сказочное приключение')}? ✨")
    if user.city == 'belgrad':
        title = f"{_B('👋 Привет!')}\n\nТы в чат-боте Open Air Вертикалей {_I('«Балдёжкино»')}.\n\nГотовы отправиться в {_B('сказочное приключение')}? ✨"

    kb = InlineKeyboardBuilder()
    kb.button(text="🚀 Начинаем", callback_data="letsgo")
    kb.button(text="💬 Расскажи подробнее", callback_data="about")
    kb.adjust(1)

    await smart_edit(callback, title, kb)


@router.callback_query(F.data.startswith("about"))
async def about(callback, state, text):
    async for session in get_session():
        user = await UserService(session=session).get_user_by_id(callback.from_user.id)

    kb = InlineKeyboardBuilder()

    if user.city == 'moscow':
        title = (
            f"📅 22 августа мы встречаемся на Open Air {_B('«Явь и Навь»')}.\n\n"
            f"✨ Это день, когда привычная среда сменит ритм:\n"
            f"— в дневное время — {_I('забавные активности')}, музыкальные выступления, общение и мастер-классы.\n"
            f"— а ближе к вечеру начнётся {_B('«Навь»')} — вечерняя программа с рейвовой атмосферой.\n\n"
            f"🎭 На площадке тебя ждут неожиданные локации, роли, маршруты и люди.\n"
            f"У каждого будет своя история внутри общего события.\n\n"
            f"🕵️‍♀️ Скоро расскажем подробности — как устроена программа, как подключиться и что не стоит пропускать.\n\n"
            f"🤝 До встречи!\n\n"
            f"📌 А пока — ознакомься с функционалом главного меню."
        )

        kb.button(text=text.main, callback_data="main")

    if user.city == 'belgrad':
        title = (
            f"✨ {_B('Вжух!')} 22 августа Яндекс Вертикали приглашают вас в {_B('«Балдёжкино»')}!\n\n"
            f"💫 Забудь обо всём на свете и окунись в {_B('сказочную атмосферу')} нашего фестиваля под открытым небом!\n\n"
            f"🏡 Представь: волшебная деревня, где ты встретишь Бабу Ягу, Кощея Бессмертного и других любимых персонажей сказок.\n\n"
            f"🎉 Это будет день полного отрыва и веселья в компании самых ярких и неординарных людей!\n\n"
            f"🌌 А вечером деревня преобразится, и ты увидишь её — и себя — совершенно по-новому.\n\n"
            f"🗝 Готовы окунуться в мир чудес и приключений? {_B('Балдёжкино ждёт!')}\n\n"
            f"📅 Подробности и расписание волшебных развлечений мы раскроем 22 августа!\n\n"
            f"🤝 До встречи в сказке!"
        )

    await smart_edit(callback, title, kb)


@router.callback_query(F.data.startswith("letsgo"))
async def letsgo(callback, state, text):
    async for session in get_session():
        user = await UserService(session=session).get_user_by_id(callback.from_user.id)

    kb = InlineKeyboardBuilder()

    if user.city == 'moscow':
        title = (
            f"🔜 Скоро ты узнаешь много интересного о фестивале.\n\n"
            f"🌞 Отличного дня!\n\n"
            f"📌 А пока — ознакомься с функционалом главного меню."
        )

        kb.button(text=text.main, callback_data="main")

    if user.city == 'belgrad':
        title = (
            f"📅 Все подробности мы раскроем 22 августа.\n\n"
            f"🤝 Встречаемся в {_B('«Балдёжкино»')}!"
        )

    await smart_edit(callback, title, kb)
