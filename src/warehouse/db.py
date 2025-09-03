from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker
from src.tools.config.settings import settings


def get_engine(url = settings.database_url) -> AsyncEngine:
    return create_async_engine(url, echo=True)

def get_session(engine=get_engine(), class_=AsyncSession) -> sessionmaker:
    return sessionmaker(engine, expire_on_commit=False, class_=class_)

AsyncSessionLocal = get_session()

async def get_db():
    session = AsyncSessionLocal()  # create session
    try:
        return session
    except Exception:
        await session.rollback()
        raise