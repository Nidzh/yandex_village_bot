from datetime import UTC
from zoneinfo import ZoneInfo

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from src.scheduler.groups.belgrad import day_22_08 as belgrad_22_08
from src.scheduler.groups.moscow import day_22_08 as moscow_22_08

scheduler = AsyncIOScheduler(timezone=UTC)

async def run_test():
    # await moscow_22_08.time_13_00(test=True)
    # await moscow_22_08.time_13_30(test=True)
    # await moscow_22_08.time_13_50(test=True)
    # await moscow_22_08.time_14_00(test=True)
    # await moscow_22_08.time_14_50(test=True)
    # await moscow_22_08.time_15_10(test=True)
    # await moscow_22_08.time_15_20(test=True)
    # await moscow_22_08.time_15_30(test=True)
    # await moscow_22_08.time_15_50(test=True)
    # await moscow_22_08.time_17_50(test=True)
    # await moscow_22_08.time_17_55(test=True)
    # await moscow_22_08.time_18_00(test=True)
    # await moscow_22_08.time_19_20(test=True)
    # await moscow_22_08.time_19_30(test=True)
    # await moscow_22_08.time_20_30(test=True)
    # await moscow_22_08.time_01_00(test=True)
    ...


# BELGRAD 22.08
scheduler.add_job(belgrad_22_08.time_12_30, CronTrigger(day=22, hour=12, minute=30, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(belgrad_22_08.time_14_30, CronTrigger(day=22, hour=14, minute=30, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(belgrad_22_08.time_14_55, CronTrigger(day=22, hour=14, minute=55, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(belgrad_22_08.time_15_25, CronTrigger(day=22, hour=15, minute=25, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(belgrad_22_08.time_17_30, CronTrigger(day=22, hour=17, minute=30, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(belgrad_22_08.time_19_00, CronTrigger(day=22, hour=19, minute=00, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(belgrad_22_08.time_19_50, CronTrigger(day=22, hour=19, minute=50, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(belgrad_22_08.time_20_00, CronTrigger(day=22, hour=20, minute=00, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(belgrad_22_08.time_20_30, CronTrigger(day=22, hour=20, minute=30, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(belgrad_22_08.time_23_00, CronTrigger(day=22, hour=23, minute=00, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(belgrad_22_08.time_23_55, CronTrigger(day=22, hour=23, minute=55, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(belgrad_22_08.time_00_25, CronTrigger(day=23, hour=00, minute=25, timezone=ZoneInfo("Europe/Moscow")))

# MOSCOW 22.08
scheduler.add_job(moscow_22_08.time_13_00, CronTrigger(day=22, hour=13, minute=00, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(moscow_22_08.time_13_30, CronTrigger(day=22, hour=13, minute=30, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(moscow_22_08.time_13_50, CronTrigger(day=22, hour=13, minute=50, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(moscow_22_08.time_14_00, CronTrigger(day=22, hour=14, minute=00, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(moscow_22_08.time_14_50, CronTrigger(day=22, hour=14, minute=50, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(moscow_22_08.time_15_10, CronTrigger(day=22, hour=15, minute=10, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(moscow_22_08.time_15_20, CronTrigger(day=22, hour=15, minute=20, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(moscow_22_08.time_15_30, CronTrigger(day=22, hour=15, minute=30, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(moscow_22_08.time_15_50, CronTrigger(day=22, hour=15, minute=50, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(moscow_22_08.time_17_50, CronTrigger(day=22, hour=17, minute=50, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(moscow_22_08.time_17_55, CronTrigger(day=22, hour=17, minute=55, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(moscow_22_08.time_18_00, CronTrigger(day=22, hour=18, minute=00, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(moscow_22_08.time_19_20, CronTrigger(day=22, hour=19, minute=20, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(moscow_22_08.time_19_30, CronTrigger(day=22, hour=19, minute=30, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(moscow_22_08.time_20_30, CronTrigger(day=22, hour=20, minute=30, timezone=ZoneInfo("Europe/Moscow")))
scheduler.add_job(moscow_22_08.time_01_00, CronTrigger(day=23, hour=1, minute=00, timezone=ZoneInfo("Europe/Moscow")))
