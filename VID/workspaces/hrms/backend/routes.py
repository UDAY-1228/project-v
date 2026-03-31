"""
HRMS - Routes
=============
FastAPI application entry point for the HRMS workspace.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from .mongodb_connection import connect_to_database, close_database_connection
from .controllers import router as hrms_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_database()
    yield
    await close_database_connection()


app = FastAPI(
    title="HRMS API",
    description="Human Resources Management System API",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hrms_router)


@app.get("/")
async def root():
    return {"message": "HRMS API", "version": "1.0.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
