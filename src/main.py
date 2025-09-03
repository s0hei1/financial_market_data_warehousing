import os
from typing import AnyStr
import sys

def get_current_path_parent(path: AnyStr, depth=1):
    if depth == 0:
        return path
    else:
        path = os.path.dirname(path)
        return get_current_path_parent(path=path, depth=depth - 1)

import asyncio
from datetime import datetime
from src.events.event_handler import event_emitter
from src.events.events import Events

async def start_up():
    event_emitter.emit(Events.ON_START_UP)

async def worker():
    elapsed_time = 0

    while True:

        current_minute = datetime.now().minute
        current_hour = datetime.now().hour
        current_day = datetime.now().day

        await asyncio.sleep(10 - elapsed_time)

        start_time = datetime.now().timestamp()

        if current_minute != datetime.now().minute:
            event_emitter.emit(Events.ON_MINUTE_CHANGED)

        if current_hour != datetime.now().hour:
            event_emitter.emit(Events.ON_HOUR_CHANGED)

        if current_day != datetime.now().day:
            event_emitter.emit(Events.ON_DAY_CHANGED)

        elapsed_time = datetime.now().timestamp() - start_time

async def run_app():
    await asyncio.gather(
        start_up(),
        worker()
    )

if __name__ == "__main__":
    sys.path.append(get_current_path_parent(path=os.path.abspath(__file__), depth=2))

    asyncio.run(run_app())

