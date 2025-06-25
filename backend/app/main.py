# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

DATABASE_URL = "sqlite:///./test.db"
SECRET = "CHANGE_THIS_SECRET_TO_SOMETHING_SECURE"

Base: DeclarativeMeta = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

# Customer model
class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)

Base.metadata.create_all(bind=engine)

# Pydantic schema for Customer
class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi_users import models, schemas
from fastapi_users import FastAPIUsers
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from fastapi_users.authentication import JWTAuthentication

# Define User schemas for FastAPI-Users
class User(models.BaseUser):
    pass

class UserCreate(models.BaseUserCreate):
    pass

class UserUpdate(models.BaseUserUpdate):
    pass

class UserDB(User, models.BaseUserDB):
    pass

user_db = SQLAlchemyUserDatabase(UserDB, SessionLocal(), User)

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

fastapi_users = FastAPIUsers(
    user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

app = FastAPI()

# Allow CORS from frontend (adjust origin as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register user routes (login, register, reset)
app.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(), prefix="/auth", tags=["auth"]
)

# Customer CRUD endpoints
@app.post("/customers/", response_model=CustomerCreate)
def create_customer(customer: CustomerCreate, db: Session = Depends(SessionLocal)):
    db_customer = Customer(name=customer.name, email=customer.email, phone=customer.phone)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.get("/customers/")
def list_customers(db: Session = Depends(SessionLocal)):
    return db.query(Customer).all()
