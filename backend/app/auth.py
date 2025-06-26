from fastapi_users import FastAPIUsers
from fastapi_users.authentication.strategy.jwt import JWTStrategy
from fastapi_users.authentication import AuthenticationBackend
from app.models import User
from app.database import get_user_db
from app.user_manager import get_user_manager

SECRET = "CHANGE_THIS_SECRET"

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=None,  # we'll set this up if needed (like BearerTransport)
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
