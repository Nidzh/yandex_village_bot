from aiogram.types import InputMediaPhoto
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.scheduler.groups.service import load_media, get_belgrad_users, get_admin_users
from src.tgbot.formatter import _B, _A


# ВРЕМЯ ВЫХОДА ПОСТОВ УКАЗАНО МОСКОВСКОЕ

async def time_12_30(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_belgrad_users()

    title = (
        f"🚌 {_B('Путь в сказку')}\n\n"
        f"Всем доброго утра!\n"
        f"В 12:30 у главного офиса вас встретит наш трансфер в сказку.\n"
        f"Подойдите на 10 минут раньше — Домовой расписание блюдёт, а Баба Яга уважает пунктуальных.\n\n"
        f"📍 Точка на карте: {_A('открыть в Maps', 'https://maps.app.goo.gl/YTvoVQBxZQDTFU3r8')}\n"
        f"🧭 Если собьётесь с тропы — зовите проводника: +381621623834 — Анастасия.\n"
        f"🆘 Если возникнут другие вопросы или нужна помощь — обращайтесь к нашей кикиморе: "
        f"+381621103264, TG {_A('@And_Irena', 'https://t.me/And_Irena')} — Ирина."
    )

    for user in users:
        await bot.bot.send_message(chat_id=user, text=title)


async def time_14_30(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_belgrad_users()

    title = (
        f"🌀 {_B('Добро пожаловать в Балдёжкино')}\n\n"
        f"Ой-ёй… небо-то сегодня какое — волшебное.\n"
        f"А всё потому, что ворота Балдёжкино сегодня отворяют врата свои для путников и путниц.\n\n"
        f"У самой арки тебя встретят старосты деревни и вручат карту.\n"
        f"С ней легко отыщешь путь — каждая тропка, каждая чудо-локация на ней отмечена.\n\n"
        f"Скоро всё начнётся… сказка уже близко."
    )

    for user in users:
        await bot.bot.send_message(chat_id=user, text=title)


async def time_14_55(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_belgrad_users()

    title = (
        f"🕯 {_B('Магический портал')}\n\n"
        f"Одна мудрая хозяйка деревни, Баба Яга, скоро проведёт "
        f"{_B('Особенную церемонию')}.\n"
        f"Которая откроет путь туда, где тонкая грань между мирами…"
    )

    for user in users:
        await bot.bot.send_message(chat_id=user, text=title)


async def time_15_25(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_belgrad_users()

    title = (
        f"☀ {_B('Дневные чудеса')}\n\n"
        f"Как только ступишь за ворота — начнётся волшебство. Сегодня выбор за тобой:\n\n"
        f"🔮 Если направо пойдёшь — к Бабе Яге: тайны гаданий приоткроют завесу судьбы.\n"
        f"🧵 Если налево — к Макоше: ткёт обереги из нитей и нежных желаний.\n"
        f"⚔ Прямо — застава Богатыря: испытания духа и силы (не опаздывай к встрече!).\n"
        f"🎲 Если вызов ты ищешь — Тайник сказок тебя ждёт: соберите дружину и "
        f"сразитесь смекалкой — кто первым назовёт сказку, тому и слава.\n"
        f"🍷 Если свернёшь к стойке Кощея — настойки крепкие, как его шутки, а истории такие, что ух…\n"
        f"🖌 В углу преображения — волшебные узоры на теле, а косы, как тропы сказки, вьются и ведут в чудный лес.\n\n"
        f"Все чудеса идут параллельно — следуй за зовом сердца.\n"
        f"Но помни: Богатырь ждёт вас в 14:30 и 16:30, а Тайник сказок шепнёт зов в 17:30 — не прозевайте!"
    )

    for user in users:
        await bot.bot.send_message(chat_id=user, text=title)


async def time_17_30(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_belgrad_users()

    title = (
        f"💨 {_B('Дымный час')}\n\n"
        f"Угли ровно дышат, кальяны прядут мягкие облака из трав, фруктов и ягод.\n"
        f"Там, где дым рисует кружевные узоры, всегда легко и приятно говорить о чём угодно."
    )

    for user in users:
        try:
            await bot.bot.send_message(chat_id=user, text=title)
        except Exception as e:
            continue

async def time_19_00(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_belgrad_users()

    title = (
        f"🥨 {_B('Ковёр-самобранец')}\n\n"
        f"Ковёр раскатился — на нём ряды яств разнообразных: тёплые, холодные, сладкие, солёные.\n"
        f"Берите тарелку, собирайте свой сет — добавки одобрены, у ковра запас бесконечный."
    )

    for user in users:
        try:
            await bot.bot.send_message(chat_id=user, text=title)
        except Exception as e:
            continue

async def time_19_50(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_belgrad_users()

    title = (
        f"🌒 {_B('Переход от дня к ночи')}\n\n"
        f"Вот и подходит час перемены. Деревня затаит дыхание… и преобразится.\n"
        f"Слушай, смотри, ощущай — это особенный миг. Скоро всё станет другим."
    )

    for user in users:
        try:
            await bot.bot.send_message(chat_id=user, text=title)
        except Exception as e:
            continue

async def time_20_00(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_belgrad_users()

    title = (
        f"🌌 {_B('Ночь приближается')}\n\n"
        f"С первыми звёздами начнётся иная глава.\n"
        f"То, что дремало днём, проснётся — ярко, смело, неожиданно.\n"
        f"Следи за вестями — сказка продолжается, и вечер откроет то, что днём было скрыто."
    )

    for user in users:
        try:
            await bot.bot.send_message(chat_id=user, text=title)
        except Exception as e:
            continue

async def time_20_30(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_belgrad_users()

    title = (
        f"🎤 {_B('20:30 — Караоке у Бабы Яги')}\n\n"
        f"В самой глуши, где звёзды подглядывают сквозь листву, "
        f"Баба Яга разводит огонь… и включает микрофон.\n"
        f"Ступай смело — здесь поют от души, а не по нотам."
    )

    for user in users:
        try:
            await bot.bot.send_message(chat_id=user, text=title)
        except Exception as e:
            continue

async def time_23_00(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_belgrad_users()

    title = (
        f"🔥 {_B('23:00 — Огонь собирает всех')}\n\n"
        f"Под конец пути, в самом сердце Балдёжкино, загорается Огонь — тёплый, зовущий, объединяющий.\n"
        f"Подходи ближе — здесь завершается путешествие. Здесь начинается общая история:\n"
        f"о взглядах в глаза, танцах и моменте, что останется с тобой навсегда."
    )

    for user in users:
        try:
            await bot.bot.send_message(chat_id=user, text=title)
        except Exception as e:
            continue

async def time_23_55(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_belgrad_users()

    title = (
        f"🌖 {_B('23:55 — первая повозка к городу')}\n\n"
        f"Кто готов — к месту посадки: повозка уже ждёт.\n"
        f"Домовой подскажет дорогу, следуйте указателям.\n"
        f"Остальные могут побалдеть ещё час — следующая отправка в 23:30."
    )

    for user in users:
        try:
            await bot.bot.send_message(chat_id=user, text=title)
        except Exception as e:
            continue

async def time_00_25(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_belgrad_users()

    title = (
        f"🌑 {_B('00:25 — последняя повозка домой')}\n\n"
        f"Уж полночь близится — сказка подходит к концу. Огонь угасает, деревня засыпает — до новой встречи.\n\n"
        f"Следуй за указателями — трансфер уже ждёт. Повозки готовы, не задерживайся.\n\n"
        f"Спасибо, что были с нами! Пусть Балдёжкино будет всегда с тобой."
    )

    for user in users:
        try:
            await bot.bot.send_message(chat_id=user, text=title)
        except Exception as e:
            continue

# ПОСТЫ 23.08

