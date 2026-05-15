"""
VID Auth Service – FastAPI Microservice
Handles: Login, Logout, Token Refresh, User Registration, Password Management
"""
import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
from routers import auth_router
from database import create_tables

load_dotenv()

app = FastAPI(
    title="VID Auth Service",
    description="Authentication & Authorization microservice for VID ERP",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ── CORS ──────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.environ.get("CORS_ORIGINS", "http://localhost:5000").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Startup ───────────────────────────────────────────────────────────────────
@app.on_event("startup")
async def startup():
    await create_tables()


# ── Health ────────────────────────────────────────────────────────────────────
@app.get("/health")
async def health():
    return {"status": "ok", "service": "auth-service"}


# ── Routes ────────────────────────────────────────────────────────────────────
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])


if __name__ == "__main__":
    port = int(os.environ.get("AUTH_SERVICE_PORT", 8001))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
