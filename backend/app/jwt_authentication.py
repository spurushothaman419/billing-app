from fastapi_users.authentication import AuthenticationBackend
from fastapi_users.authentication.strategy.jwt import JWTStrategy
from fastapi_users.authentication.transport.bearer import BearerTransport

SECRET = "SUPERSECRET"  # 🔐 Use os.environ in production

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
