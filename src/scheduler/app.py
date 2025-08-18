from datetime import UTC
from zoneinfo import ZoneInfo

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from src.scheduler.groups.moscow._18_08 import _12_00

scheduler = AsyncIOScheduler(timezone=UTC)

# scheduler.add_job(test, trigger="interval", seconds=10)


scheduler.add_job(_12_00, CronTrigger(day=18, hour=12, minute=00, timezone=ZoneInfo("Europe/Moscow")))
