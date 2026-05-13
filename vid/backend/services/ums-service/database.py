"""
VID Auth Service – Database Connection (asyncpg / SQLAlchemy async)
"""
import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql+asyncpg://vid_user:vid_password@localhost:5432/vid_db",
)

# Remove sslmode from URL for asyncpg and use connect_args instead
CLEAN_URL = DATABASE_URL.replace("?sslmode=require", "").replace("&sslmode=require", "")
engine = create_async_engine(
    CLEAN_URL, 
    echo=False, 
    pool_pre_ping=True,
    connect_args={"ssl": True}
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


async def create_tables():
    """Create all tables defined on Base metadata."""
    # We must import models here so they are registered with Base.metadata
    import models
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_db() -> AsyncSession:
    """FastAPI dependency that yields an async database session."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
