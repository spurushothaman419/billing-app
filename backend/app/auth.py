from fastapi_users import FastAPIUsers
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.authentication import AuthenticationBackend
from fastapi_users.authentication.strategy.jwt import JWTStrategy
from fastapi_users.authentication.transport.bearer import BearerTransport

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from app.models import User  # must inherit from BaseUserDB
from app.database import get_async_session
from app.schemas import UserCreate, UserRead, UserUpdate

SECRET = "CHANGE_THIS_SECRET_TO_SOMETHING_SECURE"

# 🛡 Bearer transport setup (JWT token in Authorization header)
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

# 🔑 Strategy config
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

# 🧠 Authentication backend using strategy and transport
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

# 🗃 Async User DB dependency
async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session=session, user_db_model=User)

# ⚙️ Create FastAPIUsers instance
fastapi_users = FastAPIUsers[User, int](
    get_user_db,
    [auth_backend],
    User,
    UserCreate,
    UserRead,
    UserUpdate,
)
