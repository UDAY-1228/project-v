"""
Library Management - API Routes
===============================
FastAPI router for all Library Management endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from .models import *
from .services import (
    DashboardService,
    BookCatalogService,
    IssueReturnService,
    MemberRecordsService,
    ReportService,
    SettingsService,
)

router = APIRouter(prefix="/library-management", tags=["Library Management"])


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


@router.post("/catalog", response_model=APIResponse)
async def add_book(data: BookCatalogCreate):
    try:
        book_id = await BookCatalogService.add_book(data.model_dump())
        return APIResponse(success=True, data={"id": book_id}, message="Book added to catalog")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/catalog", response_model=APIResponse)
async def get_books(category: Optional[str] = None, search: Optional[str] = None):
    try:
        books = await BookCatalogService.get_all_books(category, search)
        return APIResponse(success=True, data=books, count=len(books))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/catalog/{book_id}", response_model=APIResponse)
async def get_book(book_id: str):
    try:
        book = await BookCatalogService.get_book(book_id)
        if not book:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=book)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/catalog/{book_id}", response_model=APIResponse)
async def update_book(book_id: str, data: BookCatalogCreate):
    try:
        updated = await BookCatalogService.update_book(book_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/catalog/{book_id}", response_model=APIResponse)
async def delete_book(book_id: str):
    try:
        deleted = await BookCatalogService.delete_book(book_id)
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


@router.post("/issues/{issue_id}/return", response_model=APIResponse)
async def return_book(issue_id: str, remarks: Optional[str] = None):
    try:
        returned = await IssueReturnService.return_book(issue_id, remarks)
        return APIResponse(success=returned, message="Book returned" if returned else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/members/{member_id}/history", response_model=APIResponse)
async def get_member_history(member_id: str):
    try:
        history = await IssueReturnService.get_member_history(member_id)
        return APIResponse(success=True, data=history, count=len(history))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/members", response_model=APIResponse)
async def create_member(data: MemberRecordCreate):
    try:
        member_id = await MemberRecordsService.create_member(data.model_dump())
        return APIResponse(success=True, data={"id": member_id}, message="Member created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/members", response_model=APIResponse)
async def get_members(member_type: Optional[str] = None, status: Optional[str] = None):
    try:
        members = await MemberRecordsService.get_all_members(member_type, status)
        return APIResponse(success=True, data=members, count=len(members))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/members/{member_id}", response_model=APIResponse)
async def get_member(member_id: str):
    try:
        member = await MemberRecordsService.get_member(member_id)
        if not member:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=member)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/members/{member_id}", response_model=APIResponse)
async def update_member(member_id: str, data: MemberRecordCreate):
    try:
        updated = await MemberRecordsService.update_member(member_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/members/{member_id}", response_model=APIResponse)
async def delete_member(member_id: str):
    try:
        deleted = await MemberRecordsService.delete_member(member_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
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
