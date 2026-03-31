"""
Payment Admin - Pydantic Models
================================
Data models for all Payment Admin pages:
Dashboard, Transactions, Fee Collection, Payment Reports, Revenue Stats, Settings
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    pending = "pending"
    completed = "completed"
    failed = "failed"
    refunded = "refunded"


class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None
    count: Optional[int] = None


class PaginationParams(BaseModel):
    page: int = 1
    limit: int = 20
    sort_by: str = "created_at"
    sort_order: str = "desc"


# Dashboard

class DashboardStats(BaseModel):
    total_revenue: float = 0.0
    total_transactions: int = 0
    pending_payments: int = 0
    completed_payments: int = 0
    failed_payments: int = 0
    pending_invoices: int = 0


class DashboardActivity(BaseModel):
    id: Optional[str] = None
    action: str
    actor: str
    module: str
    description: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


# Transactions

class TransactionBase(BaseModel):
    transaction_id: Optional[str] = None
    student_id: str
    student_name: str
    amount: float
    payment_mode: str = "online"
    payment_type: str = "fee"
    fee_type: Optional[str] = None
    academic_year: Optional[str] = None
    semester: Optional[str] = None
    reference_number: Optional[str] = None
    bank_reference: Optional[str] = None
    description: Optional[str] = None
    status: StatusEnum = StatusEnum.pending


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: str
    transaction_date: datetime = Field(default_factory=datetime.utcnow)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class TransactionFilter(BaseModel):
    student_id: Optional[str] = None
    status: Optional[str] = None
    payment_type: Optional[str] = None
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None


# Fee Collection

class FeeStructureBase(BaseModel):
    fee_name: str
    fee_code: str
    course_id: Optional[str] = None
    semester: Optional[str] = None
    academic_year: str
    amount: float
    due_date: datetime
    late_fee_amount: float = 0.0
    is_mandatory: bool = True
    description: Optional[str] = None
    status: StatusEnum = StatusEnum.active


class FeeStructureCreate(FeeStructureBase):
    pass


class FeeStructure(FeeStructureBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class StudentFeeBase(BaseModel):
    student_id: str
    student_name: str
    fee_structure_id: str
    amount_payable: float
    amount_paid: float = 0.0
    balance_amount: float = 0.0
    payment_status: StatusEnum = StatusEnum.pending
    due_date: datetime
    paid_date: Optional[datetime] = None


class StudentFeeCreate(StudentFeeBase):
    pass


class StudentFee(StudentFeeBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Payment Reports

class PaymentReportBase(BaseModel):
    report_name: str
    report_type: str = "summary"
    start_date: datetime
    end_date: datetime
    generated_by: Optional[str] = None
    filters: Optional[Dict[str, Any]] = {}
    total_amount: float = 0.0
    total_transactions: int = 0
    status: StatusEnum = StatusEnum.pending


class PaymentReportCreate(PaymentReportBase):
    pass


class PaymentReport(PaymentReportBase):
    id: str
    file_url: Optional[str] = None
    generated_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Revenue Stats

class RevenueStatsBase(BaseModel):
    period: str
    period_type: str = "monthly"
    total_revenue: float = 0.0
    total_transactions: int = 0
    successful_payments: int = 0
    failed_payments: int = 0
    average_transaction_value: float = 0.0


class RevenueStats(RevenueStatsBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class CourseRevenue(BaseModel):
    course_id: str
    course_name: str
    total_revenue: float = 0.0
    student_count: int = 0
    collection_percentage: float = 0.0


# Settings

class PaymentSettingsBase(BaseModel):
    institution_name: str = "VID Institute"
    gst_percentage: float = 18.0
    late_fee_percentage: float = 1.5
    late_fee_grace_days: int = 15
    currency: str = "INR"
    payment_gateway_enabled: bool = True
    auto_receipt_generation: bool = True
    email_notifications: bool = True
    reminder_days: List[int] = [7, 3, 1]


class PaymentSettingsCreate(PaymentSettingsBase):
    pass


class PaymentSettings(PaymentSettingsBase):
    id: str
    institution_id: Optional[str] = None
    updated_by: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Invoice

class InvoiceBase(BaseModel):
    invoice_number: str
    student_id: str
    student_name: str
    amount: float
    tax_amount: float = 0.0
    total_amount: float
    status: StatusEnum = StatusEnum.pending
    payment_id: Optional[str] = None


class InvoiceCreate(InvoiceBase):
    pass


class Invoice(InvoiceBase):
    id: str
    issued_date: datetime = Field(default_factory=datetime.utcnow)
    due_date: datetime
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
