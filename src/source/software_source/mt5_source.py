import MetaTrader5 as mt5
from src.source.software_source.enums import TimeFrameEnum
from src.source.software_source.exception import MetaTraderIOException
from src.source.software_source.mt5_result import Mt5Result, LastErrorResult, LastTickResult
from typing import Callable, TypeVar, ParamSpec
from functools import wraps
import datetime as dt
from third_party.candlestic.candle import Candle
from operator import itemgetter

from third_party.candlestic.chart import Chart
from third_party.candlestic.symbol import Symbol

P = ParamSpec("P")
T = TypeVar("T")


def mt5_last_error() -> LastErrorResult:
    lasterror = mt5.last_error()
    return LastErrorResult(
        message=lasterror[1],
        result_code=lasterror[0]
    )


def _mt5_initialize(func: Callable[P, Mt5Result[T | None]]) -> Callable[P, Mt5Result[T | None]]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> Mt5Result[T | None]:
        init_result = mt5.initialize()
        if not init_result:
            _last_error = mt5_last_error()
            return Mt5Result(
                has_error=True,
                message=_last_error.message,
                result_code=_last_error.result_code,
                result=None,
            )

        try:
            return func(*args, **kwargs)
        except MetaTraderIOException:
            _last_error = mt5_last_error()
            return Mt5Result(
                has_error=True,
                message=_last_error.message,
                result_code=_last_error.result_code,
                result=None,
            )

    return wrapper


@_mt5_initialize
def get_market_historical_data(
        symbol: str,
        timeframe: TimeFrameEnum,
        date_from: dt.datetime,
        date_to: dt.datetime,
) -> Mt5Result[Chart | None]:
    result = mt5.copy_rates_range(
        symbol,
        timeframe.value.mt5_value,
        date_from,
        date_to,
    )
    _last_error = mt5.last_error()
    if result is None and mt5.last_error()[0] != 1:
        raise MetaTraderIOException(message=_last_error[1], code=_last_error[0], )

    o = itemgetter(1)
    h = itemgetter(2)
    l = itemgetter(3)
    c = itemgetter(4)
    timestamp = itemgetter(0)

    chart = Chart(
        candles=[
            Candle(
                open=o(i),
                high=h(i),
                low=l(i),
                close=c(i),
                datetime=dt.datetime.fromtimestamp(timestamp(i), dt.UTC),
            ) for i in result
        ],
        time_frame=timeframe.value.name
    )

    return Mt5Result(
        has_error=False,
        message=_last_error[0],
        result_code=_last_error[1],
        result=chart,
    )


@_mt5_initialize
def get_symbol_current_price(symbol: Symbol) -> Mt5Result[float]:
    result = mt5.symbol_info_tick(symbol.symbol_fullname)
    _last_error = mt5_last_error()

    bid = itemgetter(1)
    ask = itemgetter(2)

    last_tick_result = LastTickResult(
        bid=bid(result),
        ask=ask(result)
    )

    return Mt5Result(
        has_error=False,
        message=_last_error.message,
        result_code=_last_error.result_code,
        result=last_tick_result
    )


print(get_symbol_current_price(
    symbol=Symbol(
        "EUR",
        "USD",
        suffix='b'
    )
)
)
