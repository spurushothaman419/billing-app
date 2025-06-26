# app/auth.py

from fastapi_users.authentication import AuthenticationBackend
from fastapi_users.authentication.strategy.jwt import JWTStrategy
from fastapi_users.authentication.transport.bearer import BearerTransport

SECRET = "SUPER_SECRET_JWT"  # Change this securely

# Define Bearer token transport
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

# Define JWT strategy
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

# Compose authentication backend
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
