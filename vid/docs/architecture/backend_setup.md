# VID – Backend & Database Setup

The VID (Virtual Identification System) backend is built on a **Microservices Architecture** with a **Flask API Gateway** and multiple **FastAPI** microservices, all powered by a multi-tenant **PostgreSQL** database.

## 🏗 Architecture Overview

- **Database (PostgreSQL)**: Single database cluster with logical isolation using `institution_id`.
- **Multi-tenancy with Workspaces**: 
  - Each institution (tenant) has its own independent configuration.
  - Features are grouped into **Workspaces** (Academics, Admission, Finance, etc.).
  - Users are granted access to specific workspaces via **RBAC**.
- **API Gateway (Flask)**:
  - Central entry point for all frontend requests.
  - Handles **Authentication (JWT)** and **Tenant Resolution**.
  - Injects `X-Institution-ID` and `X-User-ID` into downstream headers.
  - Enforces **Workspace-level RBAC** using custom decorators.
- **Microservices (FastAPI)**:
  - **UMS Service**: Manages complex RBAC (Roles, Permissions, UserRoles).
  - **Business Services**: Stateless services that filter data by the provided `institution_id`.

## 📁 Directory Structure

```text
backend/
├── database/
│   └── postgres/
│       └── prisma/
│           └── schema.prisma  # Master Database Schema
├── gateway/                   # Flask API Gateway
│   ├── src/
│   │   ├── middleware/        # Auth & Tenant Logic
│   │   ├── routes/            # Proxy Route Definitions
│   │   └── utils/             # Request Proxying
│   └── main.py
└── services/
    └── ums-service/           # FastAPI Auth Microservice
        ├── routers.py         # Auth API Endpoints
        ├── models.py          # SQLAlchemy Models
        └── main.py
```

## 🚀 Getting Started

### 1. Prerequisites
- Docker & Docker Compose
- Python 3.11+
- Node.js (for Prisma CLI)

### 2. Environment Setup
Copy the example environment file:
```bash
cp .env.example .env
```

### 3. Running with Docker
The easiest way to start the entire stack:
```bash
docker-compose -f docker/docker-compose.dev.yml up --build
```

### 4. Running Without Docker (Manual Setup)
To run the application natively on your machine:

1. **Database**: Ensure PostgreSQL is running and `vid_db` is created.
2. **Launch Script**: Run the provided PowerShell script:
   ```powershell
   .\start_backend.ps1
   ```
3. **Manual Steps**:
   - Create venvs in `backend/gateway` and `backend/services/ums-service`.
   - Install `requirements.txt` in each.
   - Set the `DATABASE_URL` and `JWT_SECRET_KEY` env vars.
   - Start Gateway: `python main.py`
   - Start Auth Service: `uvicorn main:app --port 8001`

### 5. Database Migrations
To initialize the database schema:
```bash
# Install Prisma
npm install prisma --save-dev

# Generate Client & Push Schema
npx prisma generate --schema=backend/database/postgres/prisma/schema.prisma
npx prisma db push --schema=backend/database/postgres/prisma/schema.prisma
```

## 🔐 Authentication Flow

1. User sends credentials to `/api/v1/auth/login`.
2. Gateway proxies to **Auth Service**.
3. Auth Service validates and returns **JWT** containing `user_id` and `institution_id`.
4. Subsequent requests include `Authorization: Bearer <token>`.
5. Gateway's `tenant_middleware` extracts `institution_id` and injects it into headers for downstream services.

## 🛠 Workspace & RBAC Strategy

1. **Role Definition**: Roles (e.g., `Principal`, `Faculty`) are defined per tenant or globally.
2. **Permission Mapping**: Permissions are tied to resources and actions (e.g., `students:read`, `exams:write`).
3. **Workspace Access**: 
   - The Gateway checks if a user's role grants them access to the requested workspace route.
   - Example: The `/api/v1/students` route requires a role assigned to the `Student Management` workspace.
4. **Data Isolation**: All microservice queries are appended with `WHERE institution_id = :id` to ensure total tenant data isolation.

## 🛠 Next Steps
- [ ] Implement **Permission-based checks** (not just role-name) in the Gateway.
- [ ] Add **Workspace Activation** logic (enable/disable modules per institution).
- [ ] Set up **Redis** for rate limiting and session caching.
