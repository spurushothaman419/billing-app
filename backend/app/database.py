from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi import Depends

from app.models import User

# ✅ Async SQLite URL (FastAPI Users v12 needs async support)
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# ✅ Async Engine and Session
engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# ✅ Base model
Base = declarative_base()

# ✅ Provide async user database session for FastAPI Users
async def get_user_db(session: AsyncSession = Depends(async_session_maker)):
    yield SQLAlchemyUserDatabase(session, User)
