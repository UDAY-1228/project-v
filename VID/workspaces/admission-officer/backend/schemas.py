"""
Admission Officer - MongoDB Schemas
====================================
MongoDB collection schemas and indexes for the Admission Officer workspace.
"""

from pymongo import ASCENDING, DESCENDING

COLLECTIONS = {
    "applications": [
        ({"application_number": ASCENDING}, {"unique": True}),
        ({"status": ASCENDING}, {}),
        ({"submitted_at": DESCENDING}, {}),
        ({"email": ASCENDING}, {}),
    ],
    "admissions": [
        ({"admission_number": ASCENDING}, {"unique": True}),
        ({"course": ASCENDING}, {}),
        ({"batch": ASCENDING}, {}),
        ({"status": ASCENDING}, {}),
    ],
    "documents": [
        ({"application_id": ASCENDING}, {}),
        ({"status": ASCENDING}, {}),
        ({"verified_by": ASCENDING}, {}),
    ],
    "fees": [
        ({"student_id": ASCENDING}, {}),
        ({"payment_status": ASCENDING}, {}),
        ({"due_date": ASCENDING}, {}),
    ],
    "reports": [
        ({"report_type": ASCENDING}, {}),
        ({"generated_at": DESCENDING}, {}),
    ],
    "settings": [],
    "activity_log": [
        ({"timestamp": DESCENDING}, {}),
    ],
}
