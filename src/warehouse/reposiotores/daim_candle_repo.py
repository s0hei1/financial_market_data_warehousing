from sqlalchemy.ext.asyncio import AsyncSession


class DimCandleRepo:

    def __init__(self, session : AsyncSession):
        self.session = session

    def insert_candle(self, candle):
        pass
