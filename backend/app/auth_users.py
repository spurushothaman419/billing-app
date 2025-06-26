# app/auth_users.py
from fastapi_users import FastAPIUsers
from fastapi_users.db import SQLAlchemyUserDatabase
from app.models import User
from app.user_db import get_user_db
from app.user_manager import get_user_manager
from app.auth import auth_backend

fastapi_users = FastAPIUsers[User, str](
    get_user_manager,
    [auth_backend],
)
