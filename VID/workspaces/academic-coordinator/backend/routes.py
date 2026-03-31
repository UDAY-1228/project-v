"""
Academic Coordinator - API Routes
==================================
FastAPI router for all Academic Coordinator endpoints.
Covers: Dashboard, Academic Management, Courses, Subjects,
Timetable, Assessments, Reports, Notice Board, Settings
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from .models import *
from .services import (
    DashboardService,
    AcademicManagementService,
    CourseService,
    SubjectService,
    TimetableService,
    AssessmentService,
    ReportService,
    NoticeBoardService,
    SettingsService,
)

router = APIRouter(prefix="/academic-coordinator", tags=["Academic Coordinator"])


# ════════════════════════════════════════════════════════════════════════════════
# DASHBOARD
# ════════════════════════════════════════════════════════════════════════════════

@router.get("/dashboard/stats", response_model=APIResponse)
async def get_dashboard_stats():
    """Get aggregate statistics for the Academic Coordinator dashboard."""
    try:
        stats = await DashboardService.get_stats()
        return APIResponse(success=True, data=stats, message="Dashboard stats retrieved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/dashboard/activity", response_model=APIResponse)
async def get_dashboard_activity(limit: int = Query(10, ge=1, le=50)):
    """Get recent activity log entries."""
    try:
        activities = await DashboardService.get_recent_activity(limit)
        return APIResponse(success=True, data=activities, count=len(activities))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ════════════════════════════════════════════════════════════════════════════════
# ACADEMIC MANAGEMENT — Academic Years
# ════════════════════════════════════════════════════════════════════════════════

@router.post("/academic-years", response_model=APIResponse)
async def create_academic_year(data: AcademicYearCreate):
    """Create a new academic year."""
    try:
        year_id = await AcademicManagementService.create_academic_year(data.model_dump())
        return APIResponse(success=True, data={"id": year_id}, message="Academic year created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/academic-years", response_model=APIResponse)
async def get_academic_years():
    """List all academic years."""
    try:
        years = await AcademicManagementService.get_all_academic_years()
        return APIResponse(success=True, data=years, count=len(years))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/academic-years/{year_id}", response_model=APIResponse)
async def get_academic_year(year_id: str):
    """Get a specific academic year by ID."""
    try:
        year = await AcademicManagementService.get_academic_year(year_id)
        if not year:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=year)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/academic-years/{year_id}", response_model=APIResponse)
async def update_academic_year(year_id: str, data: AcademicYearCreate):
    """Update an existing academic year."""
    try:
        updated = await AcademicManagementService.update_academic_year(year_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/academic-years/{year_id}", response_model=APIResponse)
async def delete_academic_year(year_id: str):
    """Delete an academic year."""
    try:
        deleted = await AcademicManagementService.delete_academic_year(year_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ════════════════════════════════════════════════════════════════════════════════
# ACADEMIC MANAGEMENT — Semesters
# ════════════════════════════════════════════════════════════════════════════════

@router.post("/semesters", response_model=APIResponse)
async def create_semester(data: SemesterCreate):
    try:
        sem_id = await AcademicManagementService.create_semester(data.model_dump())
        return APIResponse(success=True, data={"id": sem_id}, message="Semester created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/semesters", response_model=APIResponse)
async def get_semesters(academic_year_id: Optional[str] = None):
    try:
        semesters = await AcademicManagementService.get_all_semesters(academic_year_id)
        return APIResponse(success=True, data=semesters, count=len(semesters))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/semesters/{semester_id}", response_model=APIResponse)
async def update_semester(semester_id: str, data: SemesterCreate):
    try:
        updated = await AcademicManagementService.update_semester(semester_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/semesters/{semester_id}", response_model=APIResponse)
async def delete_semester(semester_id: str):
    try:
        deleted = await AcademicManagementService.delete_semester(semester_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ════════════════════════════════════════════════════════════════════════════════
# ACADEMIC MANAGEMENT — Departments
# ════════════════════════════════════════════════════════════════════════════════

@router.post("/departments", response_model=APIResponse)
async def create_department(data: DepartmentCreate):
    try:
        dept_id = await AcademicManagementService.create_department(data.model_dump())
        return APIResponse(success=True, data={"id": dept_id}, message="Department created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/departments", response_model=APIResponse)
async def get_departments():
    try:
        depts = await AcademicManagementService.get_all_departments()
        return APIResponse(success=True, data=depts, count=len(depts))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/departments/{dept_id}", response_model=APIResponse)
async def update_department(dept_id: str, data: DepartmentCreate):
    try:
        updated = await AcademicManagementService.update_department(dept_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/departments/{dept_id}", response_model=APIResponse)
async def delete_department(dept_id: str):
    try:
        deleted = await AcademicManagementService.delete_department(dept_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ════════════════════════════════════════════════════════════════════════════════
# COURSES
# ════════════════════════════════════════════════════════════════════════════════

@router.post("/courses", response_model=APIResponse)
async def create_course(data: CourseCreate):
    try:
        course_id = await CourseService.create_course(data.model_dump())
        return APIResponse(success=True, data={"id": course_id}, message="Course created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/courses", response_model=APIResponse)
async def get_courses(department_id: Optional[str] = None):
    try:
        courses = await CourseService.get_all_courses(department_id)
        return APIResponse(success=True, data=courses, count=len(courses))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/courses/{course_id}", response_model=APIResponse)
async def get_course(course_id: str):
    try:
        course = await CourseService.get_course(course_id)
        if not course:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=course)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/courses/{course_id}", response_model=APIResponse)
async def update_course(course_id: str, data: CourseCreate):
    try:
        updated = await CourseService.update_course(course_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/courses/{course_id}", response_model=APIResponse)
async def delete_course(course_id: str):
    try:
        deleted = await CourseService.delete_course(course_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ════════════════════════════════════════════════════════════════════════════════
# SUBJECTS
# ════════════════════════════════════════════════════════════════════════════════

@router.post("/subjects", response_model=APIResponse)
async def create_subject(data: SubjectCreate):
    try:
        subject_id = await SubjectService.create_subject(data.model_dump())
        return APIResponse(success=True, data={"id": subject_id}, message="Subject created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/subjects", response_model=APIResponse)
async def get_subjects(course_id: Optional[str] = None, semester_id: Optional[str] = None):
    try:
        subjects = await SubjectService.get_all_subjects(course_id, semester_id)
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


# ════════════════════════════════════════════════════════════════════════════════
# TIMETABLE
# ════════════════════════════════════════════════════════════════════════════════

@router.post("/timetables", response_model=APIResponse)
async def create_timetable(data: TimetableCreate):
    try:
        tt_id = await TimetableService.create_timetable(data.model_dump())
        return APIResponse(success=True, data={"id": tt_id}, message="Timetable created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/timetables", response_model=APIResponse)
async def get_timetables(course_id: Optional[str] = None, semester_id: Optional[str] = None):
    try:
        timetables = await TimetableService.get_all_timetables(course_id, semester_id)
        return APIResponse(success=True, data=timetables, count=len(timetables))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/timetables/{timetable_id}", response_model=APIResponse)
async def get_timetable(timetable_id: str):
    try:
        tt = await TimetableService.get_timetable(timetable_id)
        if not tt:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=tt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/timetables/{timetable_id}", response_model=APIResponse)
async def update_timetable(timetable_id: str, data: TimetableCreate):
    try:
        updated = await TimetableService.update_timetable(timetable_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/timetables/{timetable_id}", response_model=APIResponse)
async def delete_timetable(timetable_id: str):
    try:
        deleted = await TimetableService.delete_timetable(timetable_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ════════════════════════════════════════════════════════════════════════════════
# ASSESSMENTS
# ════════════════════════════════════════════════════════════════════════════════

@router.post("/assessments", response_model=APIResponse)
async def create_assessment(data: AssessmentCreate):
    try:
        a_id = await AssessmentService.create_assessment(data.model_dump())
        return APIResponse(success=True, data={"id": a_id}, message="Assessment created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/assessments", response_model=APIResponse)
async def get_assessments(subject_id: Optional[str] = None, assessment_type: Optional[str] = None):
    try:
        assessments = await AssessmentService.get_all_assessments(subject_id, assessment_type)
        return APIResponse(success=True, data=assessments, count=len(assessments))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/assessments/{assessment_id}", response_model=APIResponse)
async def get_assessment(assessment_id: str):
    try:
        assessment = await AssessmentService.get_assessment(assessment_id)
        if not assessment:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=assessment)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/assessments/{assessment_id}", response_model=APIResponse)
async def update_assessment(assessment_id: str, data: AssessmentCreate):
    try:
        updated = await AssessmentService.update_assessment(assessment_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/assessments/{assessment_id}", response_model=APIResponse)
async def delete_assessment(assessment_id: str):
    try:
        deleted = await AssessmentService.delete_assessment(assessment_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Assessment Results
@router.post("/assessments/{assessment_id}/results", response_model=APIResponse)
async def submit_assessment_result(assessment_id: str, data: AssessmentResult):
    try:
        result_data = data.model_dump()
        result_data["assessment_id"] = assessment_id
        result_id = await AssessmentService.submit_result(result_data)
        return APIResponse(success=True, data={"id": result_id}, message="Result submitted")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/assessments/{assessment_id}/results", response_model=APIResponse)
async def get_assessment_results(assessment_id: str):
    try:
        results = await AssessmentService.get_results(assessment_id)
        return APIResponse(success=True, data=results, count=len(results))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ════════════════════════════════════════════════════════════════════════════════
# REPORTS
# ════════════════════════════════════════════════════════════════════════════════

@router.post("/reports", response_model=APIResponse)
async def create_report(data: ReportCreate):
    try:
        report_id = await ReportService.create_report(data.model_dump())
        return APIResponse(success=True, data={"id": report_id}, message="Report created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/reports", response_model=APIResponse)
async def get_reports(report_type: Optional[str] = None):
    try:
        reports = await ReportService.get_all_reports(report_type)
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


# ════════════════════════════════════════════════════════════════════════════════
# NOTICE BOARD
# ════════════════════════════════════════════════════════════════════════════════

@router.post("/notices", response_model=APIResponse)
async def create_notice(data: NoticeCreate):
    try:
        notice_id = await NoticeBoardService.create_notice(data.model_dump())
        return APIResponse(success=True, data={"id": notice_id}, message="Notice posted")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/notices", response_model=APIResponse)
async def get_notices(category: Optional[str] = None):
    try:
        notices = await NoticeBoardService.get_all_notices(category)
        return APIResponse(success=True, data=notices, count=len(notices))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/notices/{notice_id}", response_model=APIResponse)
async def get_notice(notice_id: str):
    try:
        notice = await NoticeBoardService.get_notice(notice_id)
        if not notice:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=notice)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/notices/{notice_id}", response_model=APIResponse)
async def update_notice(notice_id: str, data: NoticeCreate):
    try:
        updated = await NoticeBoardService.update_notice(notice_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/notices/{notice_id}", response_model=APIResponse)
async def delete_notice(notice_id: str):
    try:
        deleted = await NoticeBoardService.delete_notice(notice_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/notices/{notice_id}/pin", response_model=APIResponse)
async def toggle_pin_notice(notice_id: str):
    """Toggle the pinned status of a notice."""
    try:
        toggled = await NoticeBoardService.toggle_pin(notice_id)
        return APIResponse(success=toggled, message="Pin toggled" if toggled else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ════════════════════════════════════════════════════════════════════════════════
# SETTINGS
# ════════════════════════════════════════════════════════════════════════════════

@router.get("/settings", response_model=APIResponse)
async def get_settings(institution_id: Optional[str] = None):
    try:
        settings = await SettingsService.get_settings(institution_id)
        return APIResponse(success=True, data=settings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/settings", response_model=APIResponse)
async def update_settings(data: AcademicSettingsCreate, institution_id: Optional[str] = None):
    try:
        settings_id = await SettingsService.upsert_settings(data.model_dump(), institution_id)
        return APIResponse(success=True, data={"id": settings_id}, message="Settings saved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
