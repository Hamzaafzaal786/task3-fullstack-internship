from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.database import get_db
from app.models.item import Base
from app.routers import item

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI CRUD Application",
    description="A simple CRUD API built with FastAPI",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(item.router)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI CRUD Application"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}