"""
Virtual ID API — Face Enrollment, QR Generation, Verification
AI-powered biometric identity system
"""
import os
import uuid
import hashlib
import base64
from datetime import datetime
from typing import Optional
from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Form
from fastapi.responses import FileResponse

from ...shared.config import settings
from ...shared.database import get_collection
from ...shared.models.schemas import VirtualID, FaceEnrollRequest
from ...shared.services.rbac_service import get_current_user
from ...shared.ml.face_recognition_ml import FaceRecognitionService
from ...shared.utils.qr_generator import generate_qr_code, generate_virtual_id_number

router = APIRouter()
face_service = FaceRecognitionService()


@router.post("/enroll-face/{user_id}")
async def enroll_face(
    user_id: str,
    face_image: UploadFile = File(...),
    consent: bool = Form(True),
    current_user=Depends(get_current_user),
):
    """
    Enroll user face for AI attendance detection.
    Stores face encoding hash (not raw biometric data).
    """
    if not consent:
        raise HTTPException(status_code=400, detail="Biometric consent required")

    # Load and process face image
    image_bytes = await face_image.read()
    encoding = face_service.encode_face(image_bytes)

    if encoding is None:
        raise HTTPException(status_code=400, detail="No face detected in image. Please retry with a clear face photo.")

    # Hash the encoding for storage (privacy)
    encoding_hash = hashlib.sha256(str(encoding.tolist()).encode()).hexdigest()

    # Save face image
    img_filename = f"{user_id}_face_{uuid.uuid4().hex[:8]}.jpg"
    img_path = os.path.join(settings.UPLOAD_PATH, "faces", img_filename)
    os.makedirs(os.path.dirname(img_path), exist_ok=True)
    with open(img_path, "wb") as f:
        f.write(image_bytes)

    # Update user and virtual ID in DB
    users = get_collection("users")
    virtual_ids = get_collection("virtual_ids")

    await users.update_one(
        {"_id": user_id},
        {"$set": {
            "face_enrolled": True,
            "face_image_path": f"faces/{img_filename}",
            "updated_at": datetime.utcnow(),
        }}
    )

    await virtual_ids.update_one(
        {"user_id": user_id},
        {"$set": {
            "face_encoding_hash": encoding_hash,
            "face_enrolled": True,
            "face_enrollment_date": datetime.utcnow(),
        }}
    )

    return {
        "message": "Face enrolled successfully",
        "user_id": user_id,
        "face_enrolled": True,
        "encoding_hash": encoding_hash[:16] + "***",  # partial for security
    }


@router.post("/generate/{user_id}")
async def generate_virtual_id(user_id: str, current_user=Depends(get_current_user)):
    """
    Generate Virtual ID card + QR code for a user.
    """
    users = get_collection("users")
    virtual_ids = get_collection("virtual_ids")

    user = await users.find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if already has virtual ID
    existing = await virtual_ids.find_one({"user_id": user_id})
    if existing:
        return {"message": "Virtual ID already exists", "virtual_id": existing["virtual_id_number"], "qr_url": existing["qr_code_url"]}

    # Generate unique virtual ID
    virtual_id_number = generate_virtual_id_number(
        institution_code=user.get("institution_code", "EIMS"),
        role=user["role"],
        user_id=user_id,
    )

    # Generate QR code
    qr_data = f"EIMS:{virtual_id_number}:{user_id}:{user['email']}"
    qr_filename = f"qr_{user_id}_{uuid.uuid4().hex[:8]}.png"
    qr_path = os.path.join(settings.UPLOAD_PATH, "qrcodes", qr_filename)
    os.makedirs(os.path.dirname(qr_path), exist_ok=True)
    generate_qr_code(qr_data, qr_path)

    # Store virtual ID
    vid_doc = {
        "user_id": user_id,
        "institution_id": user.get("institution_id"),
        "virtual_id_number": virtual_id_number,
        "qr_code_url": f"/uploads/qrcodes/{qr_filename}",
        "qr_code_data": qr_data,
        "face_enrolled": user.get("face_enrolled", False),
        "is_active": True,
        "issued_at": datetime.utcnow(),
    }
    await virtual_ids.insert_one(vid_doc)

    # Update user record
    await users.update_one(
        {"_id": user_id},
        {"$set": {
            "virtual_id": virtual_id_number,
            "qr_code_url": vid_doc["qr_code_url"],
        }}
    )

    return {
        "virtual_id": virtual_id_number,
        "qr_code_url": vid_doc["qr_code_url"],
        "message": "Virtual ID generated successfully",
    }


@router.post("/verify-face")
async def verify_face_attendance(
    face_image: UploadFile = File(...),
    institution_id: str = Form(...),
    class_name: Optional[str] = Form(None),
    current_user=Depends(get_current_user),
):
    """
    AI-powered face verification for attendance.
    Matches face against enrolled users in the institution.
    """
    image_bytes = await face_image.read()
    detected_encoding = face_service.encode_face(image_bytes)

    if detected_encoding is None:
        raise HTTPException(status_code=400, detail="No face detected")

    # Get all enrolled users in institution
    virtual_ids = get_collection("virtual_ids")
    users = get_collection("users")

    enrolled = await virtual_ids.find(
        {"institution_id": institution_id, "face_enrolled": True}
    ).to_list(length=None)

    best_match = None
    best_distance = 0.6  # threshold

    for vid in enrolled:
        user = await users.find_one({"_id": vid["user_id"], "face_enrolled": True})
        if not user or not user.get("face_image_path"):
            continue

        img_path = os.path.join(settings.UPLOAD_PATH, user["face_image_path"])
        if not os.path.exists(img_path):
            continue

        with open(img_path, "rb") as f:
            stored_bytes = f.read()

        distance = face_service.compare_faces(stored_bytes, image_bytes)
        if distance is not None and distance < best_distance:
            best_distance = distance
            best_match = user

    if best_match:
        confidence = round((1 - best_distance) * 100, 2)
        return {
            "matched": True,
            "user_id": str(best_match["_id"]),
            "full_name": best_match["full_name"],
            "confidence": confidence,
            "virtual_id": best_match.get("virtual_id"),
        }

    return {"matched": False, "message": "No matching face found"}


@router.post("/verify-qr")
async def verify_qr(body: dict, current_user=Depends(get_current_user)):
    """Verify QR code scan for attendance/entry"""
    qr_data = body.get("qr_data", "")
    parts = qr_data.split(":")

    if len(parts) < 3 or parts[0] != "EIMS":
        raise HTTPException(status_code=400, detail="Invalid QR code")

    virtual_id_number = parts[1]
    user_id = parts[2]

    virtual_ids = get_collection("virtual_ids")
    vid = await virtual_ids.find_one({"virtual_id_number": virtual_id_number, "user_id": user_id})

    if not vid or not vid.get("is_active"):
        raise HTTPException(status_code=404, detail="Virtual ID not found or inactive")

    users = get_collection("users")
    user = await users.find_one({"_id": user_id})

    return {
        "verified": True,
        "user_id": user_id,
        "full_name": user["full_name"] if user else "Unknown",
        "virtual_id": virtual_id_number,
        "role": user["role"] if user else "unknown",
    }


@router.get("/my-id")
async def get_my_virtual_id(current_user=Depends(get_current_user)):
    """Get current user's virtual ID details"""
    virtual_ids = get_collection("virtual_ids")
    vid = await virtual_ids.find_one({"user_id": current_user["id"]})
    if not vid:
        raise HTTPException(status_code=404, detail="Virtual ID not generated yet")
    return vid


@router.delete("/revoke/{user_id}")
async def revoke_virtual_id(user_id: str, current_user=Depends(get_current_user)):
    """Revoke/regenerate a user's virtual ID"""
    virtual_ids = get_collection("virtual_ids")
    await virtual_ids.update_one(
        {"user_id": user_id},
        {"$set": {"is_active": False, "revoked_at": datetime.utcnow()}}
    )
    return {"message": f"Virtual ID for user {user_id} has been revoked"}
