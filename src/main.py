from src.etl.dim_candle_etl import DimCandleETL
import asyncio

if __name__ == '__main__':
    asyncio.run(DimCandleETL().etl())