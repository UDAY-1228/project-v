"""
EIMS — App Backend (Student & Parent)
"""
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.staticfiles import StaticFiles
from loguru import logger

from ..shared.config import settings
from ..shared.database import connect_db, disconnect_db
from .api import (
    auth_router,
    users_router,
    attendance_router,
    timetable_router,
    fees_router,
    lms_router,
    exams_router,
    communication_router,
    virtual_id_router,
    notifications_router,
)
from .api.websocket import ws_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
    await disconnect_db()

app = FastAPI(
    title="EIMS App API (Student/Parent)",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

PREFIX = "/api/v1"
app.include_router(auth_router,          prefix=f"{PREFIX}/auth",           tags=["Auth"])
app.include_router(users_router,         prefix=f"{PREFIX}/users",          tags=["Users"])
app.include_router(attendance_router,    prefix=f"{PREFIX}/attendance",     tags=["Attendance"])
app.include_router(timetable_router,     prefix=f"{PREFIX}/timetable",      tags=["Timetable"])
app.include_router(fees_router,          prefix=f"{PREFIX}/fees",           tags=["Fees"])
app.include_router(lms_router,           prefix=f"{PREFIX}/lms",            tags=["LMS"])
app.include_router(exams_router,         prefix=f"{PREFIX}/exams",          tags=["Exams"])
app.include_router(communication_router, prefix=f"{PREFIX}/communication",  tags=["Communication"])
app.include_router(virtual_id_router,    prefix=f"{PREFIX}/virtual-id",     tags=["Virtual ID"])
app.include_router(notifications_router, prefix=f"{PREFIX}/notifications",  tags=["Notifications"])
app.include_router(ws_router,            prefix="/ws",                      tags=["WebSockets"])

@app.get("/health")
async def health(): return {"status": "healthy", "service": "app-api"}
