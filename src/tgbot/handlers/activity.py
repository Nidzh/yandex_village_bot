from aiogram import F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.tgbot.formatter import _B
from src.tgbot.utils import smart_edit

router = Router()


@router.callback_query(F.data == "activity")
async def activity(callback, state, text, media):
    title = f"{_B('🎯 Активности:')}"

    kb = InlineKeyboardBuilder()
    kb.button(text="☀️ Явь (13:00–21:00)", callback_data="choice_activity:yav")
    kb.button(text="🌙 Навь (после 21:00)", callback_data="choice_activity:nav")
    kb.button(text=text.back, callback_data="main")
    kb.adjust(2, 1)

    await smart_edit(callback, title, kb, media=media.get("main.png"))


@router.callback_query(F.data.startswith("choice_activity:"))
async def choice_activity(callback, state, text, media):
    await callback.answer()
    zone = callback.data.split(":")[1]

    title = f"{_B('📍 Выберите зону:')}"

    kb = InlineKeyboardBuilder()
    kb.button(text="🌾 Поле Притопа", callback_data=f"get_activity:{zone}:1")
    kb.button(text="🌲 Тропы в Лесу", callback_data=f"get_activity:{zone}:2")
    kb.button(text="🧵 Прядильня", callback_data=f"get_activity:{zone}:3")
    kb.button(text="🎭 Игрища", callback_data=f"get_activity:{zone}:4")
    kb.button(text="🌊 Заводь грёз", callback_data=f"get_activity:{zone}:5")
    kb.button(text="👗 Нарядильня", callback_data=f"get_activity:{zone}:6")
    kb.button(text=text.back, callback_data="activity")
    kb.adjust(2, 2, 2, 1)

    await smart_edit(callback, title, kb, media=media.get("main.png"))


@router.callback_query(F.data.startswith("get_activity:"))
async def get_activity(callback, state, text, media):
    await callback.answer()
    zone = callback.data.split(":")[1]
    activity = int(callback.data.split(":")[2])

    match activity:
        case 1:
            match zone:
                case "yav":
                    title = (
                        f"🌿 На поляне — активные игры:\n"
                        f"🎯 колобоулинг\n"
                        f"🥾 нескороходы\n"
                        f"💻 ДДОС Атака\n"
                        f"🏘 городки\n"
                        f"🎈 петанк капитошками\n\n"
                        f"🤝 И встречи:\n"
                        f"⚔ богатырский турнир с Финистом Ясным Соколом\n"
                        f"🤼 командные форматы с Денницей\n"
                        f"🎤 выступления на сцене\n"
                        f"🍽 зона еды и бар"
                    )
                case "nav":
                    title = (
                        f"⏸ Поле уходит на паузу — здесь становится тихо.\n\n"
                        f"➡ Всё действие перемещается в другие зоны."
                    )

        case 2:
            match zone:
                case "yav":
                    title = (
                        f"🌞 В дневное время — активная зона с играми на ловкость.\n\n"
                        f"🏚 Можно заглянуть в шатёр Бабы-Яги, где проходят соревнования по {_B('Хоббимётлингу')} "
                        f"и головоломки от Кощея."
                    )
                case "nav":
                    title = (
                        f"🌙 Вечером лес меняется:\n"
                        f"🧙‍♀️ В шатре своём Баба-Яга чары творит и в будущее глядит."
                    )

        case 3:
            match zone:
                case "yav":
                    title = (
                        f"🛋 Зона для отдыха и общения:\n"
                        f"🎵 фоновая музыка\n"
                        f"🍹 бар\n"
                        f"💨 кальяны с 18:00\n\n"
                        f"📱 Здесь можно зарядить телефон,\n"
                        f"📸 запечатлеть себя на фотозоне,\n"
                        f"🥃 приготовить свою настойку,\n"
                        f"🔮 заглянуть в {_B('«волшебное блюдечко»')}\n"
                        f"😌 или просто почиллить рядом с Емелей."
                    )
                case "nav":
                    title = (
                        f"🪷 Прядильня становится тише — здесь проходят музыкальные медитации "
                        f"с ханго́м и глюкофоном."
                    )

        case 4:
            match zone:
                case "yav":
                    title = (
                        f"🪁 Зона с мастер-классом по созданию воздушных змеев,\n"
                        f"🍹 баром,\n"
                        f"🔌 возможностью зарядить телефон,\n"
                        f"🎒 оставить вещи,\n"
                        f"🌧 взять дождевик или бахилы.\n\n"
                        f"🛋 На веранде — чилл-зона."
                    )
                case "nav":
                    title = (
                        f"🧙‍♂️ Леший всех зовёт на {_B('ночной рейв')}.\n\n"
                        f"🛋 А на веранде включается {_B('«Клюковка понг»')} "
                        f"и открывается ледяной бар {_B('«Морозко»')}."
                    )

        case 5:
            match zone:
                case "yav":
                    title = (
                        f"🌞 Днём здесь — лёгкая программа с нетворкингом от Царевны-Лягушки,\n"
                        f"🍹 баром,\n"
                        f"🎵 музыкой от DJ,\n"
                        f"🔋 {_B('«бери заряд»')} для телефона\n"
                        f"💨 и кальянами с 18:00.\n\n"
                        f"🍽 А в большой веранде, в 19:00, для вас сготовится {_B('ужин знатный')}."
                    )
                case "nav":
                    title = (
                        f"🌙 Вечером — костёр со сказками,\n"
                        f"🕊 обряды от Жар-птицы\n"
                        f"🎸 и песни под гитару."
                    )

        case 6:
            match zone:
                case "yav":
                    title = (
                        f"🌞 Днём здесь проходят мастер-классы:\n"
                        f"📱 авоськи для телефона\n"
                        f"📿 браслеты из шармов и бусин\n\n"
                        f"🍴 Работают анимационная станция с едой,\n"
                        f"🍹 бар,\n"
                        f"📸 фото-зеркало\n"
                        f"🔋 зона {_B('«бери заряд»')}.\n\n"
                        f"✨ На {_B('Чародейской станции')} под руководством Марьи-Искусницы — украшения для волос, яркие тату, ленты и плетения.\n\n"
                        f"🎒 В гардеробе можно оставить вещи и взять дождевик или бахилы."
                    )
                case "nav":
                    title = (
                        f"🌙 Вечером {_B('Чародейская станция')} переходит в {_B('неоновый режим')}:\n"
                        f"✨ тату,\n"
                        f"🌸 веснушки,\n"
                        f"🎨 краски для лица и ресниц — всё, чтобы создать ночной образ."
                    )

    kb = InlineKeyboardBuilder()
    kb.button(text=text.back, callback_data=f"choice_activity:{zone}")
    kb.adjust(1)

    await smart_edit(callback, title, kb, media=media.get("main.png"))
