from fastapi_users import FastAPIUsers
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.manager import BaseUserManager, UUIDIDMixin
from fastapi_users.models import BaseUserDB, BaseUser
from fastapi_users.password import PasswordHelper

from app.models import User, get_user_db
from app.auth.jwt_authentication import jwt_auth_backend

class UserManager(UUIDIDMixin, BaseUserManager[User, str]):
    reset_password_token_secret = "SECRET"
    verification_token_secret = "SECRET"

    async def on_after_register(self, user: User, request=None):
        print(f"User {user.id} registered.")

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)

fastapi_users = FastAPIUsers[User, str](
    get_user_manager,
    [jwt_auth_backend],
)
