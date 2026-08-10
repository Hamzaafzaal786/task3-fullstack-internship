from fastapi import FastAPI

app = FastAPI(
    title="FastAPI CRUD Application",
    description="A simple CRUD API built with FastAPI",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI CRUD Application"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}