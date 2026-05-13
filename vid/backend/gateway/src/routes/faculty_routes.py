"""VID Gateway – Faculty Routes"""
from flask import Blueprint, current_app
from ..utils.proxy import proxy_request
from ..middleware.auth_middleware import require_auth, require_institution_admin, require_roles

faculty_bp = Blueprint("faculty", __name__)


@faculty_bp.get("/")
@require_roles("SUPER_ADMIN", "INSTITUTION_ADMIN")
def list_faculty():
    return proxy_request(current_app.config["FACULTY_SERVICE_URL"], "/faculty/")


@faculty_bp.post("/")
@require_institution_admin
def create_faculty():
    return proxy_request(current_app.config["FACULTY_SERVICE_URL"], "/faculty/")


@faculty_bp.get("/<faculty_id>")
@require_auth
def get_faculty(faculty_id):
    return proxy_request(current_app.config["FACULTY_SERVICE_URL"], f"/faculty/{faculty_id}")


@faculty_bp.put("/<faculty_id>")
@require_institution_admin
def update_faculty(faculty_id):
    return proxy_request(current_app.config["FACULTY_SERVICE_URL"], f"/faculty/{faculty_id}")


@faculty_bp.get("/<faculty_id>/classes")
@require_auth
def faculty_classes(faculty_id):
    return proxy_request(current_app.config["FACULTY_SERVICE_URL"], f"/faculty/{faculty_id}/classes")


@faculty_bp.get("/<faculty_id>/timetable")
@require_auth
def faculty_timetable(faculty_id):
    return proxy_request(current_app.config["TIMETABLE_SERVICE_URL"], f"/timetable/faculty/{faculty_id}")
