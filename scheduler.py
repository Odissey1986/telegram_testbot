from config import DECREASE_PARAMS as dpar, TIME_INTERVAL
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from db import pets

scheduler = AsyncIOScheduler()

def start_scheduler():
    scheduler.add_job(decrease_params, trigger=IntervalTrigger(seconds=TIME_INTERVAL))
    scheduler.start()

async def decrease_params():
    for pet in pets.values():
        hun = pet['hunger'] + dpar['hunger']
        en = pet['energy'] + dpar['energy']
        hap = pet['happiness'] + dpar['happiness']

        hun = max(min(hun, 100), 0)
        en = max(min(en, 100), 0)
        hap = max(min(hap, 100), 0)

        pet['hunger'] = hun
        pet['energy'] = en
        pet['happiness'] = hun

        # print(hun, en, hap)