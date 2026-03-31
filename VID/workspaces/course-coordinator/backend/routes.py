"""
Course Coordinator - API Routes
==============================
FastAPI router for all Course Coordinator endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from .models import *
from .services import (
    DashboardService,
    CoursePlanningService,
    SessionService,
    SubjectService,
    FacultyService,
    AllocationService,
    ReportService,
    SettingsService,
)

router = APIRouter(prefix="/course-coordinator", tags=["Course Coordinator"])


@router.get("/dashboard/stats", response_model=APIResponse)
async def get_dashboard_stats():
    try:
        stats = await DashboardService.get_stats()
        return APIResponse(success=True, data=stats, message="Dashboard stats retrieved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/dashboard/activity", response_model=APIResponse)
async def get_dashboard_activity(limit: int = Query(10, ge=1, le=50)):
    try:
        activities = await DashboardService.get_recent_activity(limit)
        return APIResponse(success=True, data=activities, count=len(activities))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/course-plans", response_model=APIResponse)
async def create_course_plan(data: CoursePlanCreate):
    try:
        plan_id = await CoursePlanningService.create_course_plan(data.model_dump())
        return APIResponse(success=True, data={"id": plan_id}, message="Course plan created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/course-plans", response_model=APIResponse)
async def get_course_plans(
    academic_year: Optional[str] = None,
    semester: Optional[str] = None,
    status: Optional[str] = None
):
    try:
        plans = await CoursePlanningService.get_all_course_plans(academic_year, semester, status)
        return APIResponse(success=True, data=plans, count=len(plans))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/course-plans/{plan_id}", response_model=APIResponse)
async def get_course_plan(plan_id: str):
    try:
        plan = await CoursePlanningService.get_course_plan(plan_id)
        if not plan:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=plan)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/course-plans/{plan_id}", response_model=APIResponse)
async def update_course_plan(plan_id: str, data: CoursePlanCreate):
    try:
        updated = await CoursePlanningService.update_course_plan(plan_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/course-plans/{plan_id}", response_model=APIResponse)
async def delete_course_plan(plan_id: str):
    try:
        deleted = await CoursePlanningService.delete_course_plan(plan_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/sessions", response_model=APIResponse)
async def create_session(data: SessionCreate):
    try:
        session_id = await SessionService.create_session(data.model_dump())
        return APIResponse(success=True, data={"id": session_id}, message="Session created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/sessions", response_model=APIResponse)
async def get_sessions(
    plan_id: Optional[str] = None,
    faculty_id: Optional[str] = None,
    status: Optional[str] = None
):
    try:
        sessions = await SessionService.get_all_sessions(plan_id, faculty_id, status)
        return APIResponse(success=True, data=sessions, count=len(sessions))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/sessions/{session_id}", response_model=APIResponse)
async def get_session(session_id: str):
    try:
        session = await SessionService.get_session(session_id)
        if not session:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=session)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/sessions/{session_id}", response_model=APIResponse)
async def update_session(session_id: str, data: SessionCreate):
    try:
        updated = await SessionService.update_session(session_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/sessions/{session_id}", response_model=APIResponse)
async def delete_session(session_id: str):
    try:
        deleted = await SessionService.delete_session(session_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/subjects", response_model=APIResponse)
async def create_subject(data: SubjectCreate):
    try:
        subject_id = await SubjectService.create_subject(data.model_dump())
        return APIResponse(success=True, data={"id": subject_id}, message="Subject created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/subjects", response_model=APIResponse)
async def get_subjects(
    course_id: Optional[str] = None,
    semester: Optional[str] = None,
    status: Optional[str] = None
):
    try:
        subjects = await SubjectService.get_all_subjects(course_id, semester, status)
        return APIResponse(success=True, data=subjects, count=len(subjects))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/subjects/{subject_id}", response_model=APIResponse)
async def get_subject(subject_id: str):
    try:
        subject = await SubjectService.get_subject(subject_id)
        if not subject:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=subject)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/subjects/{subject_id}", response_model=APIResponse)
async def update_subject(subject_id: str, data: SubjectCreate):
    try:
        updated = await SubjectService.update_subject(subject_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/subjects/{subject_id}", response_model=APIResponse)
async def delete_subject(subject_id: str):
    try:
        deleted = await SubjectService.delete_subject(subject_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/faculty", response_model=APIResponse)
async def create_faculty(data: FacultyCreate):
    try:
        faculty_id = await FacultyService.create_faculty(data.model_dump())
        return APIResponse(success=True, data={"id": faculty_id}, message="Faculty created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/faculty", response_model=APIResponse)
async def get_faculty(department: Optional[str] = None, status: Optional[str] = None):
    try:
        faculty = await FacultyService.get_all_faculty(department, status)
        return APIResponse(success=True, data=faculty, count=len(faculty))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/faculty/{faculty_id}", response_model=APIResponse)
async def get_faculty_by_id(faculty_id: str):
    try:
        faculty = await FacultyService.get_faculty(faculty_id)
        if not faculty:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=faculty)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/faculty/{faculty_id}", response_model=APIResponse)
async def update_faculty(faculty_id: str, data: FacultyCreate):
    try:
        updated = await FacultyService.update_faculty(faculty_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/faculty/{faculty_id}", response_model=APIResponse)
async def delete_faculty(faculty_id: str):
    try:
        deleted = await FacultyService.delete_faculty(faculty_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/allocations", response_model=APIResponse)
async def create_allocation(data: AllocationCreate):
    try:
        allocation_id = await AllocationService.create_allocation(data.model_dump())
        return APIResponse(success=True, data={"id": allocation_id}, message="Allocation created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/allocations", response_model=APIResponse)
async def get_allocations(
    faculty_id: Optional[str] = None,
    subject_id: Optional[str] = None,
    academic_year: Optional[str] = None
):
    try:
        allocations = await AllocationService.get_all_allocations(faculty_id, subject_id, academic_year)
        return APIResponse(success=True, data=allocations, count=len(allocations))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/allocations/{allocation_id}", response_model=APIResponse)
async def get_allocation(allocation_id: str):
    try:
        allocation = await AllocationService.get_allocation(allocation_id)
        if not allocation:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=allocation)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/allocations/{allocation_id}", response_model=APIResponse)
async def update_allocation(allocation_id: str, data: AllocationCreate):
    try:
        updated = await AllocationService.update_allocation(allocation_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/allocations/{allocation_id}", response_model=APIResponse)
async def delete_allocation(allocation_id: str):
    try:
        deleted = await AllocationService.delete_allocation(allocation_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/reports", response_model=APIResponse)
async def create_report(data: CoordinatorReportCreate):
    try:
        report_id = await ReportService.create_report(data.model_dump())
        return APIResponse(success=True, data={"id": report_id}, message="Report created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/reports", response_model=APIResponse)
async def get_reports(report_type: Optional[str] = None, academic_year: Optional[str] = None):
    try:
        reports = await ReportService.get_all_reports(report_type, academic_year)
        return APIResponse(success=True, data=reports, count=len(reports))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/reports/{report_id}", response_model=APIResponse)
async def get_report(report_id: str):
    try:
        report = await ReportService.get_report(report_id)
        if not report:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=report)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/reports/{report_id}", response_model=APIResponse)
async def delete_report(report_id: str):
    try:
        deleted = await ReportService.delete_report(report_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/settings", response_model=APIResponse)
async def get_settings(institution_id: Optional[str] = None):
    try:
        settings = await SettingsService.get_settings(institution_id)
        return APIResponse(success=True, data=settings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/settings", response_model=APIResponse)
async def update_settings(data: CoordinatorSettingsCreate, institution_id: Optional[str] = None):
    try:
        settings_id = await SettingsService.upsert_settings(data.model_dump(), institution_id)
        return APIResponse(success=True, data={"id": settings_id}, message="Settings saved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
