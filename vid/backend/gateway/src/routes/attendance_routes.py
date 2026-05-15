"""VID Gateway – Attendance Routes"""
from flask import Blueprint, current_app
from ..utils.proxy import proxy_request
from ..middleware.auth_middleware import require_auth, require_roles

attendance_bp = Blueprint("attendance", __name__)


@attendance_bp.post("/mark")
@require_roles("SUPER_ADMIN", "INSTITUTION_ADMIN", "FACULTY")
def mark_attendance():
    return proxy_request(current_app.config["ATTENDANCE_SERVICE_URL"], "/attendance/mark")


@attendance_bp.post("/mark/bulk")
@require_roles("SUPER_ADMIN", "INSTITUTION_ADMIN", "FACULTY")
def mark_bulk_attendance():
    return proxy_request(current_app.config["ATTENDANCE_SERVICE_URL"], "/attendance/mark/bulk")


@attendance_bp.get("/class/<class_id>")
@require_roles("SUPER_ADMIN", "INSTITUTION_ADMIN", "FACULTY")
def class_attendance(class_id):
    return proxy_request(current_app.config["ATTENDANCE_SERVICE_URL"], f"/attendance/class/{class_id}")


@attendance_bp.get("/student/<student_id>")
@require_auth
def student_attendance(student_id):
    return proxy_request(current_app.config["ATTENDANCE_SERVICE_URL"], f"/attendance/student/{student_id}")


@attendance_bp.get("/report")
@require_roles("SUPER_ADMIN", "INSTITUTION_ADMIN", "FACULTY")
def attendance_report():
    return proxy_request(current_app.config["ATTENDANCE_SERVICE_URL"], "/attendance/report")
