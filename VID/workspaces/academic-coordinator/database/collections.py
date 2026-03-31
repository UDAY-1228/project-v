"""
Academic Coordinator - MongoDB Collections Definition
======================================================
Defines all collections, indexes, and initialization logic
for the Academic Coordinator workspace.
"""

COLLECTION_PREFIX = "ac_"

# All collections used by the Academic Coordinator workspace
COLLECTIONS = {
    "academic_years": {
        "name": f"{COLLECTION_PREFIX}academic_years",
        "indexes": [
            {"keys": [("year_name", 1)], "unique": True},
            {"keys": [("status", 1)]},
        ],
    },
    "semesters": {
        "name": f"{COLLECTION_PREFIX}semesters",
        "indexes": [
            {"keys": [("academic_year_id", 1)]},
            {"keys": [("status", 1)]},
        ],
    },
    "departments": {
        "name": f"{COLLECTION_PREFIX}departments",
        "indexes": [
            {"keys": [("department_code", 1)], "unique": True},
            {"keys": [("department_name", 1)]},
        ],
    },
    "courses": {
        "name": f"{COLLECTION_PREFIX}courses",
        "indexes": [
            {"keys": [("course_code", 1)], "unique": True},
            {"keys": [("department_id", 1)]},
            {"keys": [("status", 1)]},
        ],
    },
    "subjects": {
        "name": f"{COLLECTION_PREFIX}subjects",
        "indexes": [
            {"keys": [("subject_code", 1)], "unique": True},
            {"keys": [("course_id", 1), ("semester_id", 1)]},
            {"keys": [("faculty_id", 1)]},
        ],
    },
    "timetables": {
        "name": f"{COLLECTION_PREFIX}timetables",
        "indexes": [
            {"keys": [("course_id", 1), ("semester_id", 1), ("section", 1)]},
            {"keys": [("status", 1)]},
        ],
    },
    "assessments": {
        "name": f"{COLLECTION_PREFIX}assessments",
        "indexes": [
            {"keys": [("subject_id", 1)]},
            {"keys": [("assessment_type", 1)]},
            {"keys": [("date", -1)]},
        ],
    },
    "assessment_results": {
        "name": f"{COLLECTION_PREFIX}assessment_results",
        "indexes": [
            {"keys": [("assessment_id", 1)]},
            {"keys": [("student_id", 1)]},
            {"keys": [("assessment_id", 1), ("student_id", 1)], "unique": True},
        ],
    },
    "reports": {
        "name": f"{COLLECTION_PREFIX}reports",
        "indexes": [
            {"keys": [("report_type", 1)]},
            {"keys": [("created_at", -1)]},
        ],
    },
    "notices": {
        "name": f"{COLLECTION_PREFIX}notices",
        "indexes": [
            {"keys": [("category", 1)]},
            {"keys": [("is_pinned", -1), ("created_at", -1)]},
            {"keys": [("status", 1)]},
        ],
    },
    "settings": {
        "name": f"{COLLECTION_PREFIX}settings",
        "indexes": [
            {"keys": [("institution_id", 1)], "unique": True},
        ],
    },
    "activity_log": {
        "name": f"{COLLECTION_PREFIX}activity_log",
        "indexes": [
            {"keys": [("timestamp", -1)]},
            {"keys": [("module", 1)]},
        ],
    },
}


async def initialize_collections(db):
    """
    Create all collections and their indexes in MongoDB.
    Called on application startup.
    """
    for key, config in COLLECTIONS.items():
        collection_name = config["name"]
        # Ensure collection exists
        existing = await db.list_collection_names()
        if collection_name not in existing:
            await db.create_collection(collection_name)

        col = db[collection_name]
        # Create indexes
        for idx in config.get("indexes", []):
            kwargs = {}
            if idx.get("unique"):
                kwargs["unique"] = True
            await col.create_index(idx["keys"], **kwargs)

    print(f"✅ Academic Coordinator: {len(COLLECTIONS)} collections initialized")
