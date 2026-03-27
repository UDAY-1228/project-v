from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from contextlib import asynccontextmanager
from .core.database.mongo_connection import db
from .super_admin.routes import router as super_admin_router
from .admin.routes import router as admin_router
from .auth.routes import router as auth_router

@asynccontextmanager
async def lifespan(server: FastAPI):
    await db.connect_to_mongo()
    yield
    await db.close_mongo_connection()

server = FastAPI(title="VID Backend API", version="1.0.0", lifespan=lifespan)

# Setup CORS
server.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@server.get("/")
async def root():
    return {"message": "VID Central Core API is running"}

# Register routes
server.include_router(auth_router, prefix="/api/auth", tags=["Authentication"])
server.include_router(super_admin_router, prefix="/api/super-admin", tags=["Super Admin"])
server.include_router(admin_router, prefix="/api/admin", tags=["Admin"])

if __name__ == "__main__":
    uvicorn.run(server, host="0.0.0.0", port=8000)
