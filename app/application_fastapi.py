from fastapi import FastAPI, HTTPException, Request, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

# Set up paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
os.makedirs(INSTANCE_DIR, exist_ok=True)
DB_PATH = os.path.join(INSTANCE_DIR, "drinks.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) #The connect_args={"check_same_thread": False} is needed only for SQLite, to allow multiple threads to use the same connection.
SessionLocal = sessionmaker(bind=engine) #creating new database sessions.
Base = declarative_base()

# FastAPI instance
app = FastAPI()

# Pydantic schema
class DrinkCreate(BaseModel):
    name: str
    description: str

class DrinkRead(BaseModel):
    id: int
    name: str
    description: str

#"I want to create this model from a regular Python object — like a SQLAlchemy model — not just a dictionary."
    class Config:
        from_attributes = True

# SQLAlchemy model
class Drink(Base):
    __tablename__ = "drink"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), unique=True, nullable=False)
    description = Column(String(120))

# Create the table
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root route
@app.get("/")
def index():
    return {"message": "Hello!"}

# Get all drinks
@app.get("/drinks")
def get_drinks(db: Session = Depends(get_db)):
    drinks = db.query(Drink).all()
    return {"drinks": [DrinkRead.model_validate(drink) for drink in drinks]}

# Get single drink
@app.get("/drinks/{drink_id}")
def get_drink(drink_id: int, db: Session = Depends(get_db)):
    drink = db.query(Drink).get(drink_id)
    if not drink:
        raise HTTPException(status_code=404, detail="Drink not found")
    return DrinkRead.model_validate(drink)

# Create new drink
@app.post("/drinks")
def create_drink(drink: DrinkCreate, db: Session = Depends(get_db)):
    db_drink = Drink(name=drink.name, description=drink.description)
    db.add(db_drink)
    db.commit()
    db.refresh(db_drink)
    return {"id": db_drink.id}

# Delete drink
@app.delete("/drinks/{drink_id}")
def delete_drink(drink_id: int, db: Session = Depends(get_db)):
    drink = db.query(Drink).get(drink_id)
    if not drink:
        raise HTTPException(status_code=404, detail="Drink not found")
    db.delete(drink)
    db.commit()
    return {"message": f"Drink {drink_id} deleted"}
