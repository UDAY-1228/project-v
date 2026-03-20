from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from core.backend.database.connection import db
from core.backend.auth.security import get_current_user

# Import apps from workspaces
from super_admin.backend.api.routes import router as super_admin_router
from admin.backend.api.routes import router as admin_router

import importlib

app = FastAPI(title="CAMPUX Campus Management System Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_db_client():
    await db.connect_to_mongodb()

@app.on_event("shutdown")
async def shutdown_db_client():
    await db.close_mongodb_connection()

@app.get("/health")
async def health():
    return {"status": "ok", "service": "campux-gateway"}

# Mount main modules
app.include_router(super_admin_router, prefix="/api/super-admin", tags=["Super Admin"])
app.include_router(admin_router, prefix="/api/admin", tags=["Admin"])

# Mount Workspaces
workspaces = [
    "principal", "academic-coordinator", "admission-officer", "admissions-counselor",
    "common", "team-owner", "transport-coordinator", "employee", "hostel-admin",
    "payment-administrator", "examination", "faculty", "student"
]

for ws in workspaces:
    try:
        # Load workspace routes dynamically
        module_path = f"workspaces.{ws.replace('-', '_')}.backend.api.routes"
        ws_module = importlib.import_module(module_path)
        app.include_router(ws_module.router, prefix=f"/api/{ws}", tags=[ws.replace('-', ' ').capitalize()])
    except ImportError as e:
        print(f"Could not import workspace {ws}: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
