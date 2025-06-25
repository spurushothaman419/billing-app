from fastapi_users import FastAPIUsers, models, schemas
from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.orm import Session
from .models import User
from .database import get_db

SECRET = "CHANGE_THIS_SECRET_TO_SOMETHING_SECURE"

class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass

class UserDB(User, schemas.BaseUserDB):
    pass

def get_user_db(session: Session = next(get_db())):
    yield SQLAlchemyUserDatabase(UserDB, session, User)

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

fastapi_users = FastAPIUsers(
    get_user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)
