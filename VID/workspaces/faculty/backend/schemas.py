"""
Faculty - Request/Response Schemas
==================================
Pydantic schemas for API request/response validation.
"""

from .models import (
    FacultyProfileCreate,
    FacultyProfile,
    ClassCreate,
    Class,
    AttendanceCreate,
    AttendanceSummary,
    AttendanceReport,
    AssignmentCreate,
    Assignment,
    AssignmentSubmission,
    ExamCreate,
    Exam,
    ExamResult,
    ExamResultCreate,
    ReportCreate,
    Report,
    FacultySettingsCreate,
    FacultySettings,
    DashboardStats,
    DashboardActivity,
    StatusEnum,
    AttendanceStatusEnum,
    GradeEnum,
    ExamTypeEnum,
)

__all__ = [
    "FacultyProfileCreate",
    "FacultyProfile",
    "ClassCreate",
    "Class",
    "AttendanceCreate",
    "AttendanceSummary",
    "AttendanceReport",
    "AssignmentCreate",
    "Assignment",
    "AssignmentSubmission",
    "ExamCreate",
    "Exam",
    "ExamResult",
    "ExamResultCreate",
    "ReportCreate",
    "Report",
    "FacultySettingsCreate",
    "FacultySettings",
    "DashboardStats",
    "DashboardActivity",
    "StatusEnum",
    "AttendanceStatusEnum",
    "GradeEnum",
    "ExamTypeEnum",
]