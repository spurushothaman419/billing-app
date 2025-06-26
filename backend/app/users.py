from fastapi_users import FastAPIUsers
from fastapi_users.db import SQLAlchemyUserDatabase
from app.models import User
from app.database import get_user_db
from app.jwt_authentication import jwt_auth_backend

fastapi_users = FastAPIUsers[User, int](
    get_user_db,
    [jwt_auth_backend],
)
