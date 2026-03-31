"""
Library Admin - API Routes
===========================
FastAPI router for all Library Admin endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from .models import *
from .services import (
    DashboardService,
    BookControlService,
    IssueReturnService,
    FineControlService,
    ReportService,
    SettingsService,
)

router = APIRouter(prefix="/library-admin", tags=["Library Admin"])


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


@router.post("/books", response_model=APIResponse)
async def create_book(data: BookCreate):
    try:
        book_id = await BookControlService.create_book(data.model_dump())
        return APIResponse(success=True, data={"id": book_id}, message="Book created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/books", response_model=APIResponse)
async def get_books(category: Optional[str] = None, status: Optional[str] = None):
    try:
        books = await BookControlService.get_all_books(category, status)
        return APIResponse(success=True, data=books, count=len(books))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/books/{book_id}", response_model=APIResponse)
async def get_book(book_id: str):
    try:
        book = await BookControlService.get_book(book_id)
        if not book:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=book)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/books/{book_id}", response_model=APIResponse)
async def update_book(book_id: str, data: BookCreate):
    try:
        updated = await BookControlService.update_book(book_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/books/{book_id}", response_model=APIResponse)
async def delete_book(book_id: str):
    try:
        deleted = await BookControlService.delete_book(book_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/issues", response_model=APIResponse)
async def issue_book(data: IssueReturnCreate):
    try:
        issue_id = await IssueReturnService.issue_book(data.model_dump())
        return APIResponse(success=True, data={"id": issue_id}, message="Book issued")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/issues", response_model=APIResponse)
async def get_issues(status: Optional[str] = None):
    try:
        issues = await IssueReturnService.get_all_issues(status)
        return APIResponse(success=True, data=issues, count=len(issues))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/issues/{issue_id}", response_model=APIResponse)
async def get_issue(issue_id: str):
    try:
        issue = await IssueReturnService.get_issue(issue_id)
        if not issue:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=issue)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/members/{member_id}/issues", response_model=APIResponse)
async def get_member_issues(member_id: str):
    try:
        issues = await IssueReturnService.get_member_issues(member_id)
        return APIResponse(success=True, data=issues, count=len(issues))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/issues/{issue_id}/return", response_model=APIResponse)
async def return_book(issue_id: str, fine_amount: float = Query(0.0, ge=0)):
    try:
        returned = await IssueReturnService.return_book(issue_id, fine_amount)
        return APIResponse(success=returned, message="Book returned" if returned else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/fines", response_model=APIResponse)
async def create_fine(data: FineControlCreate):
    try:
        fine_id = await FineControlService.create_fine(data.model_dump())
        return APIResponse(success=True, data={"id": fine_id}, message="Fine created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/fines", response_model=APIResponse)
async def get_fines(member_id: Optional[str] = None, status: Optional[str] = None):
    try:
        fines = await FineControlService.get_all_fines(member_id, status)
        return APIResponse(success=True, data=fines, count=len(fines))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/fines/{fine_id}", response_model=APIResponse)
async def get_fine(fine_id: str):
    try:
        fine = await FineControlService.get_fine(fine_id)
        if not fine:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=fine)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/fines/{fine_id}", response_model=APIResponse)
async def update_fine(fine_id: str, data: FineControlCreate):
    try:
        updated = await FineControlService.update_fine(fine_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/fines/{fine_id}/pay", response_model=APIResponse)
async def pay_fine(fine_id: str):
    try:
        paid = await FineControlService.pay_fine(fine_id)
        return APIResponse(success=paid, message="Fine paid" if paid else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/fines/{fine_id}/calculate", response_model=APIResponse)
async def calculate_fine(issue_id: str, fine_per_day: float = Query(5.0, gt=0)):
    try:
        amount = await FineControlService.calculate_fine(issue_id, fine_per_day)
        return APIResponse(success=True, data={"fine_amount": amount})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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


@router.get("/settings", response_model=APIResponse)
async def get_settings():
    try:
        settings = await SettingsService.get_settings()
        return APIResponse(success=True, data=settings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/settings", response_model=APIResponse)
async def update_settings(data: SettingsCreate):
    try:
        settings_id = await SettingsService.upsert_settings(data.model_dump())
        return APIResponse(success=True, data={"id": settings_id}, message="Settings saved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
