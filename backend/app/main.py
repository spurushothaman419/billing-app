# app/main.py

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession

import uuid
import asyncio

from app.auth import auth_backend
from app.auth_users import fastapi_users
from app.database import engine, Base, async_session_maker
from app.models import Customer
from app.schemas import CustomerCreate, Customer as CustomerOut

# Async DB init
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(init_db())

app = FastAPI(title="Embroidery Billing API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Auth routes
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(),
    prefix="/auth",
    tags=["auth"]
)
app.include_router(
    fastapi_users.get_users_router(),
    prefix="/users",
    tags=["users"]
)

# ✅ Customer endpoints
@app.post("/customers/", response_model=CustomerOut)
async def create_customer(customer: CustomerCreate, session: AsyncSession = Depends(async_session_maker)):
    result = await session.execute(
        Customer.__table__.select().where(Customer.email == customer.email)
    )
    existing = result.fetchone()
    if existing:
        raise HTTPException(status_code=400, detail="Customer already exists")

    new_customer = Customer(
        id=str(uuid.uuid4()),
        name=customer.name,
        email=customer.email,
        phone=customer.phone
    )
    session.add(new_customer)
    await session.commit()
    await session.refresh(new_customer)
    return new_customer

@app.get("/customers/", response_model=list[CustomerOut])
async def list_customers(session: AsyncSession = Depends(async_session_maker)):
    result = await session.execute(Customer.__table__.select())
    return result.scalars().all()

@app.get("/")
def root():
    return {"message": "Embroidery Billing API running"}
