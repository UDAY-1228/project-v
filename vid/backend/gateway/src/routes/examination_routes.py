"""VID Gateway – Examination Routes"""
from flask import Blueprint, current_app
from ..utils.proxy import proxy_request
from ..middleware.auth_middleware import require_auth, require_institution_admin, require_roles

examination_bp = Blueprint("examinations", __name__)

# ── Exams ─────────────────────────────────────────────────────────────────────

@examination_bp.get("/")
@require_auth
def list_exams():
    return proxy_request(current_app.config["EXAMINATION_SERVICE_URL"], "/exams/")


@examination_bp.post("/")
@require_institution_admin
def create_exam():
    return proxy_request(current_app.config["EXAMINATION_SERVICE_URL"], "/exams/")


@examination_bp.get("/<exam_id>")
@require_auth
def get_exam(exam_id):
    return proxy_request(current_app.config["EXAMINATION_SERVICE_URL"], f"/exams/{exam_id}")


@examination_bp.put("/<exam_id>")
@require_institution_admin
def update_exam(exam_id):
    return proxy_request(current_app.config["EXAMINATION_SERVICE_URL"], f"/exams/{exam_id}")

# ── Marks ─────────────────────────────────────────────────────────────────────

@examination_bp.post("/<exam_id>/marks")
@require_roles("SUPER_ADMIN", "INSTITUTION_ADMIN", "FACULTY")
def enter_marks(exam_id):
    return proxy_request(current_app.config["EXAMINATION_SERVICE_URL"], f"/exams/{exam_id}/marks")


@examination_bp.get("/<exam_id>/marks")
@require_auth
def get_exam_marks(exam_id):
    return proxy_request(current_app.config["EXAMINATION_SERVICE_URL"], f"/exams/{exam_id}/marks")


@examination_bp.get("/<exam_id>/report-card")
@require_auth
def report_card(exam_id):
    return proxy_request(current_app.config["EXAMINATION_SERVICE_URL"], f"/exams/{exam_id}/report-card")
