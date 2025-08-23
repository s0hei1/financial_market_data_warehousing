import MetaTrader5 as mt5
from MetaTrader5 import last_error

from src.source.software_source.enums import TimeFrameEnum
from src.source.software_source.exception import MetaTraderIOException
from src.source.software_source.mt5_result import Mt5Result
from third_party.candlestic.chart import Chart
from typing import Callable, TypeVar, ParamSpec
from functools import wraps
import datetime as dt

P = ParamSpec("P")
T = TypeVar("T")

def _check_init_decor(func: Callable[P, Mt5Result[T]]) -> Callable[P, Mt5Result[T]]:

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> Mt5Result[T]:
        init_result = mt5.initialize()
        if not init_result:
            last_error = mt5.last_error()
            return Mt5Result(
                has_error=True,
                message=last_error[1],
                result_code=last_error[0],
                result=None,
            )

        try:
            return func(*args, **kwargs)
        except MetaTraderIOException:
            last_error = mt5.last_error()
            return Mt5Result(
                has_error=True,
                message=last_error[1],
                result_code=last_error[0],
                result=None,
            )

    return wrapper

@_check_init_decor
def get_market_historical_data(
        symbol: str,
        timeframe: TimeFrameEnum,
        date_from : dt.datetime,
        date_to : dt.datetime,
) -> Mt5Result[Chart]:
    result = mt5.copy_rates_range(
        symbol,
        timeframe.value.mt5_value,
        date_from,
        date_to,
    )
    last_error = mt5.last_error()
    if result is None and mt5.last_error()[0] != 1:
        raise MetaTraderIOException(message=last_error[1],code=last_error[0],)

    candles = [i for i in result]

    return Mt5Result(
        has_error=False,
        message=last_error[0],
        result_code=last_error[1],
        result=Chart(
            candles=candles,
            time_frame=timeframe.value.name,
        ),
    )


print(get_market_historical_data())