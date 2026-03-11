from fastapi import APIRouter
from app.api.v1.endpoints import (
    auth, attendance, system, profiles, 
    timetable, fees, lms, exams, 
    analytics, notifications, messaging, 
    chatbot, audit, institution
)

api_router = APIRouter()

# Register all system endpoints
api_router.include_router(system.router, prefix="/system", tags=["System"])
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(profiles.router, prefix="/profiles", tags=["Profiles"])
api_router.include_router(attendance.router, prefix="/attendance", tags=["Attendance"])
api_router.include_router(timetable.router, prefix="/timetable", tags=["Timetable"])
api_router.include_router(fees.router, prefix="/fees", tags=["Finance"])
api_router.include_router(lms.router, prefix="/lms", tags=["LMS"])
api_router.include_router(exams.router, prefix="/exams", tags=["Exams"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
api_router.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])
api_router.include_router(messaging.router, prefix="/messaging", tags=["Messaging"])
api_router.include_router(chatbot.router, prefix="/chatbot", tags=["AI Chatbot"])
api_router.include_router(audit.router, prefix="/audit", tags=["Audit"])
api_router.include_router(institution.router, prefix="/institution", tags=["Institution Administration"])
