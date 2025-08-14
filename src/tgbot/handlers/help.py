from aiogram import F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.tgbot.formatter import _B, _A
from src.tgbot.utils import smart_edit

router = Router()


@router.callback_query(F.data == "help")
async def help(callback, state, text):
    title = f"{_B('🐱 Котопомощь:')}"

    kb = InlineKeyboardBuilder()
    kb.button(text="📱 Где можно подзарядить телефон?", callback_data=f"faq:1")
    kb.button(text="⏰ Во сколько заканчивается мероприятие?", callback_data=f"faq:2")
    kb.button(text="🚌 Автобусы обратно – где и когда?", callback_data=f"faq:3")
    kb.button(text="🚐 Как доехать до площадки?", callback_data=f"faq:4")
    kb.button(text="🍽 Где можно поесть?", callback_data=f"faq:5")
    kb.button(text="🎒 Что взять с собой?", callback_data=f"faq:6")
    kb.button(text="🚗 Есть ли парковка?", callback_data=f"faq:7")
    kb.button(text="📅 Где посмотреть расписание активностей?", callback_data=f"faq:8")
    kb.button(text="🗺 Как работает голосовая навигация?", callback_data=f"faq:9")
    kb.button(text="🆘 Что делать, если потерялся друг или вещь?", callback_data=f"faq:10")
    kb.button(text="🙋 Если FAQ не помог", callback_data=f"faq:11")
    kb.button(text=text.back, callback_data="main")
    kb.adjust(1)

    await smart_edit(callback, title, kb)


@router.callback_query(F.data.startswith("faq:"))
async def choice_activity(callback, state, text):
    await callback.answer()
    question = int(callback.data.split(":")[1])

    match question:
        case 1:
            title = (
                f"🔋 Зарядки есть в зонах «Нарядильня», «Игрища», «Прядильня», "
                f"«Заводь грёз», «Поле Притопа».\nИщи станции {_B('«Бери заряд»')}."
            )
        case 2:
            title = (
                f"🌙 {_B('«Явь и Навь»')} завершается в 02:00.\n\n"
                f"🚌 В 23:00 автобусы начнут забирать гостей обратно.\n"
                f"Если останешься до конца — поймаешь самую тёплую Навь."
            )
        case 3:
            title = (
                f"🌙 {_B('«Явь и Навь»')} завершается в 02:00.\n\n"
                f"🚌 В 23:00 автобусы начнут забирать гостей обратно.\n"
                f"Если останешься до конца — поймаешь самую тёплую Навь."
            )
        case 4:
            title = (
                f"ℹ Информацию о трансфере и маршруте ты можешь получить, "
                f"нажав кнопку {_B('Трансфер')} в главном меню.\n\n"
                f"📌 Кнопка {_B('Трансфер')} прикреплена к сообщению."
            )
        case 5:
            title = (
                f"🍴 На {_B('«Поле Притопа»')} тебя ждёт {_B('«Скатерть Самобранка»')}.\n\n"
                f"Также еду и барные напитки можно найти в «Игрищах», «Нарядильне», "
                f"«Прядильне» и «Заводи Грёз».\n\n"
                f"🍽 Вечерний ужин будет ждать тебя в «Заводи Грёз» "
                f"на большой веранде в 19:00."
            )
        case 6:
            title = (
                f"👟 Возьми удобную обувь,\n"
                f"🧢 головной убор от солнца\n"
                f"💧 и бутылку воды.\n\n"
                f"Мы позаботимся о теневых зонах, но день может быть жарким."
            )
        case 7:
            title = (
                f"🅿 Да, парковка есть, но мест немного.\n\n"
                f"🚐 Лучше оставить авто дома, приехать на трансфере "
                f"и не отказывать себе в бокале игристого или пенного 😉."
            )
        case 8:
            title = (
                f"🗓 Всё расписание — в чат-боте, в разделах {_B('Активности')} и {_B('Программа')}.\n\n"
                f"Там можно выбрать локацию и посмотреть, что происходит прямо сейчас."
            )
        case 9:
            title = (
                f"🔊 На площадке расставлены колонки, из которых звучат голосовые подсказки "
                f"от меня, Кота Учёного.\n\n"
                f"Они помогают найти зоны и переключиться между {_B('Явью')} и {_B('Навью')}.\n"
                f"Просто прислушайся — я подскажу путь."
            )
        case 10:
            title = (
                f"📩 Напиши в чат-бот в раздел {_B('Котопомощь')} или подойди к гардеробу "
                f"в зоне {_B('Нарядильня')}.\n\n"
                f"Мы постараемся быстро помочь."
            )
        case 11:
            title = (
                f"💬 {_B('Опишите свою проблему')} и отправьте сообщение оператору.\n\n"
                f"👤 TG: {_A('@marivalleri', 'https://t.me/marivalleri')}"
            )

    kb = InlineKeyboardBuilder()
    kb.button(text=text.back, callback_data="help")
    kb.adjust(1)

    await smart_edit(callback, title, kb)
