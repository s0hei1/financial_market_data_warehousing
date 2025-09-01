from sqlalchemy import select, exists
from sqlalchemy.ext.asyncio import AsyncSession
from src.warehouse.models import Flags


class FlagsRepo:

    def __init__(self, session : AsyncSession) -> None:
        self.session = session

    async def config_flags(self) -> Flags:

        query_result = await self.session.execute(
            select(Flags).where(Flags.id == 1)
        )
        result = query_result.scalar_one_or_none()
        if result is not None:
            return result

        flag = Flags(
            id = 1,
            is_first_run = True
        )
        self.session.add(flag)
        await self.session.commit()
        await self.session.refresh(flag)

        return flag

    async def is_first_run(self) -> bool:
        query_result = await self.session.execute(
            select(Flags.is_first_run).where(Flags.id == 1)
        )
        result = query_result.scalar_one_or_none()
        if result is not None:
            return result

        return False
