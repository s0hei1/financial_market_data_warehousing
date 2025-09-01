from enum import Enum

class Events(Enum):
    ON_FIRST_RUN = "on_first_run"
    ON_START_UP = "on_start_up"
    ON_MINUTE_CHANGED = "on_minute_changed"
    ON_HOUR_CHANGED = "on_hour_changed"
    ON_DAY_CHANGED = "on_day_changed"
