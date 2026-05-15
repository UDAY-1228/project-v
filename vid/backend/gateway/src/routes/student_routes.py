"""VID Gateway – Student Routes"""
from flask import Blueprint, current_app
from ..utils.proxy import proxy_request
from ..middleware.auth_middleware import require_auth, require_institution_admin, require_roles

student_bp = Blueprint("students", __name__)


@student_bp.get("/")
@require_roles("SUPER_ADMIN", "INSTITUTION_ADMIN", "FACULTY")
def list_students():
    return proxy_request(current_app.config["STUDENT_SERVICE_URL"], "/students/")


@student_bp.post("/")
@require_institution_admin
def create_student():
    return proxy_request(current_app.config["STUDENT_SERVICE_URL"], "/students/")


@student_bp.get("/<student_id>")
@require_auth
def get_student(student_id):
    return proxy_request(current_app.config["STUDENT_SERVICE_URL"], f"/students/{student_id}")


@student_bp.put("/<student_id>")
@require_institution_admin
def update_student(student_id):
    return proxy_request(current_app.config["STUDENT_SERVICE_URL"], f"/students/{student_id}")


@student_bp.delete("/<student_id>")
@require_institution_admin
def delete_student(student_id):
    return proxy_request(current_app.config["STUDENT_SERVICE_URL"], f"/students/{student_id}")


@student_bp.get("/<student_id>/profile")
@require_auth
def student_profile(student_id):
    return proxy_request(current_app.config["STUDENT_SERVICE_URL"], f"/students/{student_id}/profile")


@student_bp.get("/<student_id>/attendance")
@require_auth
def student_attendance(student_id):
    return proxy_request(current_app.config["ATTENDANCE_SERVICE_URL"], f"/attendance/student/{student_id}")


@student_bp.get("/<student_id>/marks")
@require_auth
def student_marks(student_id):
    return proxy_request(current_app.config["EXAMINATION_SERVICE_URL"], f"/marks/student/{student_id}")


@student_bp.get("/<student_id>/fees")
@require_auth
def student_fees(student_id):
    return proxy_request(current_app.config["PAYMENT_SERVICE_URL"], f"/fees/student/{student_id}")
