"""
VID API Gateway – Tenant Middleware
Resolves institution_id from JWT or request header and injects into Flask `g`.
"""
import logging
from flask import g, request, jsonify
from flask_jwt_extended import decode_token, verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError

logger = logging.getLogger(__name__)

# Routes that don't need tenant resolution
PUBLIC_ROUTES = {
    "/health",
    "/",
    "/api/v1/auth/login",
    "/api/v1/auth/refresh",
    "/api/v1/auth/register",
    "/api/v1/institutions/register",
}


def tenant_middleware():
    """
    Before-request hook: extracts institution_id from JWT claims or
    X-Institution-ID header and stores in flask.g for downstream use.
    """
    if request.path in PUBLIC_ROUTES or request.method == "OPTIONS":
        return

    # Try to get institution_id from JWT if token is present
    auth_header = request.headers.get("Authorization", "")
    if auth_header.startswith("Bearer "):
        try:
            token = auth_header.split(" ")[1]
            decoded = decode_token(token)
            g.institution_id = decoded.get("sub_claims", {}).get(
                "institution_id"
            ) or decoded.get("institution_id")
        except Exception as exc:
            logger.debug(f"Tenant middleware – could not decode token: {exc}")
            g.institution_id = None
    else:
        g.institution_id = None

    # Allow override via header (for super-admin acting on behalf of tenant)
    header_tenant = request.headers.get("X-Institution-ID")
    if header_tenant:
        g.institution_id = header_tenant

    logger.debug(f"Tenant resolved: institution_id={g.institution_id} path={request.path}")
