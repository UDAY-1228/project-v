"""VID Gateway – Academic Routes (Classes & Subjects)"""
from flask import Blueprint, current_app
from ..utils.proxy import proxy_request
from ..middleware.auth_middleware import require_auth, require_institution_admin, require_roles

academic_bp = Blueprint("academic", __name__)

# ── Classes ──────────────────────────────────────────────────────────────────

@academic_bp.get("/classes")
@require_auth
def list_classes():
    return proxy_request(current_app.config["ACADEMIC_SERVICE_URL"], "/classes/")


@academic_bp.post("/classes")
@require_institution_admin
def create_class():
    return proxy_request(current_app.config["ACADEMIC_SERVICE_URL"], "/classes/")


@academic_bp.get("/classes/<class_id>")
@require_auth
def get_class(class_id):
    return proxy_request(current_app.config["ACADEMIC_SERVICE_URL"], f"/classes/{class_id}")


@academic_bp.put("/classes/<class_id>")
@require_institution_admin
def update_class(class_id):
    return proxy_request(current_app.config["ACADEMIC_SERVICE_URL"], f"/classes/{class_id}")


@academic_bp.get("/classes/<class_id>/students")
@require_roles("SUPER_ADMIN", "INSTITUTION_ADMIN", "FACULTY")
def class_students(class_id):
    return proxy_request(current_app.config["ACADEMIC_SERVICE_URL"], f"/classes/{class_id}/students")

# ── Subjects ──────────────────────────────────────────────────────────────────

@academic_bp.get("/subjects")
@require_auth
def list_subjects():
    return proxy_request(current_app.config["ACADEMIC_SERVICE_URL"], "/subjects/")


@academic_bp.post("/subjects")
@require_institution_admin
def create_subject():
    return proxy_request(current_app.config["ACADEMIC_SERVICE_URL"], "/subjects/")


@academic_bp.get("/subjects/<subject_id>")
@require_auth
def get_subject(subject_id):
    return proxy_request(current_app.config["ACADEMIC_SERVICE_URL"], f"/subjects/{subject_id}")


@academic_bp.put("/subjects/<subject_id>")
@require_institution_admin
def update_subject(subject_id):
    return proxy_request(current_app.config["ACADEMIC_SERVICE_URL"], f"/subjects/{subject_id}")

# ── Academic Years ────────────────────────────────────────────────────────────

@academic_bp.get("/years")
@require_auth
def list_years():
    return proxy_request(current_app.config["ACADEMIC_SERVICE_URL"], "/years/")


@academic_bp.post("/years")
@require_institution_admin
def create_year():
    return proxy_request(current_app.config["ACADEMIC_SERVICE_URL"], "/years/")
