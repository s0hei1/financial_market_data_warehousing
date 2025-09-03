
from dependency_injector import containers,providers
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from dependency_injector.providers import Factory
from sqlalchemy.orm import sessionmaker
from src.tools.config.settings import settings
from src.warehouse.db import get_db
from src.warehouse.reposiotores.flags_repo import FlagsRepo


class Container:


    @classmethod
    async def flags_repo(cls) -> FlagsRepo:
        session = await get_db()
        return FlagsRepo(session = session)


