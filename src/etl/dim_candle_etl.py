import datetime as dt
from prefect import task, flow
import pandas as pd
import asyncio
from src.etl.etl_exceptions import ETLException
from third_party.candlestic.chart import Chart
from third_party.candlestic.symbol import Symbol
from third_party.candlestic.time_frame import TimeFrame
from src.data_source.software_source.mt5 import mt5_source


class DimCandleETL:

    def __init__(self  ):
        pass

    @task(name='FactChartETL.extract()', log_prints=True)
    async def extract(
            self, symbol: Symbol,
            time_frame: TimeFrame,
            date_from: dt.datetime,
            date_to: dt.datetime) -> Chart:
        mt5_result = mt5_source.get_market_historical_data(
            symbol,
            time_frame,
            date_from,
            date_to
        )
        if mt5_result.has_error:
            raise ETLException(mt5_result.message)

        return mt5_result.result


    @task(name='FactChartETL.transform()', log_prints=True)
    async def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return df

    @task(name='FactChartETL.load()', log_prints=True)
    async def load(self, df: pd.DataFrame) -> None:
        print("FactChartETL.load() run")

    @flow(name="FactChartETL.etl()")
    async def etl(self) -> None:
        df = await self.extract()
        df = await self.transform(df)
        await self.load(df)
        asyncio.sleep(2)
