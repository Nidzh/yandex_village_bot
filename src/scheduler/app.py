from datetime import UTC
from zoneinfo import ZoneInfo

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from src.scheduler.groups.moscow._15_08 import _12_00, _16_00
from src.scheduler.groups.test import test

scheduler = AsyncIOScheduler(timezone=UTC)

# scheduler.add_job(test, trigger="interval", seconds=10)


scheduler.add_job(_12_00, CronTrigger(day=15, hour=12, minute=00, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(_16_00, CronTrigger(day=15, hour=16, minute=00, timezone=ZoneInfo("Europe/Moscow")))
