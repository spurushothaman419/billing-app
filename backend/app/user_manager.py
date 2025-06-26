# app/user_manager.py
from fastapi_users import BaseUserManager, UUIDIDMixin
from app.models import User
from app.database import get_user_db
from app.config import SECRET  # Use same secret as in auth.py

class UserManager(UUIDIDMixin, BaseUserManager[User, str]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request=None):
        print(f"User {user.id} has registered.")

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
