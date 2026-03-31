"""
Payment Admin - API Routes
===========================
FastAPI router for all Payment Admin endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from .models import *
from .services import (
    DashboardService,
    TransactionService,
    FeeCollectionService,
    PaymentReportService,
    RevenueStatsService,
    SettingsService,
    InvoiceService,
)

router = APIRouter(prefix="/payment-admin", tags=["Payment Admin"])


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


@router.post("/transactions", response_model=APIResponse)
async def create_transaction(data: TransactionCreate):
    try:
        tx_id = await TransactionService.create_transaction(data.model_dump())
        return APIResponse(success=True, data={"id": tx_id}, message="Transaction created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/transactions", response_model=APIResponse)
async def get_transactions(
    status: Optional[str] = None,
    student_id: Optional[str] = None,
    payment_type: Optional[str] = None,
    limit: int = Query(100, ge=1, le=500)
):
    try:
        transactions = await TransactionService.get_all_transactions(status, student_id, payment_type, limit)
        return APIResponse(success=True, data=transactions, count=len(transactions))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/transactions/{transaction_id}", response_model=APIResponse)
async def get_transaction(transaction_id: str):
    try:
        transaction = await TransactionService.get_transaction(transaction_id)
        if not transaction:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=transaction)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/transactions/{transaction_id}", response_model=APIResponse)
async def update_transaction(transaction_id: str, data: TransactionCreate):
    try:
        updated = await TransactionService.update_transaction(transaction_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/transactions/{transaction_id}", response_model=APIResponse)
async def delete_transaction(transaction_id: str):
    try:
        deleted = await TransactionService.delete_transaction(transaction_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/transactions/search", response_model=APIResponse)
async def search_transactions(q: str = Query(..., min_length=1)):
    try:
        results = await TransactionService.search_transactions(q)
        return APIResponse(success=True, data=results, count=len(results))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/fee-structures", response_model=APIResponse)
async def create_fee_structure(data: FeeStructureCreate):
    try:
        fee_id = await FeeCollectionService.create_fee_structure(data.model_dump())
        return APIResponse(success=True, data={"id": fee_id}, message="Fee structure created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/fee-structures", response_model=APIResponse)
async def get_fee_structures(
    course_id: Optional[str] = None,
    academic_year: Optional[str] = None
):
    try:
        fees = await FeeCollectionService.get_all_fee_structures(course_id, academic_year)
        return APIResponse(success=True, data=fees, count=len(fees))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/fee-structures/{fee_id}", response_model=APIResponse)
async def get_fee_structure(fee_id: str):
    try:
        fee = await FeeCollectionService.get_fee_structure(fee_id)
        if not fee:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=fee)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/fee-structures/{fee_id}", response_model=APIResponse)
async def update_fee_structure(fee_id: str, data: FeeStructureCreate):
    try:
        updated = await FeeCollectionService.update_fee_structure(fee_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/fee-structures/{fee_id}", response_model=APIResponse)
async def delete_fee_structure(fee_id: str):
    try:
        deleted = await FeeCollectionService.delete_fee_structure(fee_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/student-fees", response_model=APIResponse)
async def get_student_fees(
    student_id: Optional[str] = None,
    status: Optional[str] = None
):
    try:
        fees = await FeeCollectionService.get_student_fees(student_id, status)
        return APIResponse(success=True, data=fees, count=len(fees))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/reports", response_model=APIResponse)
async def create_report(data: PaymentReportCreate):
    try:
        report_id = await PaymentReportService.create_report(data.model_dump())
        return APIResponse(success=True, data={"id": report_id}, message="Report created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/reports", response_model=APIResponse)
async def get_reports(report_type: Optional[str] = None):
    try:
        reports = await PaymentReportService.get_all_reports(report_type)
        return APIResponse(success=True, data=reports, count=len(reports))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/reports/{report_id}", response_model=APIResponse)
async def get_report(report_id: str):
    try:
        report = await PaymentReportService.get_report(report_id)
        if not report:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=report)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/reports/{report_id}", response_model=APIResponse)
async def delete_report(report_id: str):
    try:
        deleted = await PaymentReportService.delete_report(report_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/revenue/period", response_model=APIResponse)
async def get_revenue_by_period(period_type: str = Query("monthly")):
    try:
        stats = await RevenueStatsService.get_revenue_by_period(period_type)
        return APIResponse(success=True, data=stats, count=len(stats))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/revenue/courses", response_model=APIResponse)
async def get_course_revenue():
    try:
        stats = await RevenueStatsService.get_course_revenue()
        return APIResponse(success=True, data=stats, count=len(stats))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/revenue/daily", response_model=APIResponse)
async def get_daily_revenue(days: int = Query(30, ge=1, le=365)):
    try:
        stats = await RevenueStatsService.get_daily_revenue(days)
        return APIResponse(success=True, data=stats, count=len(stats))
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
async def update_settings(data: PaymentSettingsCreate, institution_id: Optional[str] = None):
    try:
        settings_id = await SettingsService.upsert_settings(data.model_dump(), institution_id)
        return APIResponse(success=True, data={"id": settings_id}, message="Settings saved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/invoices", response_model=APIResponse)
async def create_invoice(data: InvoiceCreate):
    try:
        invoice_id = await InvoiceService.create_invoice(data.model_dump())
        return APIResponse(success=True, data={"id": invoice_id}, message="Invoice created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/invoices", response_model=APIResponse)
async def get_invoices(status: Optional[str] = None):
    try:
        invoices = await InvoiceService.get_all_invoices(status)
        return APIResponse(success=True, data=invoices, count=len(invoices))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/invoices/{invoice_id}", response_model=APIResponse)
async def get_invoice(invoice_id: str):
    try:
        invoice = await InvoiceService.get_invoice(invoice_id)
        if not invoice:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=invoice)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/invoices/{invoice_id}", response_model=APIResponse)
async def update_invoice(invoice_id: str, data: InvoiceCreate):
    try:
        updated = await InvoiceService.update_invoice(invoice_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
