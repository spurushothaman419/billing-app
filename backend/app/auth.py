from fastapi_users import FastAPIUsers, models, schemas
from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from app.models import User  # this must extend BaseUserDB + SQLAlchemy base
from app.database import get_db

SECRET = "CHANGE_THIS_SECRET_TO_SOMETHING_SECURE"

# Define Pydantic schemas
class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass

class UserDB(schemas.BaseUserDB):
    pass

# Proper dependency function for FastAPI
async def get_user_db(session: AsyncSession = Depends(get_db)):
    yield SQLAlchemyUserDatabase(UserDB, session, User)

# JWT Auth Setup
jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

# Create FastAPI Users instance
fastapi_users = FastAPIUsers[User, int](
    get_user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)
