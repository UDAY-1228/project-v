"""
VID API Gateway – Route Registration
"""
from flask import Flask, current_app
from .auth_routes import auth_bp
from .institution_routes import institution_bp
from .student_routes import student_bp
from .faculty_routes import faculty_bp
from .academic_routes import academic_bp
from .attendance_routes import attendance_bp
from .examination_routes import examination_bp
from .payment_routes import payment_bp
from .timetable_routes import timetable_bp
from .notice_routes import notice_bp


def register_routes(app: Flask) -> None:
    """Register all API blueprints under /api/v1."""
    prefix = "/api/v1"

    app.register_blueprint(auth_bp,         url_prefix=f"{prefix}/auth")
    app.register_blueprint(institution_bp,  url_prefix=f"{prefix}/institutions")
    app.register_blueprint(student_bp,      url_prefix=f"{prefix}/students")
    app.register_blueprint(faculty_bp,      url_prefix=f"{prefix}/faculty")
    app.register_blueprint(academic_bp,     url_prefix=f"{prefix}/academic")
    app.register_blueprint(attendance_bp,   url_prefix=f"{prefix}/attendance")
    app.register_blueprint(examination_bp,  url_prefix=f"{prefix}/examinations")
    app.register_blueprint(payment_bp,      url_prefix=f"{prefix}/payments")
    app.register_blueprint(timetable_bp,    url_prefix=f"{prefix}/timetable")
    app.register_blueprint(notice_bp,       url_prefix=f"{prefix}/notices")
