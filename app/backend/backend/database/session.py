from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from core import settings
from backend.main import AppState
from backend.models.models import *
from sqlmodel import SQLModel
async_engine = create_async_engine(
   settings.database_uri,
   echo=True,
   future=True,
)

async_session = async_sessionmaker(
    bind= async_engine,
    class_=AsyncSession,
)

async def create_db() -> None:
    async with async_engine.begin() as conn:
        try:
         await conn.run_sync(SQLModel.metadata.create_all)
        except Exception:
            print("There is an error!!")

async def get_async_session(state: AppState) -> AsyncGenerator[AsyncSession, None]:
    async with state["_db"]() as session:
        yield session