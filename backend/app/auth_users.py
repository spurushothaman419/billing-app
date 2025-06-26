# app/auth_users.py

from typing import Optional, Union
from fastapi_users import FastAPIUsers, BaseUserManager, IntegerIDMixin
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.models import BaseUserDB
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_users.schemas import BaseUserCreate
from app.database import get_async_session
from app.models import User
from app.auth import auth_backend

SECRET = "SUPER_SECRET_JWT"  # Replace in production

class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    user_db_model = User
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request=None):
        print(f"User {user.id} has registered.")

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
