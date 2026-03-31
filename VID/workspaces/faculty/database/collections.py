"""
Faculty Database Collections
===========================
Collection name constants and metadata for Faculty workspace.
"""

COLLECTION_NAMES = {
    "PROFILES": "profiles",
    "CLASSES": "classes",
    "ATTENDANCE": "attendance",
    "ASSIGNMENTS": "assignments",
    "ASSIGNMENT_SUBMISSIONS": "assignment_submissions",
    "EXAMS": "exams",
    "EXAM_RESULTS": "exam_results",
    "REPORTS": "reports",
    "SETTINGS": "settings",
    "ACTIVITY_LOG": "activity_log",
    "STUDENTS": "students",
}

COLLECTION_PREFIX = "fac_"

def get_collection_name(name: str) -> str:
    """Get prefixed collection name."""
    return f"{COLLECTION_PREFIX}{name}"

def get_all_collections() -> dict:
    """Get all collection names with prefix."""
    return {key: get_collection_name(value) for key, value in COLLECTION_NAMES.items()}
