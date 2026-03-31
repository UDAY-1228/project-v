"""
Hostel Admin - API Routes
=========================
FastAPI router for all Hostel Admin endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from .models import *
from .services import (
    DashboardService,
    RoomService,
    StudentService,
    FeeRecordService,
    ComplaintService,
    ReportService,
    SettingsService,
)

router = APIRouter(prefix="/hostel-admin", tags=["Hostel Admin"])


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


@router.post("/rooms", response_model=APIResponse)
async def create_room(data: RoomCreate):
    try:
        room_id = await RoomService.create_room(data.model_dump())
        return APIResponse(success=True, data={"id": room_id}, message="Room created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/rooms", response_model=APIResponse)
async def get_rooms(block_name: Optional[str] = None, status: Optional[str] = None):
    try:
        rooms = await RoomService.get_all_rooms(block_name, status)
        return APIResponse(success=True, data=rooms, count=len(rooms))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/rooms/{room_id}", response_model=APIResponse)
async def get_room(room_id: str):
    try:
        room = await RoomService.get_room(room_id)
        if not room:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=room)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/rooms/{room_id}", response_model=APIResponse)
async def update_room(room_id: str, data: RoomCreate):
    try:
        updated = await RoomService.update_room(room_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/rooms/{room_id}", response_model=APIResponse)
async def delete_room(room_id: str):
    try:
        deleted = await RoomService.delete_room(room_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/students", response_model=APIResponse)
async def create_student(data: StudentCreate):
    try:
        student_id = await StudentService.create_student(data.model_dump())
        return APIResponse(success=True, data={"id": student_id}, message="Student created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/students", response_model=APIResponse)
async def get_students(room_id: Optional[str] = None, status: Optional[str] = None):
    try:
        students = await StudentService.get_all_students(room_id, status)
        return APIResponse(success=True, data=students, count=len(students))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/students/{student_id}", response_model=APIResponse)
async def get_student(student_id: str):
    try:
        student = await StudentService.get_student(student_id)
        if not student:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=student)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/students/{student_id}", response_model=APIResponse)
async def update_student(student_id: str, data: StudentCreate):
    try:
        updated = await StudentService.update_student(student_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/students/{student_id}", response_model=APIResponse)
async def delete_student(student_id: str):
    try:
        deleted = await StudentService.delete_student(student_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/fee-records", response_model=APIResponse)
async def create_fee_record(data: FeeRecordCreate):
    try:
        record_id = await FeeRecordService.create_fee_record(data.model_dump())
        return APIResponse(success=True, data={"id": record_id}, message="Fee record created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/fee-records", response_model=APIResponse)
async def get_fee_records(student_id: Optional[str] = None, status: Optional[str] = None, academic_year: Optional[str] = None):
    try:
        records = await FeeRecordService.get_all_fee_records(student_id, status, academic_year)
        return APIResponse(success=True, data=records, count=len(records))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/fee-records/{record_id}", response_model=APIResponse)
async def update_fee_record(record_id: str, data: FeeRecordCreate):
    try:
        updated = await FeeRecordService.update_fee_record(record_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/fee-records/{record_id}/payment", response_model=APIResponse)
async def record_payment(record_id: str, paid_amount: float, payment_method: str, transaction_id: str):
    try:
        recorded = await FeeRecordService.record_payment(record_id, paid_amount, payment_method, transaction_id)
        return APIResponse(success=recorded, message="Payment recorded" if recorded else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/fee-records/{record_id}", response_model=APIResponse)
async def delete_fee_record(record_id: str):
    try:
        deleted = await FeeRecordService.delete_fee_record(record_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/complaints", response_model=APIResponse)
async def create_complaint(data: ComplaintCreate):
    try:
        complaint_id = await ComplaintService.create_complaint(data.model_dump())
        return APIResponse(success=True, data={"id": complaint_id}, message="Complaint created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/complaints", response_model=APIResponse)
async def get_complaints(student_id: Optional[str] = None, status: Optional[str] = None, complaint_type: Optional[str] = None):
    try:
        complaints = await ComplaintService.get_all_complaints(student_id, status, complaint_type)
        return APIResponse(success=True, data=complaints, count=len(complaints))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/complaints/{complaint_id}", response_model=APIResponse)
async def get_complaint(complaint_id: str):
    try:
        complaint = await ComplaintService.get_complaint(complaint_id)
        if not complaint:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=complaint)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/complaints/{complaint_id}", response_model=APIResponse)
async def update_complaint(complaint_id: str, data: ComplaintCreate):
    try:
        updated = await ComplaintService.update_complaint(complaint_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/complaints/{complaint_id}/resolve", response_model=APIResponse)
async def resolve_complaint(complaint_id: str, resolution_notes: str):
    try:
        resolved = await ComplaintService.resolve_complaint(complaint_id, resolution_notes)
        return APIResponse(success=resolved, message="Complaint resolved" if resolved else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/complaints/{complaint_id}", response_model=APIResponse)
async def delete_complaint(complaint_id: str):
    try:
        deleted = await ComplaintService.delete_complaint(complaint_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/reports", response_model=APIResponse)
async def create_report(data: HostelReportCreate):
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
async def update_settings(data: HostelSettingsCreate, institution_id: Optional[str] = None):
    try:
        settings_id = await SettingsService.upsert_settings(data.model_dump(), institution_id)
        return APIResponse(success=True, data={"id": settings_id}, message="Settings saved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
