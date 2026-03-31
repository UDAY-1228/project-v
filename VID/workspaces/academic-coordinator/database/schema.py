"""
Academic Coordinator - MongoDB Schema Validation
==================================================
JSON Schema validators for MongoDB collections.
Applied at the database level for data integrity.
"""

SCHEMAS = {
    "ac_academic_years": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["year_name", "start_date", "end_date", "status"],
            "properties": {
                "year_name": {"bsonType": "string", "description": "Academic year label e.g. 2025-2026"},
                "start_date": {"bsonType": "date"},
                "end_date": {"bsonType": "date"},
                "status": {"enum": ["active", "inactive", "archived"]},
                "institution_id": {"bsonType": "string"},
                "created_at": {"bsonType": "date"},
                "updated_at": {"bsonType": "date"},
            },
        }
    },
    "ac_semesters": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["semester_name", "academic_year_id", "start_date", "end_date"],
            "properties": {
                "semester_name": {"bsonType": "string"},
                "academic_year_id": {"bsonType": "string"},
                "start_date": {"bsonType": "date"},
                "end_date": {"bsonType": "date"},
                "status": {"enum": ["active", "inactive", "archived"]},
                "created_at": {"bsonType": "date"},
                "updated_at": {"bsonType": "date"},
            },
        }
    },
    "ac_departments": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["department_name", "department_code"],
            "properties": {
                "department_name": {"bsonType": "string"},
                "department_code": {"bsonType": "string"},
                "hod_name": {"bsonType": "string"},
                "hod_email": {"bsonType": "string"},
                "status": {"enum": ["active", "inactive"]},
                "total_faculty": {"bsonType": "int"},
                "total_students": {"bsonType": "int"},
                "created_at": {"bsonType": "date"},
                "updated_at": {"bsonType": "date"},
            },
        }
    },
    "ac_courses": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["course_name", "course_code", "department_id"],
            "properties": {
                "course_name": {"bsonType": "string"},
                "course_code": {"bsonType": "string"},
                "department_id": {"bsonType": "string"},
                "duration_years": {"bsonType": "int"},
                "total_credits": {"bsonType": "int"},
                "degree_type": {"enum": ["UG", "PG", "PhD", "Diploma"]},
                "description": {"bsonType": "string"},
                "status": {"enum": ["active", "inactive", "draft", "archived"]},
                "created_at": {"bsonType": "date"},
                "updated_at": {"bsonType": "date"},
            },
        }
    },
    "ac_subjects": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["subject_name", "subject_code", "course_id", "semester_id"],
            "properties": {
                "subject_name": {"bsonType": "string"},
                "subject_code": {"bsonType": "string"},
                "course_id": {"bsonType": "string"},
                "semester_id": {"bsonType": "string"},
                "credits": {"bsonType": "int"},
                "subject_type": {"enum": ["theory", "lab", "elective", "project"]},
                "faculty_id": {"bsonType": "string"},
                "faculty_name": {"bsonType": "string"},
                "max_students": {"bsonType": "int"},
                "status": {"enum": ["active", "inactive", "draft"]},
                "created_at": {"bsonType": "date"},
                "updated_at": {"bsonType": "date"},
            },
        }
    },
    "ac_timetables": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["timetable_name", "course_id", "semester_id", "academic_year_id"],
            "properties": {
                "timetable_name": {"bsonType": "string"},
                "course_id": {"bsonType": "string"},
                "semester_id": {"bsonType": "string"},
                "academic_year_id": {"bsonType": "string"},
                "section": {"bsonType": "string"},
                "slots": {"bsonType": "array"},
                "status": {"enum": ["active", "inactive", "draft"]},
                "created_at": {"bsonType": "date"},
                "updated_at": {"bsonType": "date"},
            },
        }
    },
    "ac_assessments": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["assessment_name", "subject_id", "course_id", "semester_id"],
            "properties": {
                "assessment_name": {"bsonType": "string"},
                "assessment_type": {"enum": ["internal", "external", "assignment", "quiz", "project", "viva"]},
                "subject_id": {"bsonType": "string"},
                "course_id": {"bsonType": "string"},
                "semester_id": {"bsonType": "string"},
                "total_marks": {"bsonType": "double"},
                "passing_marks": {"bsonType": "double"},
                "date": {"bsonType": "date"},
                "duration_minutes": {"bsonType": "int"},
                "status": {"enum": ["draft", "active", "completed", "archived"]},
                "created_at": {"bsonType": "date"},
                "updated_at": {"bsonType": "date"},
            },
        }
    },
    "ac_assessment_results": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["assessment_id", "student_id", "marks_obtained"],
            "properties": {
                "assessment_id": {"bsonType": "string"},
                "student_id": {"bsonType": "string"},
                "student_name": {"bsonType": "string"},
                "marks_obtained": {"bsonType": "double"},
                "grade": {"bsonType": "string"},
                "remarks": {"bsonType": "string"},
                "submitted_at": {"bsonType": "date"},
            },
        }
    },
    "ac_reports": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["report_name", "report_type"],
            "properties": {
                "report_name": {"bsonType": "string"},
                "report_type": {"enum": ["academic", "attendance", "performance", "course-wise", "department-wise"]},
                "department_id": {"bsonType": "string"},
                "course_id": {"bsonType": "string"},
                "status": {"enum": ["pending", "completed", "archived"]},
                "file_url": {"bsonType": "string"},
                "created_at": {"bsonType": "date"},
                "updated_at": {"bsonType": "date"},
            },
        }
    },
    "ac_notices": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["title", "content"],
            "properties": {
                "title": {"bsonType": "string"},
                "content": {"bsonType": "string"},
                "category": {"enum": ["general", "academic", "exam", "event", "urgent"]},
                "priority": {"enum": ["low", "normal", "high", "urgent"]},
                "target_audience": {"bsonType": "array"},
                "is_pinned": {"bsonType": "bool"},
                "views_count": {"bsonType": "int"},
                "status": {"enum": ["active", "inactive", "archived"]},
                "created_at": {"bsonType": "date"},
                "updated_at": {"bsonType": "date"},
            },
        }
    },
    "ac_settings": {
        "$jsonSchema": {
            "bsonType": "object",
            "properties": {
                "grading_system": {"enum": ["absolute", "relative", "cgpa"]},
                "max_credits_per_semester": {"bsonType": "int"},
                "min_attendance_percentage": {"bsonType": "double"},
                "pass_percentage": {"bsonType": "double"},
                "allow_course_registration": {"bsonType": "bool"},
                "institution_id": {"bsonType": "string"},
                "created_at": {"bsonType": "date"},
                "updated_at": {"bsonType": "date"},
            },
        }
    },
}


async def apply_schemas(db):
    """Apply JSON Schema validation to all collections."""
    for collection_name, validator in SCHEMAS.items():
        try:
            await db.command({
                "collMod": collection_name,
                "validator": validator,
                "validationLevel": "moderate",
                "validationAction": "warn",
            })
            print(f"  ✓ Schema applied: {collection_name}")
        except Exception as e:
            # Collection may not exist yet — create it with validator
            try:
                await db.create_collection(collection_name, validator=validator)
                print(f"  ✓ Collection created with schema: {collection_name}")
            except Exception as inner:
                print(f"  ✗ Schema error for {collection_name}: {inner}")

    print(f"✅ Academic Coordinator: {len(SCHEMAS)} schemas applied")
