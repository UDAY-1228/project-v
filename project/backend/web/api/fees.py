"""
Fees API — Fee plans, invoices, payment gateway integration, waivers
"""
from datetime import datetime
from typing import Optional, List
from fastapi import APIRouter, HTTPException, Depends, Query
from ...shared.database import get_collection
from ...shared.models.schemas import FeeInvoice, FeePlan, FeeStatus
from ...shared.services.rbac_service import get_current_user

router = APIRouter()


@router.post("/plans", response_model=dict)
async def create_fee_plan(plan: FeePlan, current_user=Depends(get_current_user)):
    """Create a fee plan for a class/academic year"""
    plans = get_collection("fee_plans")
    doc = plan.dict()
    doc["created_at"] = datetime.utcnow()
    doc["created_by"] = current_user["id"]
    result = await plans.insert_one(doc)
    return {"message": "Fee plan created", "id": str(result.inserted_id)}


@router.get("/plans/{institution_id}")
async def get_fee_plans(institution_id: str, current_user=Depends(get_current_user)):
    """Get all fee plans for an institution"""
    plans = get_collection("fee_plans")
    docs = await plans.find({"institution_id": institution_id}).to_list(100)
    for d in docs:
        d["_id"] = str(d["_id"])
    return docs


@router.post("/invoice", response_model=dict)
async def create_invoice(invoice: FeeInvoice, current_user=Depends(get_current_user)):
    """Generate fee invoice for a student"""
    invoices = get_collection("fees_invoices")

    # Generate invoice number
    count = await invoices.count_documents({"institution_id": invoice.institution_id})
    invoice_number = f"INV-{invoice.institution_id[:4].upper()}-{datetime.now().year}-{count+1:04d}"

    doc = invoice.dict()
    doc["invoice_number"] = invoice_number
    doc["created_at"] = datetime.utcnow()

    result = await invoices.insert_one(doc)
    return {"message": "Invoice created", "invoice_number": invoice_number, "id": str(result.inserted_id)}


@router.get("/invoices/{student_id}")
async def get_student_invoices(student_id: str, current_user=Depends(get_current_user)):
    """Get all fee invoices for a student"""
    invoices = get_collection("fees_invoices")
    docs = await invoices.find({"student_id": student_id}).sort("created_at", -1).to_list(50)
    for d in docs:
        d["_id"] = str(d["_id"])
    return docs


@router.post("/pay/{invoice_id}")
async def process_payment(
    invoice_id: str,
    body: dict,
    current_user=Depends(get_current_user),
):
    """
    Process fee payment.
    body: {amount, payment_method: "upi|netbanking|card|cash", transaction_id}
    """
    invoices = get_collection("fees_invoices")
    from bson import ObjectId

    invoice = await invoices.find_one({"_id": ObjectId(invoice_id)})
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    new_paid = invoice.get("paid_amount", 0) + body.get("amount", 0)
    new_status = FeeStatus.PAID if new_paid >= invoice["total_amount"] else FeeStatus.PARTIAL

    await invoices.update_one(
        {"_id": ObjectId(invoice_id)},
        {"$set": {
            "paid_amount": new_paid,
            "status": new_status,
            "payment_date": datetime.utcnow(),
            "payment_method": body.get("payment_method"),
            "transaction_id": body.get("transaction_id"),
        }}
    )

    return {
        "message": "Payment recorded",
        "invoice_id": invoice_id,
        "status": new_status,
        "paid_amount": new_paid,
        "balance": max(0, invoice["total_amount"] - new_paid),
    }


@router.post("/waiver/{invoice_id}")
async def apply_waiver(
    invoice_id: str,
    body: dict,
    current_user=Depends(get_current_user),
):
    """Apply fee waiver with reason (scholarship, hardship)"""
    invoices = get_collection("fees_invoices")
    from bson import ObjectId

    await invoices.update_one(
        {"_id": ObjectId(invoice_id)},
        {"$set": {
            "status": FeeStatus.WAIVED,
            "waiver_reason": body.get("reason"),
            "waived_by": current_user["id"],
            "waived_at": datetime.utcnow(),
        }}
    )
    return {"message": "Waiver applied successfully"}


@router.get("/defaulters/{institution_id}")
async def get_fee_defaulters(
    institution_id: str,
    current_user=Depends(get_current_user),
):
    """Get list of students with overdue fees"""
    invoices = get_collection("fees_invoices")
    users = get_collection("users")

    overdue = await invoices.find({
        "institution_id": institution_id,
        "status": {"$in": ["overdue", "pending"]},
    }).to_list(200)

    result = []
    for inv in overdue:
        student = await users.find_one({"_id": inv["student_id"]})
        result.append({
            "student_name": student["full_name"] if student else "Unknown",
            "student_id": inv["student_id"],
            "invoice_number": inv["invoice_number"],
            "total_amount": inv["total_amount"],
            "paid_amount": inv.get("paid_amount", 0),
            "balance": inv["total_amount"] - inv.get("paid_amount", 0),
            "status": inv["status"],
        })

    return {"defaulters": result, "count": len(result)}


@router.get("/collection-summary/{institution_id}")
async def fee_collection_summary(institution_id: str, current_user=Depends(get_current_user)):
    """Fee collection analytics for the institution"""
    invoices = get_collection("fees_invoices")

    pipeline = [
        {"$match": {"institution_id": institution_id}},
        {"$group": {
            "_id": "$status",
            "count": {"$sum": 1},
            "total": {"$sum": "$total_amount"},
            "collected": {"$sum": "$paid_amount"},
        }}
    ]
    stats = await invoices.aggregate(pipeline).to_list(10)
    return {"collection_stats": stats}
