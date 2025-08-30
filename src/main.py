from src.etl.fact_chart_etl import FactChartETL
import asyncio

if __name__ == '__main__':
    asyncio.run(FactChartETL().etl())