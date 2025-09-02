from pyee.asyncio import AsyncIOEventEmitter
from src.events.jobs import first_run_configs
from src.events.events import Events

event_emitter = AsyncIOEventEmitter()

event_emitter.add_listener(Events.ON_START_UP,first_run_configs)

