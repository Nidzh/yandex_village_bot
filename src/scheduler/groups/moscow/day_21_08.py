from aiogram.types import InputMediaPhoto
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.scheduler.groups.service import load_media, get_moscow_users, get_admin_users
from src.tgbot.formatter import _B


async def time_12_00(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"🚐 Чтобы вам было удобно добираться до нашего сказочного места, вот информация о расписании трансфера:\n\n"
        f"📍 Место отбытия автобусов на Open Air:\n"
        f"Ул. Зеленоградская, 41 (Парковочная зона 4098).\n\n"
        f"⏰ Время отбытия:\n"
        f"12:30 — 1 рейс\n"
        f"13:00 — 2 рейс\n"
        f"13:30 — 3 рейс\n"
        f"14:00 — 4 рейс\n\n"
        f"⏰ Время отбытия автобусов обратно в город:\n"
        f"23:00 — 1 рейс до метро Ховрино\n"
        f"00:00 — 2 рейс до метро Ховрино\n"
        f"02:00 — 1 рейс до метро Ховрино и БЦ «Аврора»\n"
        f"02:30 — 2 рейс до метро Ховрино и БЦ «Аврора»\n\n"
        f"🧾 При регистрации на посадку в автобус подготовьте заранее свои штрих-коды, "
        f"чтобы посадка прошла быстрее и комфортнее.\n\n"
        f"✨ Надеюсь, эта информация вам поможет, а путь ваш будет лёгким и приятным.\n"
        f"🤝 До встречи на фестивале!"
    )

    kb = InlineKeyboardBuilder()
    kb.button(text="📍 Я.Карты", url="https://yandex.ru/maps/-/CHtbR2kH")
    kb.button(text="🔍 Высокое разрешение", url="https://clck.ru/3NiErq")
    markup = kb.as_markup() if kb else None

    for user in users:
        await bot.bot.send_photo(
            chat_id=user,
            photo=media["transfer.jpg"],
            caption=title,
            reply_markup=markup,
        )



async def time_16_00(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"🎲 А вот вам игра на смекалку.\n\n"
        f"Попробуйте угадать, какие сказки я зашифровал в эмодзи.\n\n"
        f"✍️ После того как нажмёшь кнопку {_B('✍️ Мой ответ')}, "
        f"пришли одно сообщение со всеми своими ответами.\n\n"
        f"⚠️ Сообщения, отправленные до нажатия кнопки, не засчитываются.\n\n"
        f"Коли всё угадаешь — получишь почёт и уважение {_B('Кота Учёного')}."
    )

    kb = InlineKeyboardBuilder()
    kb.button(text="✍️ Мой ответ", callback_data="answer:fairytale")
    markup = kb.as_markup() if kb else None

    photos = [
        InputMediaPhoto(media=media["21_08_16_00_1.jpg"]),
        InputMediaPhoto(media=media["21_08_16_00_2.jpg"]),
        InputMediaPhoto(media=media["21_08_16_00_3.jpg"]),
        InputMediaPhoto(media=media["21_08_16_00_4.jpg"]),
        InputMediaPhoto(media=media["21_08_16_00_5.jpg"]),
    ]

    for user in users:
        await bot.bot.send_media_group(chat_id=user, media=photos)
        await bot.bot.send_message(
            chat_id=user,
            text=title,
            reply_markup=markup
        )



async def time_18_00(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"🎨 А вот вам задание для самых креативных.\n\n"
        f"Объявляем конкурс на самый необычный рецепт коктейля в сказочном стиле {'🍹'}.\n\n"
        f"Придумайте напиток, который бы отражал дух {_B('Яви')} и был таким же ярким и радостным. "
        f"Название, ингредиенты, подача — всё должно быть пропитано сказкой.\n\n"
        # f"✍️ Отправляйте рецепты в бот с подписью {_B('«Вкус Яви»')}.\n\n"
        f"✍️ После того как нажмёшь кнопку {_B('✍️ Мой рецепт')}, "
        f"пришли одно сообщение со своим рецептом.\n\n"
        f"⚠️ Сообщения, отправленные до нажатия кнопки, не засчитываются.\n\n"
        f"🏆📜 Самый необычный коктейль станет частью летописи нашей сказки."
    )

    kb = InlineKeyboardBuilder()
    kb.button(text="✍️ Мой рецепт", callback_data="answer:cocktail")
    markup = kb.as_markup() if kb else None

    for user in users:
        await bot.bot.send_photo(
            chat_id=user,
            photo=media["21_08_18_00.jpg"],
            caption=title,
            reply_markup=markup,
        )