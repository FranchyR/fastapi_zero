from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from fastapi_zero.settings import Settings

engine = create_async_engine(Settings().DATABASE_URL)


async def get_session():
    async with AsyncSession(engine, expire_on_comit=False) as session:
        yield session
