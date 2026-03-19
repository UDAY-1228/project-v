# 🎓 EIMS — Educational Institution Management System

> AI-powered multi-tenant platform for schools & institutions (Hyderabad, India)

## Tech Stack
| Layer | Technology |
|---|---|
| Frontend | Angular 18 + TypeScript 5+, Angular Material, Bootstrap 5 |
| Backend | Python FastAPI + Uvicorn |
| Database | MongoDB (Motor async driver) |
| Cache/Sessions | Redis |
| AI/ML | TensorFlow, OpenCV, scikit-learn, PyTorch |
| Realtime | WebSockets (FastAPI) |
| Auth | JWT + RBAC |
| Containerization | Docker + Docker Compose |
| Reverse Proxy | Nginx |

## Roles
- **Super Admin** — Platform-wide management
- **Institution Admin** — Institution-specific operations
- **Faculty/Teacher** — Classroom & teaching tools
- **Ed Officials** — Oversight & compliance
- **Students** — Learning, attendance, fees
- **Parents** — Child monitoring, PTM, payments

## Quick Start

```bash
# Clone and navigate
cd eims-platform

# Start all services
docker-compose -f server/docker-compose.yml up --build

# Services:
# Frontend (Angular)  → http://localhost:4200
# Backend (FastAPI)   → http://localhost:8000
# API Docs (Swagger)  → http://localhost:8000/docs
# MongoDB             → localhost:27017
# Redis               → localhost:6379
```

## Development

```bash
# Frontend only
cd frontend && npm install && npm start

# Backend only
cd backend && pip install -r requirements.txt && uvicorn main:app --reload --port 8000
```

## Project Structure
```
eims-platform/
├── frontend/           # Angular 18 app (ALL roles)
│   ├── web/            # Super Admin, Institution Admin, Faculty, Ed Officials
│   └── app/            # Student & Parent mobile-first app
├── backend/            # FastAPI Python backend
│   ├── api/            # REST endpoints
│   ├── ml/             # AI/ML models
│   ├── models/         # Pydantic schemas
│   └── services/       # Business logic
├── database/           # MongoDB init scripts
├── server/             # Docker Compose + Nginx config
└── docs/               # Feature matrices & API docs
```

## Features
- 🤖 AI Face Recognition (enrollment + attendance)
- 📱 QR Code Virtual ID generation
- 📊 Predictive analytics (at-risk students)
- 📅 AI Timetable conflict resolver
- 💬 Real-time WebSocket chat
- 📚 LMS with AI homework helper
- 💳 Fee management & payment gateway
- 🔔 Push notifications (PWA)
- 🌐 Telugu + English language support
- 📴 Offline kiosk attendance mode

## API Documentation
After starting, visit: http://localhost:8000/docs

## Tests
```bash
cd backend && pytest tests/ --cov=. --cov-report=html
```
Target: 80%+ coverage
