from datetime import UTC
from zoneinfo import ZoneInfo

from aiogram.utils.keyboard import InlineKeyboardBuilder
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from src.scheduler.groups.belgrad import day_22_08 as belgrad_22_08
from src.scheduler.groups.moscow import day_22_08 as moscow_22_08
from src.scheduler.groups.service import get_admin_users, get_users
from src.tgbot.formatter import _B, _A

scheduler = AsyncIOScheduler(timezone=UTC)


async def report(test: bool = False):
    from src.app import bot
    users = await get_admin_users() if test else await get_users()

    title = (
        f"🗣 {_B('Обратная связь')}\n\n"
        f"Говорят, что вчера было ТАК шумно, что лес да поляна ходуном ходили!\n\n"
        f"Если вы там были и мёд, и пиво пили, да и закусок не пропустили — "
        f"поделитесь с нами мнением о том, как всё прошло!\n\n"
        f"Каждый голос и мнение важны — чтобы в будущем делать круче!\n\n"
    )

    url = "https://forms.yandex-team.ru/ext/surveys/13777043"
    kb = InlineKeyboardBuilder()
    kb.button(text="🔗 Оставить отзыв", url=url)
    markup = kb.as_markup()

    for user in users:
        try:
            await bot.bot.send_message(chat_id=user, text=title, reply_markup=markup)
        except Exception as e:
            continue


async def run_test():
    await report(test=True)
    ...


scheduler.add_job(report, CronTrigger(day=23, hour=12, minute=00, timezone=ZoneInfo("Europe/Moscow")))
