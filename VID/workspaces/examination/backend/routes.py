"""
Examination - FastAPI Routes
============================
API endpoints for the Examination workspace.
"""

from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from . import models
from . import services

router = APIRouter(prefix="/api/examination", tags=["Examination"])


@router.get("/dashboard", response_model=models.DashboardStats)
async def get_dashboard():
    """Get dashboard statistics."""
    return await services.DashboardService.get_stats()


@router.get("/dashboard/stats", response_model=models.DashboardStats)
async def get_dashboard_stats():
    """Get dashboard statistics (alias)."""
    return await services.DashboardService.get_stats()


@router.post("/exams", response_model=models.Exam)
async def create_exam(exam: models.ExamCreate):
    """Create a new exam."""
    return await services.ExamService.create(exam.model_dump())


@router.get("/exams", response_model=List[models.Exam])
async def get_all_exams():
    """Get all exams."""
    return await services.ExamService.get_all()


@router.get("/exams/{exam_id}", response_model=models.Exam)
async def get_exam(exam_id: str):
    """Get exam by ID."""
    exam = await services.ExamService.get_by_id(exam_id)
    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")
    return exam


@router.put("/exams/{exam_id}", response_model=models.Exam)
async def update_exam(exam_id: str, exam: models.ExamUpdate):
    """Update an exam."""
    updated = await services.ExamService.update(exam_id, exam.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Exam not found")
    return updated


@router.delete("/exams/{exam_id}")
async def delete_exam(exam_id: str):
    """Delete an exam."""
    deleted = await services.ExamService.delete(exam_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Exam not found")
    return {"message": "Exam deleted successfully"}


@router.post("/schedules", response_model=models.ExamSchedule)
async def create_schedule(schedule: models.ExamScheduleCreate):
    """Create a new exam schedule."""
    return await services.ExamScheduleService.create(schedule.model_dump())


@router.get("/schedules", response_model=List[models.ExamSchedule])
async def get_all_schedules():
    """Get all exam schedules."""
    return await services.ExamScheduleService.get_all()


@router.get("/schedules/exam/{exam_id}", response_model=List[models.ExamSchedule])
async def get_schedules_by_exam(exam_id: str):
    """Get schedules by exam ID."""
    return await services.ExamScheduleService.get_by_exam(exam_id)


@router.put("/schedules/{schedule_id}", response_model=models.ExamSchedule)
async def update_schedule(schedule_id: str, schedule: models.ExamScheduleUpdate):
    """Update an exam schedule."""
    updated = await services.ExamScheduleService.update(schedule_id, schedule.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return updated


@router.delete("/schedules/{schedule_id}")
async def delete_schedule(schedule_id: str):
    """Delete an exam schedule."""
    deleted = await services.ExamScheduleService.delete(schedule_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return {"message": "Schedule deleted successfully"}


@router.post("/hall-tickets", response_model=models.HallTicket)
async def create_hall_ticket(ticket: models.HallTicketCreate):
    """Create a new hall ticket."""
    return await services.HallTicketService.create(ticket.model_dump())


@router.get("/hall-tickets", response_model=List[models.HallTicket])
async def get_all_hall_tickets():
    """Get all hall tickets."""
    return await services.HallTicketService.get_all()


@router.get("/hall-tickets/student/{student_id}", response_model=List[models.HallTicket])
async def get_hall_tickets_by_student(student_id: str):
    """Get hall tickets by student ID."""
    return await services.HallTicketService.get_by_student(student_id)


@router.put("/hall-tickets/{ticket_id}", response_model=models.HallTicket)
async def update_hall_ticket(ticket_id: str, ticket: models.HallTicketUpdate):
    """Update a hall ticket."""
    updated = await services.HallTicketService.update(ticket_id, ticket.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Hall ticket not found")
    return updated


@router.post("/results", response_model=models.Result)
async def create_result(result: models.ResultCreate):
    """Create a new result."""
    return await services.ResultService.create(result.model_dump())


@router.get("/results", response_model=List[models.Result])
async def get_all_results():
    """Get all results."""
    return await services.ResultService.get_all()


@router.get("/results/student/{student_id}", response_model=List[models.Result])
async def get_results_by_student(student_id: str):
    """Get results by student ID."""
    return await services.ResultService.get_by_student(student_id)


@router.put("/results/{result_id}", response_model=models.Result)
async def update_result(result_id: str, result: models.ResultUpdate):
    """Update a result."""
    updated = await services.ResultService.update(result_id, result.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Result not found")
    return updated


@router.post("/reports", response_model=models.Report)
async def create_report(report: models.ReportCreate):
    """Create a new report."""
    return await services.ReportService.create(report.model_dump())


@router.get("/reports", response_model=List[models.Report])
async def get_all_reports():
    """Get all reports."""
    return await services.ReportService.get_all()


@router.get("/reports/type/{report_type}", response_model=List[models.Report])
async def get_reports_by_type(report_type: str):
    """Get reports by type."""
    return await services.ReportService.get_by_type(report_type)


@router.get("/settings")
async def get_settings():
    """Get settings."""
    settings = await services.SettingsService.get()
    if not settings:
        return {"exam_name": "Examination System", "passing_percentage": 35.0, "notification_enabled": True}
    return settings


@router.put("/settings")
async def update_settings(settings: models.SettingsUpdate):
    """Update settings."""
    return await services.SettingsService.update(settings.model_dump(exclude_unset=True))


@router.post("/logout")
async def logout():
    """Logout endpoint."""
    return {"message": "Logged out successfully"}
