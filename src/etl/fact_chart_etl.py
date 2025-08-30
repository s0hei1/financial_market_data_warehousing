from prefect import task, flow
import pandas as pd
import asyncio
class FactChartETL:

    def __init__(self):
        pass


    @task(name='FactChartETL.extract()',log_prints=True)
    async def extract(self) -> pd.DataFrame:
        return pd.DataFrame()

    @task(name='FactChartETL.transform()',log_prints=True)
    async def transform(self, df : pd.DataFrame) -> pd.DataFrame:
        return df

    @task(name='FactChartETL.load()',log_prints=True)
    async def load(self, df : pd.DataFrame) -> None:
        print("FactChartETL.load() run")

    @flow(name = "FactChartETL.etl()")
    async def etl(self) -> None:
        df = await self.extract()
        df = await self.transform(df)
        await self.load(df)
        asyncio.sleep(2)





