"""
QR Code & Virtual ID Generator Utilities
"""
import qrcode
import uuid
import hashlib
from datetime import datetime
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageDraw, ImageFont


def generate_qr_code(data: str, output_path: str, size: int = 10) -> str:
    """Generate QR code PNG file"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_H,
        box_size=size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="#1a1a2e", back_color="white")
    img.save(output_path)
    return output_path


def generate_virtual_id_number(institution_code: str, role: str, user_id: str) -> str:
    """
    Generate unique virtual ID:
    Format: EIMS-{INST_CODE}-{ROLE_PREFIX}-{YEAR}-{HASH}
    Example: EIMS-DPS-STU-2024-A1B2C3
    """
    role_prefix = {
        "student": "STU",
        "faculty": "FAC",
        "institution_admin": "ADM",
        "parent": "PAR",
        "ed_official": "EDO",
        "super_admin": "SUP",
    }.get(role.lower(), "USR")

    year = datetime.now().year
    hash_part = hashlib.md5(f"{institution_code}{user_id}{role}".encode()).hexdigest()[:6].upper()

    return f"EIMS-{institution_code.upper()[:4]}-{role_prefix}-{year}-{hash_part}"


def generate_id_card_data(user: dict, institution: dict, virtual_id: str, qr_path: str) -> dict:
    """Prepare data for ID card PDF generation"""
    return {
        "name": user.get("full_name"),
        "role": user.get("role"),
        "virtual_id": virtual_id,
        "institution_name": institution.get("name"),
        "institution_code": institution.get("code"),
        "valid_until": f"{datetime.now().year + 1}-03-31",
        "photo_url": user.get("profile_photo"),
        "qr_path": qr_path,
        "blood_group": user.get("blood_group", "N/A"),
        "emergency_contact": user.get("phone"),
    }
