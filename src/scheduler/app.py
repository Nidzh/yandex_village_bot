from datetime import UTC
from zoneinfo import ZoneInfo

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from src.scheduler.groups.moscow import day_19_08

scheduler = AsyncIOScheduler(timezone=UTC)

async def run_test():
    # await day_19_08.time_13_00(test=True)
    # await day_19_08.time_15_00(test=True)
    # await day_19_08.time_17_00(test=True)
    # await day_19_08.time_18_00(test=True)
    ...

scheduler.add_job(day_19_08.time_13_00, CronTrigger(day=19, hour=13, minute=00, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(day_19_08.time_15_00, CronTrigger(day=19, hour=15, minute=00, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(day_19_08.time_17_00, CronTrigger(day=19, hour=17, minute=00, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(day_19_08.time_18_00, CronTrigger(day=19, hour=18, minute=00, timezone=ZoneInfo("Europe/Moscow")))
