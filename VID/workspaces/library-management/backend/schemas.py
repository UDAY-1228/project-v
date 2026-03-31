"""
Library Management - MongoDB Schemas
=====================================
MongoDB collection schemas and indexes for the Library Management workspace.
"""

from pymongo import ASCENDING, DESCENDING

COLLECTIONS = {
    "catalog": [
        ({"accession_number": ASCENDING}, {"unique": True}),
        ({"isbn": ASCENDING}, {"unique": True}),
        ({"title": ASCENDING}, {}),
        ({"author": ASCENDING}, {}),
        ({"category": ASCENDING}, {}),
        ({"status": ASCENDING}, {}),
    ],
    "issues": [
        ({"book_id": ASCENDING}, {}),
        ({"member_id": ASCENDING}, {}),
        ({"issue_date": DESCENDING}, {}),
        ({"due_date": ASCENDING}, {}),
        ({"status": ASCENDING}, {}),
    ],
    "members": [
        ({"member_id": ASCENDING}, {"unique": True}),
        ({"email": ASCENDING}, {"unique": True}),
        ({"member_type": ASCENDING}, {}),
        ({"status": ASCENDING}, {}),
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
