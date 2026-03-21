from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from core.backend.database.connection import db
# Using new JSON based auth
from core.backend.auth.login import router as auth_router
from super_admin.backend.api.routes import router as super_admin_router
from admin.backend.api.routes import router as admin_router

import importlib

app = FastAPI(title="VID Campus Management System Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": "ok", "service": "vid-gateway"}

# Mount Auth
app.include_router(auth_router, prefix="/api/auth", tags=["Authentication"])

from core.backend.api.timetable_routes import router as timetable_router
from core.backend.api.notice_routes import router as notice_router

# Mount main modules
app.include_router(super_admin_router, prefix="/api/super-admin", tags=["Super Admin"])
app.include_router(admin_router, prefix="/api/admin", tags=["Admin"])
app.include_router(timetable_router, prefix="/api", tags=["Timetable"])
app.include_router(notice_router, prefix="/api", tags=["Notices"])



# Mount Workspaces
workspaces = [
    "academic_coordinator", "admission_officer",
    "common", "team_owner", "transport_coordinator", "employee", "hostel_admin",
    "payment_administrator", "examination", "faculty", "student", "course_coordinator",
    "sports_officer"
]

for ws in workspaces:
    try:
        module_path = f"workspaces.{ws}.backend.api.routes"
        ws_module = importlib.import_module(module_path)
        app.include_router(ws_module.router, prefix=f"/api/{ws.replace('_', '-')}", tags=[ws.replace('_', ' ').capitalize()])
    except ImportError as e:
        print(f"Could not import workspace {ws}: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
