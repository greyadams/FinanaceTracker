import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/FT_test" # Используйте тестовую БД

@pytest.fixture
async def db_session():
    engine = create_async_engine(DATABASE_URL, echo=True)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        yield session

@pytest.mark.asyncio
async def test_database_connection(db_session):
    assert db_session is not None  # Простая проверка, что сессия создана
