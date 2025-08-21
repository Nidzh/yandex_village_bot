from datetime import UTC
from zoneinfo import ZoneInfo

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from src.scheduler.groups.moscow import day_21_08

scheduler = AsyncIOScheduler(timezone=UTC)

async def run_test():
    await day_21_08.time_12_00(test=True)
    await day_21_08.time_16_00(test=True)
    await day_21_08.time_18_00(test=True)
    ...

scheduler.add_job(day_21_08.time_12_00, CronTrigger(day=21, hour=12, minute=5, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(day_21_08.time_16_00, CronTrigger(day=21, hour=16, minute=00, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(day_21_08.time_18_00, CronTrigger(day=21, hour=18, minute=00, timezone=ZoneInfo("Europe/Moscow")))
