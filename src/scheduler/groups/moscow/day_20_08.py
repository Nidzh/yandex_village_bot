from aiogram.types import InputMediaPhoto
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.scheduler.groups.service import load_media, get_moscow_users, get_admin_users
from src.tgbot.formatter import _B


async def time_12_00(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"Знаю, что все вы — красавцы и красавицы, только в нашей сказке свой, особый Dress Code есть. "
        f"Встречают, как известно, по одёжке.\n\n"
        f"👗 {_B('Дресс-код: сказочный стиль с современными элементами.')}\n\n"
        f"Это значит:\n"
        f"• Различная народная одежда: сарафаны, косоворотки, кафтаны — всё, что близко вам и вашей культуре.\n"
        f"• Кокошники, повязки, тюбетейки и другие головные уборы — можно украсить их светодиодами.\n"
        f"• Вышивка красивая.\n"
        f"• Украшения диковинные.\n\n"
        f"Мы подготовили для вас мудборды для вдохновения. Не бойтесь экспериментировать! "
        f"Главное, чтобы было видно, что вы пришли из сказки, да ещё и в ногу со временем идёте.\n\n"
        f"🏆 Авторов лучших костюмов ждут призы и слава на весь сказочный мир!\n\n"
        f"И ещё! На нашем Open Air будет {_B('«Нарядильня»')}, где вы сможете дополнить свой образ "
        f"и придать ему последние штрихи. Так что не переживайте, если что-то не успели доделать!"
    )

    kb = None
    markup = kb.as_markup() if kb else None

    photos = [
        InputMediaPhoto(media=media["18_08_12_00_1.jpg"], caption=title),
        InputMediaPhoto(media=media["18_08_12_00_2.jpg"]),
        InputMediaPhoto(media=media["18_08_12_00_3.jpg"]),
        InputMediaPhoto(media=media["18_08_12_00_4.jpg"]),
        InputMediaPhoto(media=media["18_08_12_00_5.jpg"]),
    ]

    for user in users:
        await bot.bot.send_media_group(chat_id=user, media=photos)


async def time_14_00(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"🎶 Чтобы вы заранее могли настроиться на сказку, я, {_B('Кот Учёный')}, собрал для вас плейлист для настроения.\n\n"
        f"Тут и народные мотивы, и электронная музыка, и всякие сказочные переливы.\n\n"
        f"Слушайте, заряжайтесь энергией и готовьтесь к погружению в сказку.\n\n"
        f"🤝 До встречи на фестивале!"
    )

    kb = InlineKeyboardBuilder()
    kb.button(text="🎵 Ссылка на плейлист",
              url="https://music.yandex.ru/users/walarius@setitagila.ru/playlists/1003?utm_medium=copy_link&ref_id=9aa84f26-76f1-4ae6-8b0f-4f7a7a2519d0")

    markup = kb.as_markup() if kb else None

    for user in users:
        await bot.bot.send_message(chat_id=user, text=title, reply_markup=markup)


async def time_16_00(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"✨ Сейчас, мои любезные, я покажу вам диковинки невиданные — "
        f"мемы сказочные в стиле лубочном.\n\n"
        f"Тут кладезь историй, рассказанных языком народным, да с юмором знатным!\n\n"
        f"📜 В старину лубки рассказывали истории, учили мудрости и просто веселили народ.\n\n"
        f"Мы же решили взять эту традицию за основу и создать мемы в этом стиле, "
        f"но про нашу IT-шную жизнь.\n\n"
        f"Вот, полюбуйтесь!"
    )

    photos = [
        InputMediaPhoto(media=media["20_08_16_00_1.png"], caption=title),
        InputMediaPhoto(media=media["20_08_16_00_2.png"]),
        InputMediaPhoto(media=media["20_08_16_00_3.png"]),
        InputMediaPhoto(media=media["20_08_16_00_4.png"]),
    ]

    for user in users:
        await bot.bot.send_media_group(chat_id=user, media=photos)


async def time_18_00(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"🗺 А теперь — карта вам в руки. Точнее, на экран.\n\n"
        f"Это карта локаций нашего сказочного фестиваля.\n"
        f"Изучайте, запоминайте и не заблудитесь в лесу дремучем!\n\n"
        f"На карте всё отмечено да подписано: где игры, где угощение, "
        f"где мастер-классы, где танцы-пляски.\n\n"
        f"Всё для вашего удобства да сказочного настроения."
    )

    kb = InlineKeyboardBuilder()
    kb.button(text="🔍 Высокое разрешение", url="https://clck.ru/3NfkxE")
    markup = kb.as_markup() if kb else None

    for user in users:
        await bot.bot.send_photo(
            chat_id=user,
            photo=media["map.png"],
            caption=title,
            reply_markup=markup,
        )
