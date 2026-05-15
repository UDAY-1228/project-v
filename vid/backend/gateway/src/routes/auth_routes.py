"""
VID API Gateway – Auth Routes
Proxies to Auth Microservice (FastAPI on port 8001)
"""
from flask import Blueprint, current_app
from ..utils.proxy import proxy_request
from ..middleware.auth_middleware import require_auth

auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/login")
def login():
    """POST /api/v1/auth/login"""
    return proxy_request(current_app.config["AUTH_SERVICE_URL"], "/auth/login")


@auth_bp.post("/logout")
@require_auth
def logout():
    """POST /api/v1/auth/logout"""
    return proxy_request(current_app.config["AUTH_SERVICE_URL"], "/auth/logout")


@auth_bp.post("/refresh")
def refresh():
    """POST /api/v1/auth/refresh"""
    return proxy_request(current_app.config["AUTH_SERVICE_URL"], "/auth/refresh")


@auth_bp.post("/register")
def register():
    """POST /api/v1/auth/register  (initial super-admin / institution setup)"""
    return proxy_request(current_app.config["AUTH_SERVICE_URL"], "/auth/register")


@auth_bp.get("/me")
@require_auth
def me():
    """GET /api/v1/auth/me"""
    return proxy_request(current_app.config["AUTH_SERVICE_URL"], "/auth/me")


@auth_bp.post("/change-password")
@require_auth
def change_password():
    """POST /api/v1/auth/change-password"""
    return proxy_request(current_app.config["AUTH_SERVICE_URL"], "/auth/change-password")
