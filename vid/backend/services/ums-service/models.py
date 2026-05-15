"""
VID Auth Service – SQLAlchemy Models (Updated for Full RBAC & Multi-tenancy)
"""
import uuid
from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, String, Text, Table, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database import Base

# ── RBAC Pivot Table: Role <-> Permission ─────────────────────────────────────
role_permissions = Table(
    "role_permissions",
    Base.metadata,
    Column("role_id", UUID(as_uuid=True), ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True),
    Column("permission_id", UUID(as_uuid=True), ForeignKey("permissions.id", ondelete="CASCADE"), primary_key=True),
)


class Permission(Base):
    __tablename__ = "permissions"

    id          = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    resource    = Column(String(100), nullable=False)  # e.g. "students", "exams"
    action      = Column(String(50), nullable=False)   # e.g. "read", "write"
    description = Column(String(255), nullable=True)

    __table_args__ = (UniqueConstraint("resource", "action", name="uq_resource_action"),)


class Role(Base):
    __tablename__ = "roles"

    id             = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    institution_id = Column(UUID(as_uuid=True), ForeignKey("institutions.id", ondelete="CASCADE"), nullable=True, index=True)
    name           = Column(String(100), nullable=False)
    code           = Column(String(100), nullable=False)
    description    = Column(String(255), nullable=True)
    is_system      = Column(Boolean, default=False)
    created_at     = Column(DateTime, default=datetime.utcnow)

    permissions    = relationship("Permission", secondary=role_permissions)
    
    __table_args__ = (UniqueConstraint("institution_id", "code", name="uq_institution_role"),)


class UserRole(Base):
    __tablename__ = "user_roles"

    id             = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id        = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    role_id        = Column(UUID(as_uuid=True), ForeignKey("roles.id", ondelete="CASCADE"), nullable=False)
    institution_id = Column(UUID(as_uuid=True), ForeignKey("institutions.id", ondelete="CASCADE"), nullable=False)
    assigned_at    = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="user_roles")
    role = relationship("Role")

    __table_args__ = (UniqueConstraint("user_id", "role_id", name="uq_user_role"),)


class Workspace(Base):
    __tablename__ = "workspaces"

    id             = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    institution_id = Column(UUID(as_uuid=True), ForeignKey("institutions.id", ondelete="CASCADE"), nullable=False, index=True)
    name           = Column(String(100), nullable=False)
    code           = Column(String(100), nullable=False)
    description    = Column(String(255), nullable=True)
    is_active      = Column(Boolean, default=True)
    created_at     = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (UniqueConstraint("institution_id", "code", name="uq_institution_workspace"),)


class User(Base):
    __tablename__ = "users"

    id              = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    institution_id  = Column(UUID(as_uuid=True), ForeignKey("institutions.id", ondelete="CASCADE"), nullable=True, index=True)
    email           = Column(String(255), unique=True, nullable=False, index=True)
    password_hash   = Column(String(255), nullable=False)
    first_name      = Column(String(100), nullable=False)
    last_name       = Column(String(100), nullable=False)
    phone           = Column(String(20), nullable=True)
    avatar_url      = Column(Text, nullable=True)
    user_type       = Column(
        Enum("SUPER_ADMIN", "INSTITUTION_ADMIN", "FACULTY", "STUDENT", "STAFF", "PARENT", name="usertype"),
        default="STAFF",
        nullable=False,
    )
    is_active        = Column(Boolean, default=True, nullable=False)
    is_email_verified= Column(Boolean, default=False, nullable=False)
    last_login_at    = Column(DateTime, nullable=True)
    created_at       = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at       = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    sessions   = relationship("Session", back_populates="user", cascade="all, delete-orphan")
    user_roles = relationship("UserRole", back_populates="user", cascade="all, delete-orphan")


class Session(Base):
    __tablename__ = "sessions"

    id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id       = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    refresh_token = Column(String(500), unique=True, nullable=False)
    expires_at    = Column(DateTime, nullable=False)
    ip_address    = Column(String(50), nullable=True)
    user_agent    = Column(Text, nullable=True)
    created_at    = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="sessions")


class Institution(Base):
    __tablename__ = "institutions"

    id         = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name       = Column(String(255), nullable=False)
    code       = Column(String(50), unique=True, nullable=False)
    is_active  = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
