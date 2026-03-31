"""
Faculty - API Routes
=====================
FastAPI router for all Faculty endpoints.
Covers: Dashboard, Classes, Attendance, Assignments, Exams, Reports, Profile, Settings
"""

from fastapi import APIRouter, HTTPException, Query, Body
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel
from typing import Any

router = APIRouter(prefix="/faculty", tags=["Faculty"])


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


from .services import (
    DashboardService,
    ProfileService,
    ClassesService,
    AttendanceService,
    AssignmentsService,
    ExamsService,
    ReportsService,
    SettingsService,
)


@router.get("/dashboard/stats", response_model=APIResponse)
async def get_dashboard_stats(faculty_id: Optional[str] = None):
    """Get aggregate statistics for the Faculty dashboard."""
    try:
        stats = await DashboardService.get_stats(faculty_id)
        return APIResponse(success=True, data=stats, message="Dashboard stats retrieved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/dashboard/activity", response_model=APIResponse)
async def get_dashboard_activity(faculty_id: Optional[str] = None, limit: int = Query(10, ge=1, le=50)):
    """Get recent activity log entries."""
    try:
        activities = await DashboardService.get_recent_activity(faculty_id, limit)
        return APIResponse(success=True, data=activities, count=len(activities))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/profile", response_model=APIResponse)
async def create_profile(data: dict):
    """Create a new faculty profile."""
    try:
        profile_id = await ProfileService.create_profile(data)
        return APIResponse(success=True, data={"id": profile_id}, message="Profile created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/profile/{faculty_id}", response_model=APIResponse)
async def get_profile(faculty_id: str):
    """Get faculty profile by faculty ID."""
    try:
        profile = await ProfileService.get_profile(faculty_id)
        if not profile:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=profile)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/profile/{faculty_id}", response_model=APIResponse)
async def update_profile(faculty_id: str, data: dict):
    """Update faculty profile."""
    try:
        updated = await ProfileService.update_profile(faculty_id, data)
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/classes", response_model=APIResponse)
async def create_class(data: dict):
    """Create a new class."""
    try:
        class_id = await ClassesService.create_class(data)
        return APIResponse(success=True, data={"id": class_id}, message="Class created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/classes", response_model=APIResponse)
async def get_classes(faculty_id: Optional[str] = None, semester_id: Optional[str] = None):
    """List all classes for a faculty."""
    try:
        classes = await ClassesService.get_all_classes(faculty_id, semester_id)
        return APIResponse(success=True, data=classes, count=len(classes))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/classes/{class_id}", response_model=APIResponse)
async def get_class(class_id: str):
    """Get a specific class by ID."""
    try:
        class_data = await ClassesService.get_class(class_id)
        if not class_data:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=class_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/classes/{class_id}", response_model=APIResponse)
async def update_class(class_id: str, data: dict):
    """Update an existing class."""
    try:
        updated = await ClassesService.update_class(class_id, data)
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/classes/{class_id}", response_model=APIResponse)
async def delete_class(class_id: str):
    """Delete a class."""
    try:
        deleted = await ClassesService.delete_class(class_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/classes/{class_id}/students", response_model=APIResponse)
async def get_class_students(class_id: str):
    """Get all students enrolled in a class."""
    try:
        students = await ClassesService.get_class_students(class_id)
        return APIResponse(success=True, data=students, count=len(students))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/attendance", response_model=APIResponse)
async def mark_attendance(data: dict, faculty_id: Optional[str] = None):
    """Mark attendance for a class."""
    try:
        records = data.get("records", [])
        class_id = await AttendanceService.mark_attendance(data["class_id"], data["date"], records, faculty_id)
        return APIResponse(success=True, data={"class_id": class_id}, message="Attendance marked")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/attendance/{class_id}", response_model=APIResponse)
async def get_attendance_records(class_id: str, date: Optional[datetime] = None):
    """Get attendance records for a class."""
    try:
        records = await AttendanceService.get_attendance_records(class_id, date)
        return APIResponse(success=True, data=records, count=len(records))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/attendance/{class_id}/summary", response_model=APIResponse)
async def get_attendance_summary(class_id: str):
    """Get attendance summary for all students in a class."""
    try:
        summary = await AttendanceService.get_attendance_summary(class_id)
        return APIResponse(success=True, data=summary, count=len(summary))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/attendance/{class_id}/report", response_model=APIResponse)
async def get_attendance_report(
    class_id: str,
    start_date: datetime = Query(...),
    end_date: datetime = Query(...)
):
    """Generate an attendance report for a date range."""
    try:
        report = await AttendanceService.get_attendance_report(class_id, start_date, end_date)
        return APIResponse(success=True, data=report, message="Report generated")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/attendance/{record_id}", response_model=APIResponse)
async def update_attendance_record(record_id: str, data: dict):
    """Update an attendance record."""
    try:
        updated = await AttendanceService.update_attendance_record(record_id, data)
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/assignments", response_model=APIResponse)
async def create_assignment(data: dict):
    """Create a new assignment."""
    try:
        assignment_id = await AssignmentsService.create_assignment(data)
        return APIResponse(success=True, data={"id": assignment_id}, message="Assignment created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/assignments", response_model=APIResponse)
async def get_assignments(faculty_id: Optional[str] = None, class_id: Optional[str] = None):
    """List all assignments for a faculty."""
    try:
        assignments = await AssignmentsService.get_all_assignments(faculty_id, class_id)
        return APIResponse(success=True, data=assignments, count=len(assignments))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/assignments/{assignment_id}", response_model=APIResponse)
async def get_assignment(assignment_id: str):
    """Get a specific assignment by ID."""
    try:
        assignment = await AssignmentsService.get_assignment(assignment_id)
        if not assignment:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=assignment)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/assignments/{assignment_id}", response_model=APIResponse)
async def update_assignment(assignment_id: str, data: dict):
    """Update an existing assignment."""
    try:
        updated = await AssignmentsService.update_assignment(assignment_id, data)
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/assignments/{assignment_id}", response_model=APIResponse)
async def delete_assignment(assignment_id: str):
    """Delete an assignment."""
    try:
        deleted = await AssignmentsService.delete_assignment(assignment_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/assignments/{assignment_id}/submissions", response_model=APIResponse)
async def get_submissions(assignment_id: str):
    """Get all submissions for an assignment."""
    try:
        submissions = await AssignmentsService.get_submissions(assignment_id)
        return APIResponse(success=True, data=submissions, count=len(submissions))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/assignments/{assignment_id}/evaluate", response_model=APIResponse)
async def evaluate_submission(assignment_id: str, data: dict):
    """Submit evaluation for an assignment."""
    try:
        eval_id = await AssignmentsService.submit_evaluation(assignment_id, data)
        return APIResponse(success=True, data={"id": eval_id}, message="Evaluation submitted")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/exams", response_model=APIResponse)
async def create_exam(data: dict):
    """Create a new exam."""
    try:
        exam_id = await ExamsService.create_exam(data)
        return APIResponse(success=True, data={"id": exam_id}, message="Exam created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/exams", response_model=APIResponse)
async def get_exams(faculty_id: Optional[str] = None, class_id: Optional[str] = None):
    """List all exams for a faculty."""
    try:
        exams = await ExamsService.get_all_exams(faculty_id, class_id)
        return APIResponse(success=True, data=exams, count=len(exams))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/exams/{exam_id}", response_model=APIResponse)
async def get_exam(exam_id: str):
    """Get a specific exam by ID."""
    try:
        exam = await ExamsService.get_exam(exam_id)
        if not exam:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=exam)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/exams/{exam_id}", response_model=APIResponse)
async def update_exam(exam_id: str, data: dict):
    """Update an existing exam."""
    try:
        updated = await ExamsService.update_exam(exam_id, data)
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/exams/{exam_id}", response_model=APIResponse)
async def delete_exam(exam_id: str):
    """Delete an exam."""
    try:
        deleted = await ExamsService.delete_exam(exam_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/exams/{exam_id}/results", response_model=APIResponse)
async def submit_results(exam_id: str, results: List[dict]):
    """Submit exam results."""
    try:
        success = await ExamsService.submit_results(exam_id, results)
        return APIResponse(success=success, message="Results submitted")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/exams/{exam_id}/results", response_model=APIResponse)
async def get_results(exam_id: str):
    """Get all results for an exam."""
    try:
        results = await ExamsService.get_results(exam_id)
        return APIResponse(success=True, data=results, count=len(results))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/exams/{exam_id}/results/{student_id}", response_model=APIResponse)
async def get_result(exam_id: str, student_id: str):
    """Get a specific student result for an exam."""
    try:
        result = await ExamsService.get_result(exam_id, student_id)
        if not result:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/reports", response_model=APIResponse)
async def create_report(data: dict):
    """Create a new report."""
    try:
        report_id = await ReportsService.create_report(data)
        return APIResponse(success=True, data={"id": report_id}, message="Report created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/reports", response_model=APIResponse)
async def get_reports(faculty_id: Optional[str] = None, report_type: Optional[str] = None):
    """List all reports."""
    try:
        reports = await ReportsService.get_all_reports(faculty_id, report_type)
        return APIResponse(success=True, data=reports, count=len(reports))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/reports/{report_id}", response_model=APIResponse)
async def get_report(report_id: str):
    """Get a specific report by ID."""
    try:
        report = await ReportsService.get_report(report_id)
        if not report:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=report)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/reports/{report_id}", response_model=APIResponse)
async def delete_report(report_id: str):
    """Delete a report."""
    try:
        deleted = await ReportsService.delete_report(report_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/reports/performance", response_model=APIResponse)
async def generate_performance_report(faculty_id: str, class_id: str):
    """Generate a performance report for a class."""
    try:
        report = await ReportsService.generate_performance_report(faculty_id, class_id)
        return APIResponse(success=True, data=report, message="Report generated")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/settings", response_model=APIResponse)
async def get_settings(faculty_id: Optional[str] = None):
    """Get faculty settings."""
    try:
        settings = await SettingsService.get_settings(faculty_id)
        return APIResponse(success=True, data=settings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/settings", response_model=APIResponse)
async def update_settings(data: dict, faculty_id: Optional[str] = None):
    """Update faculty settings."""
    try:
        settings_id = await SettingsService.upsert_settings(data, faculty_id)
        return APIResponse(success=True, data={"id": settings_id}, message="Settings saved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
