"""VID Gateway – Institution Routes"""
from flask import Blueprint, current_app
from ..utils.proxy import proxy_request
from ..middleware.auth_middleware import require_auth, require_super_admin, require_institution_admin

institution_bp = Blueprint("institutions", __name__)


@institution_bp.get("/")
@require_super_admin
def list_institutions():
    return proxy_request(current_app.config["INSTITUTION_SERVICE_URL"], "/institutions/")


@institution_bp.post("/")
@require_super_admin
def create_institution():
    return proxy_request(current_app.config["INSTITUTION_SERVICE_URL"], "/institutions/")


@institution_bp.get("/<institution_id>")
@require_institution_admin
def get_institution(institution_id):
    return proxy_request(current_app.config["INSTITUTION_SERVICE_URL"], f"/institutions/{institution_id}")


@institution_bp.put("/<institution_id>")
@require_institution_admin
def update_institution(institution_id):
    return proxy_request(current_app.config["INSTITUTION_SERVICE_URL"], f"/institutions/{institution_id}")


@institution_bp.get("/<institution_id>/stats")
@require_institution_admin
def institution_stats(institution_id):
    return proxy_request(current_app.config["INSTITUTION_SERVICE_URL"], f"/institutions/{institution_id}/stats")
