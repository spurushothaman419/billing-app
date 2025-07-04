from fastapi_users.authentication import AuthenticationBackend
from fastapi_users.authentication.strategy.jwt import JWTStrategy
from fastapi_users.authentication.transport.bearer import BearerTransport

SECRET = "SUPER_SECRET_KEY_CHANGE_ME"  # ✅ Set securely via env var in production

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

jwt_auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
