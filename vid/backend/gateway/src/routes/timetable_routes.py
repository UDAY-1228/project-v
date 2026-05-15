"""VID Gateway – Timetable Routes"""
from flask import Blueprint, current_app
from ..utils.proxy import proxy_request
from ..middleware.auth_middleware import require_auth, require_institution_admin, require_roles

timetable_bp = Blueprint("timetable", __name__)


@timetable_bp.get("/class/<class_id>")
@require_auth
def class_timetable(class_id):
    return proxy_request(current_app.config["TIMETABLE_SERVICE_URL"], f"/timetable/class/{class_id}")


@timetable_bp.post("/")
@require_institution_admin
def create_timetable_entry():
    return proxy_request(current_app.config["TIMETABLE_SERVICE_URL"], "/timetable/")


@timetable_bp.put("/<entry_id>")
@require_institution_admin
def update_timetable_entry(entry_id):
    return proxy_request(current_app.config["TIMETABLE_SERVICE_URL"], f"/timetable/{entry_id}")


@timetable_bp.delete("/<entry_id>")
@require_institution_admin
def delete_timetable_entry(entry_id):
    return proxy_request(current_app.config["TIMETABLE_SERVICE_URL"], f"/timetable/{entry_id}")


@timetable_bp.get("/faculty/<faculty_id>")
@require_auth
def faculty_timetable(faculty_id):
    return proxy_request(current_app.config["TIMETABLE_SERVICE_URL"], f"/timetable/faculty/{faculty_id}")
