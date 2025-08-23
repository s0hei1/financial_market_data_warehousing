from enum import Enum
from functools import lru_cache
from typing import NamedTuple
import MetaTrader5 as mt5
from dataclasses import dataclass
from operator import attrgetter
from more_itertools import first

@dataclass(frozen=True)
class TimeFrameModel:
    name : str
    mt5_value : int
    included_m1 : int

class TimeFrameEnum(Enum):
    M1 = TimeFrameModel(name="m1", mt5_value=mt5.TIMEFRAME_M1, included_m1=1)
    M5 = TimeFrameModel(name="m5", mt5_value=mt5.TIMEFRAME_M5, included_m1=5)
    M15 = TimeFrameModel(name="m15", mt5_value=mt5.TIMEFRAME_M15, included_m1=15)
    H1 = TimeFrameModel(name="h1", mt5_value=mt5.TIMEFRAME_H1, included_m1=60)
    H4 = TimeFrameModel(name="h4", mt5_value=mt5.TIMEFRAME_H4, included_m1=240)
    Daily = TimeFrameModel(name="daily", mt5_value=mt5.TIMEFRAME_D1, included_m1=1440)
    Weekly = TimeFrameModel(name="weekly", mt5_value=mt5.TIMEFRAME_W1, included_m1=10080)
    Monthly = TimeFrameModel(name="monthly", mt5_value=mt5.TIMEFRAME_MN1, included_m1=43200)

    @classmethod
    @lru_cache
    def get_time_frame_by_mt5_value(cls, mt5_value: int) -> 'TimeFrameEnum | None':
        return first([i for i in TimeFrameEnum if i.value.mt5_value == mt5_value], default=None)

    @classmethod
    @lru_cache
    def get_time_frame_by_name(self, name: str) -> 'TimeFrameEnum | None':
        return first([i for i in TimeFrameEnum if i.value.name == name], default=None)

