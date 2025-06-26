from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.jwt_authentication import auth_backend
from app.auth.jwt_authentication import jwt_auth_backend
from app.auth.fastapi_users import fastapi_users
from app.users import fastapi_users
from app.database import engine, get_db
from app.models import Base, Customer
from app.schemas import CustomerCreate, Customer, UserCreate, UserRead

# Create all DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Embroidery Billing API")

# CORS configuration for frontend (e.g. React at localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register authentication routes
#app.include_router(
   # fastapi_users.get_auth_router(jwt_authentication),
   # prefix="/auth/jwt",
    #tags=["auth"]
app.include_router(
    fastapi_users.get_auth_router(jwt_auth_backend), prefix="/auth/jwt", tags=["auth"]
)
)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)

# Customer CRUD APIs
@app.post("/customers/", response_model=Customer)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    existing_customer = db.query(Customer).filter(Customer.email == customer.email).first()
    if existing_customer:
        raise HTTPException(status_code=400, detail="Customer with this email already exists")
    new_customer = Customer(
        name=customer.name,
        email=customer.email,
        phone=customer.phone
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

@app.get("/customers/", response_model=list[Customer])
def list_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()

@app.get("/")
def root():
    return {"message": "Embroidery Billing API running"}
