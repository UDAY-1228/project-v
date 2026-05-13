"""VID Gateway – Payment / Fee Routes"""
from flask import Blueprint, current_app
from ..utils.proxy import proxy_request
from ..middleware.auth_middleware import require_auth, require_institution_admin, require_roles

payment_bp = Blueprint("payments", __name__)

# ── Fee Structure ─────────────────────────────────────────────────────────────

@payment_bp.get("/fees")
@require_auth
def list_fees():
    return proxy_request(current_app.config["PAYMENT_SERVICE_URL"], "/fees/")


@payment_bp.post("/fees")
@require_institution_admin
def create_fee():
    return proxy_request(current_app.config["PAYMENT_SERVICE_URL"], "/fees/")


@payment_bp.get("/fees/<fee_id>")
@require_auth
def get_fee(fee_id):
    return proxy_request(current_app.config["PAYMENT_SERVICE_URL"], f"/fees/{fee_id}")


@payment_bp.get("/fees/student/<student_id>")
@require_auth
def student_fees(student_id):
    return proxy_request(current_app.config["PAYMENT_SERVICE_URL"], f"/fees/student/{student_id}")

# ── Payments / Receipts ───────────────────────────────────────────────────────

@payment_bp.post("/collect")
@require_roles("SUPER_ADMIN", "INSTITUTION_ADMIN", "ACCOUNTANT")
def collect_payment():
    return proxy_request(current_app.config["PAYMENT_SERVICE_URL"], "/payments/collect")


@payment_bp.get("/receipts/<receipt_number>")
@require_auth
def get_receipt(receipt_number):
    return proxy_request(current_app.config["PAYMENT_SERVICE_URL"], f"/payments/receipts/{receipt_number}")


@payment_bp.get("/report")
@require_institution_admin
def payment_report():
    return proxy_request(current_app.config["PAYMENT_SERVICE_URL"], "/payments/report")
