from aiogram.types import InputMediaPhoto

from src.scheduler.groups.service import load_media, get_moscow_users
from src.tgbot.formatter import _B, _I


async def _12_00():
    from src.app import bot
    users = await get_moscow_users()
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