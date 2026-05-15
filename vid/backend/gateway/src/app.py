"""
VID API Gateway – Flask Application Factory
"""
import logging
from flask import Flask, jsonify
from flask_cors import CORS

from .config.settings import get_config
from .middleware.auth_middleware import jwt
from .middleware.tenant_middleware import tenant_middleware
from .routes import register_routes


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)
    cfg = get_config()
    app.config.from_object(cfg)

    # ── Logging ───────────────────────────────────────────────────────────
    logging.basicConfig(level=cfg.LOG_LEVEL, format=cfg.LOG_FORMAT)
    logger = logging.getLogger(__name__)
    logger.info(f"Starting {cfg.APP_NAME} v{cfg.VERSION} [{cfg.LOG_LEVEL}]")

    # ── Extensions ────────────────────────────────────────────────────────
    CORS(app, origins=cfg.CORS_ORIGINS, supports_credentials=True)
    jwt.init_app(app)

    # ── Middleware ─────────────────────────────────────────────────────────
    app.before_request(tenant_middleware)

    # ── Routes ────────────────────────────────────────────────────────────
    # Root route for health check and visibility
    @app.route("/")
    def index():
        return {
            "message": "VID Multi-Tenant API Gateway is Running",
            "version": "1.0.0",
            "status": "online"
        }

    # Register all workspace routes
    register_routes(app)

    # ── Health Check ──────────────────────────────────────────────────────
    @app.get("/health")
    def health():
        return jsonify({"status": "ok", "service": cfg.APP_NAME, "version": cfg.VERSION})

    @app.get("/")
    def root():
        return jsonify({"message": "VID API Gateway", "version": cfg.VERSION, "docs": "/api/v1/docs"})

    # ── Error Handlers ─────────────────────────────────────────────────────
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Not Found", "message": str(e)}), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        return jsonify({"error": "Method Not Allowed", "message": str(e)}), 405

    @app.errorhandler(500)
    def internal_error(e):
        logger.error(f"Internal Server Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

    return app
