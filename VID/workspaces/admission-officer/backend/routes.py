"""
Admission Officer - API Routes
===============================
FastAPI router for all Admission Officer endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from .models import *
from .services import (
    DashboardService,
    ApplicationService,
    StudentAdmissionService,
    DocumentVerificationService,
    FeeDetailsService,
    ReportService,
    SettingsService,
)

router = APIRouter(prefix="/admission-officer", tags=["Admission Officer"])


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


@router.post("/applications", response_model=APIResponse)
async def create_application(data: ApplicationCreate):
    try:
        app_id = await ApplicationService.create_application(data.model_dump())
        return APIResponse(success=True, data={"id": app_id}, message="Application created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/applications", response_model=APIResponse)
async def get_applications(status: Optional[str] = None):
    try:
        apps = await ApplicationService.get_all_applications(status)
        return APIResponse(success=True, data=apps, count=len(apps))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/applications/{app_id}", response_model=APIResponse)
async def get_application(app_id: str):
    try:
        app = await ApplicationService.get_application(app_id)
        if not app:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=app)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/applications/{app_id}", response_model=APIResponse)
async def update_application(app_id: str, data: ApplicationCreate):
    try:
        updated = await ApplicationService.update_application(app_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/applications/{app_id}", response_model=APIResponse)
async def delete_application(app_id: str):
    try:
        deleted = await ApplicationService.delete_application(app_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/admissions", response_model=APIResponse)
async def create_admission(data: StudentAdmissionCreate):
    try:
        adm_id = await StudentAdmissionService.create_admission(data.model_dump())
        return APIResponse(success=True, data={"id": adm_id}, message="Admission created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/admissions", response_model=APIResponse)
async def get_admissions(course: Optional[str] = None, batch: Optional[str] = None):
    try:
        adms = await StudentAdmissionService.get_all_admissions(course, batch)
        return APIResponse(success=True, data=adms, count=len(adms))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/admissions/{admission_id}", response_model=APIResponse)
async def get_admission(admission_id: str):
    try:
        adm = await StudentAdmissionService.get_admission(admission_id)
        if not adm:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=adm)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/admissions/{admission_id}", response_model=APIResponse)
async def update_admission(admission_id: str, data: StudentAdmissionCreate):
    try:
        updated = await StudentAdmissionService.update_admission(admission_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/admissions/{admission_id}", response_model=APIResponse)
async def delete_admission(admission_id: str):
    try:
        deleted = await StudentAdmissionService.delete_admission(admission_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/documents", response_model=APIResponse)
async def create_verification(data: DocumentVerificationCreate):
    try:
        doc_id = await DocumentVerificationService.create_verification(data.model_dump())
        return APIResponse(success=True, data={"id": doc_id}, message="Verification created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/documents", response_model=APIResponse)
async def get_verifications(status: Optional[str] = None):
    try:
        docs = await DocumentVerificationService.get_all_verifications(status)
        return APIResponse(success=True, data=docs, count=len(docs))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/documents/{doc_id}", response_model=APIResponse)
async def get_verification(doc_id: str):
    try:
        doc = await DocumentVerificationService.get_verification(doc_id)
        if not doc:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=doc)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/documents/{doc_id}", response_model=APIResponse)
async def update_verification(doc_id: str, data: DocumentVerificationCreate):
    try:
        updated = await DocumentVerificationService.update_verification(doc_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/documents/{doc_id}/approve", response_model=APIResponse)
async def approve_document(doc_id: str, verified_by: str):
    try:
        approved = await DocumentVerificationService.approve_document(doc_id, verified_by)
        return APIResponse(success=approved, message="Document approved" if approved else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/fees", response_model=APIResponse)
async def create_fee_details(data: FeeDetailsCreate):
    try:
        fee_id = await FeeDetailsService.create_fee_details(data.model_dump())
        return APIResponse(success=True, data={"id": fee_id}, message="Fee details created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/fees", response_model=APIResponse)
async def get_fee_details(student_id: Optional[str] = None, payment_status: Optional[str] = None):
    try:
        fees = await FeeDetailsService.get_all_fee_details(student_id, payment_status)
        return APIResponse(success=True, data=fees, count=len(fees))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/fees/{fee_id}", response_model=APIResponse)
async def get_fee_detail(fee_id: str):
    try:
        fee = await FeeDetailsService.get_fee_details(fee_id)
        if not fee:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=fee)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/fees/{fee_id}", response_model=APIResponse)
async def update_fee_details(fee_id: str, data: FeeDetailsCreate):
    try:
        updated = await FeeDetailsService.update_fee_details(fee_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/fees/{fee_id}/payment", response_model=APIResponse)
async def record_payment(fee_id: str, amount: float, payment_method: str):
    try:
        recorded = await FeeDetailsService.record_payment(fee_id, amount, payment_method)
        return APIResponse(success=recorded, message="Payment recorded" if recorded else "Not found")
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
