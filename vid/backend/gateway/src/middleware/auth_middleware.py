"""
VID API Gateway – JWT Auth Middleware
"""
import logging
from functools import wraps
from flask import g, jsonify, request
from flask_jwt_extended import (
    JWTManager,
    get_jwt,
    get_jwt_identity,
    verify_jwt_in_request,
)

logger = logging.getLogger(__name__)
jwt = JWTManager()


# ─────────────────────────────────────────────────────────────────────────────
# JWT Error Handlers
# ─────────────────────────────────────────────────────────────────────────────

@jwt.unauthorized_loader
def missing_token(reason):
    return jsonify({"error": "Unauthorized", "message": reason}), 401


@jwt.invalid_token_loader
def invalid_token(reason):
    return jsonify({"error": "Invalid Token", "message": reason}), 422


@jwt.expired_token_loader
def expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token Expired", "message": "Access token has expired"}), 401


@jwt.revoked_token_loader
def revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token Revoked", "message": "Token has been revoked"}), 401


# ─────────────────────────────────────────────────────────────────────────────
# Role-Based Access Decorators
# ─────────────────────────────────────────────────────────────────────────────

def require_auth(f):
    """Require a valid JWT access token."""
    @wraps(f)
    def decorated(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        g.current_user_id   = get_jwt_identity()
        g.institution_id    = claims.get("institution_id")
        g.user_type         = claims.get("user_type")
        g.roles             = claims.get("roles", [])
        return f(*args, **kwargs)
    return decorated


def require_roles(*allowed_roles):
    """Require the user to have at least one of the allowed roles."""
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            g.current_user_id   = get_jwt_identity()
            g.institution_id    = claims.get("institution_id")
            g.user_type         = claims.get("user_type")
            g.roles             = claims.get("roles", [])

            user_roles = set(g.roles + [g.user_type])
            if not user_roles.intersection(set(allowed_roles)):
                return jsonify({
                    "error":   "Forbidden",
                    "message": f"Required roles: {allowed_roles}",
                }), 403
            return f(*args, **kwargs)
        return decorated
    return decorator


def require_super_admin(f):
    return require_roles("SUPER_ADMIN")(f)


def require_institution_admin(f):
    return require_roles("SUPER_ADMIN", "INSTITUTION_ADMIN")(f)
