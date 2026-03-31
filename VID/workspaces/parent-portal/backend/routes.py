"""
Parent Portal - API Routes
==========================
FastAPI router for all Parent Portal endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from datetime import datetime
from .models import *
from .services import (
    DashboardService,
    StudentProgressService,
    AttendanceService,
    FeeStatusService,
    NotificationService,
    SettingsService,
)

router = APIRouter(prefix="/parent-portal", tags=["Parent Portal"])


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


@router.post("/student-progress", response_model=APIResponse)
async def create_student_progress(data: StudentProgressCreate):
    try:
        progress_id = await StudentProgressService.create_progress(data.model_dump())
        return APIResponse(success=True, data={"id": progress_id}, message="Progress record created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/student-progress", response_model=APIResponse)
async def get_student_progress(student_id: Optional[str] = None):
    try:
        progress = await StudentProgressService.get_all_progress(student_id)
        return APIResponse(success=True, data=progress, count=len(progress))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/student-progress/{progress_id}", response_model=APIResponse)
async def get_student_progress_record(progress_id: str):
    try:
        progress = await StudentProgressService.get_progress(progress_id)
        if not progress:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=progress)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/student-progress/{progress_id}", response_model=APIResponse)
async def update_student_progress(progress_id: str, data: StudentProgressCreate):
    try:
        updated = await StudentProgressService.update_progress(progress_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/attendance", response_model=APIResponse)
async def mark_attendance(data: AttendanceCreate):
    try:
        attendance_id = await AttendanceService.mark_attendance(data.model_dump())
        return APIResponse(success=True, data={"id": attendance_id}, message="Attendance marked")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/attendance", response_model=APIResponse)
async def get_attendance(
    student_id: str = Query(..., min_length=1),
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
):
    try:
        attendance = await AttendanceService.get_attendance(student_id, start_date, end_date)
        return APIResponse(success=True, data=attendance, count=len(attendance))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/attendance/summary", response_model=APIResponse)
async def get_attendance_summary(student_id: str = Query(..., min_length=1)):
    try:
        summary = await AttendanceService.get_attendance_summary(student_id)
        return APIResponse(success=True, data=summary)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/fees", response_model=APIResponse)
async def create_fee(data: FeeStatusCreate):
    try:
        fee_id = await FeeStatusService.create_fee(data.model_dump())
        return APIResponse(success=True, data={"id": fee_id}, message="Fee record created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/fees", response_model=APIResponse)
async def get_fees(student_id: Optional[str] = None):
    try:
        fees = await FeeStatusService.get_all_fees(student_id)
        return APIResponse(success=True, data=fees, count=len(fees))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/fees/{fee_id}", response_model=APIResponse)
async def get_fee_record(fee_id: str):
    try:
        fee = await FeeStatusService.get_fee(fee_id)
        if not fee:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=fee)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/fees/{fee_id}/payment", response_model=APIResponse)
async def make_payment(fee_id: str, data: FeePayment):
    try:
        paid = await FeeStatusService.make_payment(fee_id, data.model_dump())
        return APIResponse(success=paid, message="Payment successful" if paid else "Payment failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/fees/{fee_id}/payments", response_model=APIResponse)
async def get_payment_history(fee_id: str):
    try:
        payments = await FeeStatusService.get_payment_history(fee_id)
        return APIResponse(success=True, data=payments, count=len(payments))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/notifications", response_model=APIResponse)
async def create_notification(data: NotificationCreate):
    try:
        notif_id = await NotificationService.create_notification(data.model_dump())
        return APIResponse(success=True, data={"id": notif_id}, message="Notification created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/notifications", response_model=APIResponse)
async def get_notifications(recipient_id: Optional[str] = None):
    try:
        notifications = await NotificationService.get_notifications(recipient_id)
        return APIResponse(success=True, data=notifications, count=len(notifications))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/notifications/{notification_id}/read", response_model=APIResponse)
async def mark_notification_read(notification_id: str):
    try:
        marked = await NotificationService.mark_as_read(notification_id)
        return APIResponse(success=marked, message="Marked as read" if marked else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/notifications/{notification_id}", response_model=APIResponse)
async def delete_notification(notification_id: str):
    try:
        deleted = await NotificationService.delete_notification(notification_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/settings", response_model=APIResponse)
async def get_settings(parent_id: Optional[str] = None):
    try:
        settings = await SettingsService.get_settings(parent_id)
        return APIResponse(success=True, data=settings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/settings", response_model=APIResponse)
async def update_settings(data: SettingsCreate, parent_id: Optional[str] = None):
    try:
        settings_id = await SettingsService.upsert_settings(data.model_dump(), parent_id)
        return APIResponse(success=True, data={"id": settings_id}, message="Settings saved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
