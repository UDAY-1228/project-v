"""VID Gateway – Notice Board Routes"""
from flask import Blueprint, current_app
from ..utils.proxy import proxy_request
from ..middleware.auth_middleware import require_auth, require_institution_admin

notice_bp = Blueprint("notices", __name__)


@notice_bp.get("/")
@require_auth
def list_notices():
    return proxy_request(current_app.config["NOTICE_SERVICE_URL"], "/notices/")


@notice_bp.post("/")
@require_institution_admin
def create_notice():
    return proxy_request(current_app.config["NOTICE_SERVICE_URL"], "/notices/")


@notice_bp.get("/<notice_id>")
@require_auth
def get_notice(notice_id):
    return proxy_request(current_app.config["NOTICE_SERVICE_URL"], f"/notices/{notice_id}")


@notice_bp.put("/<notice_id>")
@require_institution_admin
def update_notice(notice_id):
    return proxy_request(current_app.config["NOTICE_SERVICE_URL"], f"/notices/{notice_id}")


@notice_bp.delete("/<notice_id>")
@require_institution_admin
def delete_notice(notice_id):
    return proxy_request(current_app.config["NOTICE_SERVICE_URL"], f"/notices/{notice_id}")
