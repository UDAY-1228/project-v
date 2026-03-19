from .auth import router as auth_router
from .users import router as users_router
from .institutions import router as institutions_router
from .attendance import router as attendance_router
from .timetable import router as timetable_router
from .fees import router as fees_router
from .lms import router as lms_router
from .exams import router as exams_router
from .analytics import router as analytics_router
from .communication import router as communication_router
from .virtual_id import router as virtual_id_router
from .notifications import router as notifications_router
from .admin import router as admin_router
from .ed_officials import router as ed_officials_router

__all__ = [
    "auth_router", "users_router", "institutions_router",
    "attendance_router", "timetable_router", "fees_router",
    "lms_router", "exams_router", "analytics_router",
    "communication_router", "virtual_id_router", "notifications_router",
    "admin_router", "ed_officials_router",
]
