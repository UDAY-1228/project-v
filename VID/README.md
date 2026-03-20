# VID Enterprise Management System

## Project Structure

```bash
VID/
├── core/               # Shared logic (Auth, DB, Base UI)
├── admin/              # Institution Admin module
├── super-admin/        # Super Admin module
├── workspaces/         # Domain-specific modules
│   ├── academic/
│   ├── academic-coordinator/
│   ├── admission-officer/
│   ├── common/
│   ├── team-owner/
│   ├── transport-coordinator/
│   ├── employee/
│   ├── hostel-admin/
│   ├── payment/
│   ├── examination/
│   ├── faculty/
│   └── student/
├── gateway/           # API Gateway (FastAPI)
├── server/            # Infrastructure (Docker, Nginx)
└── database/          # Database Schema Registry
```

## Tech Stack
- **Frontend**: React (TypeScript), TailwindCSS
- **Backend**: Python (FastAPI)
- **Database**: MongoDB

## Features
- **JWT Auth & RBAC**: Role-based access control out of the box.
- **Dynamic Workspaces**: Each workspace is a standalone FastAPI module.
- **Super Admin**: Create institutions and auto-generate credentials.
- **Admin**: Manage institution users (teachers, staff, students).
- **Responsive UI**: Premium TailwindCSS design for all screens.

## Quick Start
1. Run MongoDB.
2. Setup environment variables (MONGO_URL, SECRET_KEY, DB_NAME).
3. Run Gateway: `python -m gateway.main`.
4. Deploy with Docker: `docker-compose -f server/docker-compose.yml up -d`.
