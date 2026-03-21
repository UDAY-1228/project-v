from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, Any, List, Optional
from pydantic import BaseModel
from core.backend.services.timetable_service import (
    generate_timetable, save_timetable, get_timetable,
    get_all_timetables, update_timetable, mark_absent,
    get_substitute_suggestions, assign_substitute,
    get_affected_periods, get_all_classes, get_faculty_list, get_courses
)

router = APIRouter(tags=["Timetable"])


# ── Schemas ──────────────────────────────
class GenerateRequest(BaseModel):
    classId: str
    workingDays: List[str]
    periodsPerDay: int
    breakTime: str = "12:00-1:00"

class UpdateRequest(BaseModel):
    schedule: List[Dict[str, Any]]

class AbsenceRequest(BaseModel):
    facultyId: str
    date: str

class SubstituteRequest(BaseModel):
    classId: str
    day: str
    timeSlot: str
    substituteFacultyId: str


# ── Endpoints ─────────────────────────────

@router.get("/timetable/classes")
async def list_classes():
    return {"classes": get_all_classes()}


@router.get("/timetable/faculty")
async def list_faculty():
    return {"faculty": get_faculty_list()}


@router.get("/timetable/courses/{class_id}")
async def get_course(class_id: str):
    course = get_courses(class_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.post("/timetable/generate")
async def api_generate_timetable(req: GenerateRequest):
    try:
        tt = generate_timetable(req.classId, req.workingDays, req.periodsPerDay, req.breakTime)
        save_timetable(tt)
        return {"success": True, "timetable": tt}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/timetable/{class_id}")
async def api_get_timetable(class_id: str):
    tt = get_timetable(class_id)
    if not tt:
        raise HTTPException(status_code=404, detail="Timetable not found")
    return tt


@router.get("/timetable")
async def api_get_all_timetables():
    return {"timetables": get_all_timetables()}


@router.put("/timetable/{class_id}")
async def api_update_timetable(class_id: str, req: UpdateRequest):
    ok = update_timetable(class_id, req.schedule)
    if not ok:
        raise HTTPException(status_code=404, detail="Timetable not found")
    return {"success": True}


@router.post("/timetable/absence/mark")
async def api_mark_absent(req: AbsenceRequest):
    rec = mark_absent(req.facultyId, req.date)
    affected = get_affected_periods(req.facultyId, req.date)
    return {"absence": rec, "affectedPeriods": affected}


@router.get("/timetable/absence/all")
async def api_get_absences():
    from core.backend.services.timetable_service import get_absences
    return {"absences": get_absences()}


@router.get("/timetable/substitute/{faculty_id}/{subject}")
async def api_get_substitutes(faculty_id: str, subject: str):
    subs = get_substitute_suggestions(faculty_id, subject)
    return {"suggestions": subs}


@router.post("/timetable/substitute/assign")
async def api_assign_substitute(req: SubstituteRequest):
    ok = assign_substitute(req.classId, req.day, req.timeSlot, req.substituteFacultyId)
    if not ok:
        raise HTTPException(status_code=404, detail="Period not found")
    return {"success": True}
