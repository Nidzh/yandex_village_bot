import asyncio

from aiogram.types import InputMediaPhoto, InputMediaVideo
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.scheduler.groups.service import load_media, get_moscow_users, get_admin_users
from src.tgbot.formatter import _B, _A


# 13:00 — Привет на сказочном Open Air  (media: 22_08_13_00.jpg)
async def time_13_00(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"👋 {_B('Добро пожаловать в Сказку!')}\n\n"
        f"Весь этот день — для веселья, плясок да потех. Встречайтесь с волшебными персонажами, "
        f"соревнуйтесь в играх, делайте совместные фото и отправляйте их в бот.\n\n"
        f"Вас ждут 6 основных зон:\n"
        f"• {_B('«Поле Притопа»')} — здесь главная сцена и шоу от ваших коллег, не пропустите!\n"
        f"• {_B('«Тропы в лесу»')} — тут для вас Баба-Яга и Кощей игры приготовили, заглядывайте.\n"
        f"• {_B('«Прядильня»')} — тут Емеля лежит-отдыхает, а вы можете вместе с ним поваляться, "
        f"настойки поделать да кальян подымить с 18:00.\n"
        f"• {_B('«Игрища»')} — танцуйте, чилльте, общайтесь и создавайте своего Змея Горыныча!\n"
        f"• {_B('«Заводь грёз»')} — поболтайте с Царевной-лягушкой, потанцуйте под сказочные биты "
        f"и угощайтесь кушаньем вечерним!\n"
        f"• {_B('«Нарядильня»')} — Марья-Искусница подготовила мастер-классы, а Василиса Прекрасная поможет дополнить образ."
    )

    for user in users:
        await bot.bot.send_animation(
            chat_id=user,
            animation=media["22_08_12_00.mp4"],
            caption=title,
        )


# 13:30 — Механика работы гардероба  (media: 22_08_13_30.jpg)
async def time_13_30(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"🧥 {_B('Механика работы гардероба')}\n\n"
        f"В сказке много интересного, а таскать с собой одежду и рюкзаки не хочется?\n"
        f"Всё продумано! В зонах {_B('«Игрища»')} и {_B('«Нарядильня»')} вас ждут гардероб и камеры хранения.\n\n"
        f"Чтобы получить свой уникальный номерок, зайдите в меню бота и нажмите кнопку {_B('Гардероб')}.\n\n"
        f"Если ваш номер — {_B('от 1 до 500')}, оставляйте вещи в {_B('«Нарядильне»')}.\n"
        f"Если {_B('от 501 до 1000')}, ваши вещи будут надёжно храниться в зоне {_B('«Игрища»')}.\n\n"
        f"После — налегке отправляйтесь исследовать наш сказочный мир."
    )

    kb = InlineKeyboardBuilder()
    kb.button(text="🧥 Гардероб", callback_data="wardrobe")
    markup = kb.as_markup()

    for user in users:
        await bot.bot.send_photo(
            chat_id=user,
            photo=media["22_08_13_30.jpg"],
            caption=title,
            reply_markup=markup,
        )


# 13:50 — Конкурс костюмов  (без медиа в списке — сообщение)
async def time_13_50(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()

    title = (
        f"✨ {_B('Конкурс костюмов')}\n\n"
        f"Парни удалые да девицы красные! Приехали в ярких и стильных образах? Тогда айда участвовать!\n\n"
        f"Сделайте фото своего костюма и загрузите через бот {_B('до 17:00')}.\n\n"
        f"А в 19:30 подведём итоги и наградим тех, за кого коллеги отдадут больше всего голосов. Дерзайте!"
    )

    kb = InlineKeyboardBuilder()
    kb.button(text="📸 Мой костюм", callback_data="answer:costume")
    markup = kb.as_markup()

    for user in users:
        await bot.bot.send_message(chat_id=user, text=title, reply_markup=markup)


# 14:00 — Активности  (media: 22_08_14_00.mp4)
async def time_14_00(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"🎛 {_B('Активности')}\n\n"
        f"Глаза разбегаются и не знаете, чем заняться? Не переживайте!\n"
        f"Нажмите в боте кнопку {_B('Программа активностей')} и выберите локацию — "
        f"узнаете, что там проходит, и ничего интересного не пропустите.\n\n"
        f"Приключения ждут — не заставляйте их ждать!"
    )

    kb = InlineKeyboardBuilder()
    kb.button(text="🎯 Активности", callback_data="activity")
    markup = kb.as_markup()

    for user in users:
        await bot.bot.send_video(
            chat_id=user,
            video=media["22_08_14_00.mp4"],
            caption=title,
            reply_markup=markup,
        )


# 14:50 — Старт программы на сцене  (media: 22_08_14_50.png)
async def time_14_50(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"🎭 {_B('Старт программы на сцене')}\n\n"
        f"Люд честной! Уже через 10 минут на {_B('«Поле Притопа»')} начнётся долгожданная программа.\n"
        f"Сцена оживёт — сюрпризы от ТОПов компании и потехи разные. Не пропустите!"
    )

    for user in users:
        await bot.bot.send_photo(
            chat_id=user,
            photo=media["22_08_14_50.png"],
            caption=title,
        )


# 15:10 — Сказочная трансляция  (media: 22_08_15_10.jpg)
async def time_15_10(test: bool = False, stream_url: str = "https://vkvideo.ru/video1066141499_456239039"):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"📺 {_B('Сказочная трансляция')}\n\n"
        f"Чудо чудное, диво дивное! Можно отдыхать в любой зоне и всё равно знать, что происходит на главной сцене.\n"
        f"Переходите по ссылке и смотрите трансляцию с {_B('«Поля Притопа»')} из любого места нашего Open Air:\n"
    )

    kb = InlineKeyboardBuilder()
    kb.button(text="▶️ Смотреть трансляцию", url=stream_url)
    markup = kb.as_markup()

    for user in users:
        await asyncio.sleep(0.1)
        await bot.bot.send_photo(
            chat_id=user,
            photo=media["22_08_15_10.jpg"],
            caption=title,
            reply_markup=markup,
        )


# 15:20 — Хор Яви (альбом)  (media: 22_08_15_20_0.png … 22_08_15_20_6.jpg)
async def time_15_20(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"🎶 {_B('Хор Яви')}\n\n"
        f"Ох и любо петь на природе, а ещё лучше — вместе с коллегами!\n"
        f"Присоединяйтесь на {_B('«Поле Притопа»')} через 10 минут — споём любимые песни и единство своё покажем.\n"
        f"Если слова подзабылись — не беда, всё подготовлено в карточках ниже."
    )


    photos = [
        InputMediaPhoto(media=media["22_08_15_20_0.png"], caption=title),
        InputMediaPhoto(media=media["22_08_15_20_1.jpg"]),
        InputMediaPhoto(media=media["22_08_15_20_2.jpg"]),
        InputMediaPhoto(media=media["22_08_15_20_3.jpg"]),
        InputMediaPhoto(media=media["22_08_15_20_4.jpg"]),
        InputMediaPhoto(media=media["22_08_15_20_5.jpg"]),
        InputMediaPhoto(media=media["22_08_15_20_6.jpg"]),
    ]

    for user in users:
        await asyncio.sleep(0.1)
        await bot.bot.send_media_group(chat_id=user, media=photos)


async def time_15_25(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"🐾 {_B('Кот Учёный мурчит из Прядильни')}: \n\n"
        f"Если вдруг захочется передохнуть от игрищ да весёлой суеты, знайте: "
        f"в {_B('Прядильне')} есть тихие комнаты.\n\n"
        f"Уютные, как берлога Емели, и тихие, как шёпот лесных существ. "
        f"Там можно спокойно поговорить, поработать или просто перевести дух."
    )

    for user in users:
        await asyncio.sleep(0.1)
        await bot.bot.send_message(
            chat_id=user,
            text=title,
        )


# 15:30 — Минута славы!  (media: 22_08_15_30.jpg)
async def time_15_30(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"🌟 {_B('Минута славы!')}\n\n"
        f"Торопитесь, не пропустите! Через 10 минут на {_B('«Поле Притопа»')} "
        f"выступят ваши коллеги с номерами затейливыми да песнями заводными.\n"
        f"Поддержите их и повеселитесь от души!"
    )

    for user in users:
        await asyncio.sleep(0.1)
        await bot.bot.send_photo(
            chat_id=user,
            photo=media["22_08_15_30.jpg"],
            caption=title,
        )


# 15:50 — Выдача мерча  (media: 22_08_15_50.jpg)
async def time_15_50(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"🎁 {_B('Выдача мерча')}\n\n"
        f"Кот Учёный приготовил вам подарок! Отправляйтесь в зоны {_B('«Игрища»')} и {_B('«Нарядильня»')} — "
        f"получите уникальный мерч по номерку из гардероба.\n"
        f"Спешите: такую красоту разбирают быстро! Времени отведено {_B('до полуночи')}."
    )

    for user in users:
        await asyncio.sleep(0.1)
        await bot.bot.send_photo(
            chat_id=user,
            photo=media["22_08_15_50.jpg"],
            caption=title,
        )


# 17:50 — Запускаем Горынычей!  (media: 22_08_17_50.png)
async def time_17_50(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"🪁 {_B('Запускаем Горынычей!')}\n\n"
        f"Сегодня запустим в небо множество добрых Змеев Горынычей.\n"
        f"Через 10 минут на {_B('«Поле Притопа»')} стартует фестиваль воздушных змеев.\n"
        f"Если уже собрали своего — приходите, запустим их в небо вместе!"
    )

    for user in users:
        await asyncio.sleep(0.1)
        await bot.bot.send_photo(
            chat_id=user,
            photo=media["22_08_17_50.png"],
            caption=title,
        )


# 17:55 — Квест от Кощея  (media: 22_08_17_55.png)
async def time_17_55(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"🗝 {_B('Квест от Кощея')}\n\n"
        f"Чу! У избушки Бабы-Яги Кощей ждёт команды от {_B('2 до 7')} человек на квест загадочный.\n"
        f"Осмелитесь ли вызов принять и выиграть дар дивный — зелье лесное, волшебное?\n"
        f"Собирайтесь скорее: уже через {_B('5 минут')} начинаем!"
    )

    for user in users:
        await asyncio.sleep(0.1)
        await bot.bot.send_photo(
            chat_id=user,
            photo=media["22_08_17_55.png"],
            caption=title,
        )


# 18:00 — Голосование за лучший костюм  (со ссылкой)
async def time_18_00(test: bool = False, vote_url: str = "https://forms.yandex.ru/surveys/13776743.9670907e4910fae1fb04a8777509fb8a98f56aa9"):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()

    title = (
        f"🗳 {_B('Голосование за лучший костюм')}\n\n"
        f"Други наши, мы собрали все ваши потрясающие костюмы и объявляем начало голосования!\n"
        f"Перейдите по ссылке ниже и проголосуйте в трёх номинациях:\n\n"
        f"1. {_B('«Сказочная краса»')} — самый позитивный и вайбовый образ.\n\n"
        f"{_B('«Любо миру, любо людям»')} — приз зрительских симпатий.\n\n"
        f"{_B('«Диво дивное, чудо чудное»')} — самый оригинальный и неожиданный костюм.\n\n"
        f"Делайте выбор до {_B('19:10')}. А в 19:30 — награждение у главной сцены!\n\n"
    )

    kb = InlineKeyboardBuilder()
    kb.button(text="🗳 Голосование", url=vote_url)
    markup = kb.as_markup()

    for user in users:
        await asyncio.sleep(0.1)
        await bot.bot.send_message(chat_id=user, text=title, reply_markup=markup)


# 19:20 — Награждение конкурса костюмов  (media: 22_08_19_20.jpg)
async def time_19_20(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"🏆 {_B('Награждение конкурса костюмов')}\n\n"
        f"Братцы и сестрицы! Собираемся скорее на {_B('«Поле Притопа»')}.\n"
        f"Через 10 минут будем награждать победителей. Не пропустите — вдруг именно вам достанется приз диковинный!"
    )

    for user in users:
        await asyncio.sleep(0.1)
        await bot.bot.send_photo(
            chat_id=user,
            photo=media["22_08_19_20.jpg"],
            caption=title,
        )


# 19:30 — Пора плясать!  (media: 22_08_19_30.mp4)
async def time_19_30(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"🕺 {_B('Пора плясать!')}\n\n"
        f"В нашей сказке есть не только персонажи волшебные, но и музыканты сказочные!\n"
        f"Через 10 минут на {_B('«Поле Притопа»')} выступает группа {_B('«Хвоя»')} — ноги сами в пляс пойдут!"
    )

    for user in users:
        await asyncio.sleep(0.1)
        await bot.bot.send_video(
            chat_id=user,
            video=media["22_08_19_30.mp4"],
            caption=title,
        )


# 20:30 — Явь к закату — Навь к восходу  (media: 22_08_20_30.png)
async def time_20_30(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"🌇 {_B('Явь к закату — Навь к восходу')}\n\n"
        f"Весело было под солнцем ясным в Яви. Но скоро придёт Навь — и сказка преобразится.\n"
        f"Не пропустите мистический миг: встречаемся через 10 минут на {_B('«Поле Притопа»')}."
    )

    for user in users:
        await asyncio.sleep(0.1)
        await bot.bot.send_photo(
            chat_id=user,
            photo=media["22_08_20_30.png"],
            caption=title,
        )


# 01:00 — Летопись Яви и Нави  (media: 22_08_01_00.jpg)
async def time_01_00(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_moscow_users()
    media = load_media()

    title = (
        f"📜 {_B('Летопись Яви и Нави')}\n\n"
        f"Затерялись мы в краях Яви и Нави — и сказке приходит конец.\n\n"
        f"Дорогие гости {_B('Open Air Яндекс Вертикалей')}, сегодня мы с вами не просто провели время — "
        f"мы вместе сплели настоящую сказку! Спасибо за улыбки, смех и энергию.\n\n"
        f"А чтобы собрать летопись славную об этом дне, перейдите в раздел {_B('Летопись')} "
        f"и ответьте всего на 5 простых вопросов."
    )

    for user in users:
        await asyncio.sleep(0.1)
        await bot.bot.send_photo(
            chat_id=user,
            photo=media["22_08_01_00.jpg"],
            caption=title,
        )
