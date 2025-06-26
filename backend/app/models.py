from sqlalchemy import Column, Integer, String, Boolean
from fastapi_users.db import SQLAlchemyBaseUserTable
from app.database import Base  # ✅ important: use shared Base

# FastAPI Users - User model
class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"  # ✅ explicitly set table name
    # Optionally add more fields:
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
