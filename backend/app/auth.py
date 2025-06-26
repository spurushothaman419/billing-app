# app/auth.py

from fastapi_users.authentication import AuthenticationBackend
from fastapi_users.authentication.strategy.jwt import JWTStrategy
from fastapi_users.authentication.transport.bearer import BearerTransport

SECRET = "SUPER_SECRET_JWT"  # Replace with a secure secret

# Define the transport method (Bearer token)
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

# Define the JWT strategy
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

# Define the authentication backend
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
