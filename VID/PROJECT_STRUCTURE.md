# VID Project Structure & Architecture Guide

Welcome to the **VID Management System**. This document provides a comprehensive overview of the project's folder structure, files, and core architectural concepts. It is designed to help new and existing developers quickly understand and navigate the codebase.

## 1. High-Level Architecture

VID is a modular, monolithic application built with:
- **Frontend**: React (TypeScript) with Vite and Tailwind CSS.
- **Backend**: FastAPI (Python) for modular API routes and business logic.
- **Database**: Centralized JSON-based storage for temporary data & fast iteration (via `core/backend/database/`).
- **Micro-apps (Workspaces)**: The app is divided into distinct "workspaces" (feature modules) based on user roles (e.g., Student, Admin, Transport Coordinator).

## 2. Full Directory Tree

Below is the complete tree of the main application structure, excluding standard ignore folders like `node_modules` or `__pycache__`:

```text
project-v/VID/
├── README.md
├── __init__.py
├── admin
│   ├── backend/
│   │   ├── api/routes.py
│   │   ├── models/
│   │   └── services/
│   └── frontend/
│       └── pages/ (CreateUser, Dashboard, ManageUsers)
├── core/
│   ├── backend/
│   │   ├── api/ (notice_routes.py, timetable_routes.py)
│   │   ├── auth/ (login.py, security.py)
│   │   ├── database/ (connection.py, json_storage.py, various structured json files)
│   │   ├── models/ (common.py)
│   │   └── services/ (timetable_service.py)
│   └── frontend/
│       ├── components/ (Button, Card, Layout)
│       ├── pages/ (Home, Login, NoticeBoard)
│       └── utils/ (timetableConstants.ts)
├── gateway/
│   └── main.py (Main FastAPI aggregator)
├── server/
│   ├── docker-compose.yml
│   └── nginx.conf
├── src/
│   ├── App.tsx (Main Routing logic)
│   ├── index.css (Global styles / Tailwind)
│   └── main.tsx (React DOM root)
└── workspaces/
    ├── academic_coordinator/ (frontend pages & backend routes)
    ├── admission_officer/
    ├── common/ (Examination, Hrms, StudentCentral, UserManagementSystem, etc.)
    ├── course_coordinator/
    ├── employee/ (Attendance, Leaves, Salary, etc.)
    ├── examination/ (Results, Tests, Reports, etc.)
    ├── faculty/ (ClassTimetable, Lms, MyCourses, etc.)
    ├── hostel_admin/ (GatePass, Hostels, Attendance, etc.)
    ├── payment_administrator/ (Challans, Concessions, OnlineTransactions, etc.)
    ├── sports_officer/ (EventCalendar, Certificates, Teams, etc.)
    ├── student/ (Chatbot, Dashboard, Examinations, Fees, Profile)
    ├── team_owner/ (Institutions, Apps, DataManagement)
    └── transport_coordinator/ (Buses, Routes, Analytics)
```

*(Note: Every specific workspace mimics a standard frontend/backend modular setup with identical internal hierarchy as described further below).*

## 3. Core Modules Explained

### Root Configuration & Helper Scripts
- **`package.json` / `vite.config.ts` / `tsconfig*.json`**: Frontend tooling, build configurations, dependencies, and strict TypeScript rules.
- **`tailwind.config.cjs` & `postcss.config.cjs`**: Primary styling themes, utility generation, and post-processing tools.
- **Python Automation Scripts**: Scripts located in root (e.g., `scaffold_workspaces.py`, `update_workspaces.py`, `update_app_tsx.py`, `fix_dashboards.py`) used to rapidly bootstrap new modules, sync changes across multiple workspaces, or hotfix React index files without manual drudgery.

### `src/` (Frontend Entrypoint)
- **`main.tsx` & `App.tsx`**: The core React application start. `App.tsx` is specifically critical because it intelligently lazy-loads specific workspaces matching the authenticated user's role ensuring performance scaling.
- **`index.css`**: Tailwind setup encompassing the core design system's variables and primary overrides.

### `server/` & `gateway/` (Backend Entrypoint & Deployment)
- **`gateway/main.py`**: The central API Gateway built entirely in FastAPI. It automatically dynamically imports and mounts all granular routes from individual modules turning micro-app-like structure into a cohesive single API.
- **`server/` directory**: Contains `docker-compose.yml` and generic reverse-proxy setups (`nginx.conf`) allowing immediate, replicable containerization in production environments.

### `core/` (Shared Logic & Common Base)
Holds essential blocks that act as utilities shared application-wide to enforce DRY boundaries:
- **`core/frontend/`**: Hosts generic resuable building blocks such as custom `<Button />`, `<Card />`, and primary structural `<Layout />`. Also retains universal entry flows like `<Login />` and core interfaces.
- **`core/backend/`**: Serves as the authentication and data highway. Highlights include:
  - **Auth System**: Generic JWT verifications globally applied via `login.py` & `security.py`.
  - **Shared DB State**: Localized flat JSON datasets that sync data across module boundaries (e.g., common `users.json`, `institutions.json`, and robust wrappers like `json_storage.py`).

### `workspaces/` (Role-Based Features / Domain Contexts)
The architectural philosophy is Domain-Driven modularity. Each folder completely sandboxes a business feature/target audience role guaranteeing that changes made to the Transport workflow won’t mistakenly break Student fees logic.

**Standard Anatomy inside a Workspace (e.g., `student/`):** 
- **`frontend/`**:
  - `pages/`: Dedicated unique `.tsx` screens. (e.g., `Dashboard.tsx`, `NoticeBoard.tsx`, `Attendance.tsx`). Keep views dumb, feed local functionality via React hooks where necessary.
  - `components/`: Granular interface splits specifically intended for this singular view context.
  - `services/`: Fetch wrappers dedicated only to calling its coupled `backend` service.
- **`backend/`**:
  - `api/routes.py`: FastAPI Router definitions tightly constrained to endpoints servicing merely this domain slice.
  - `services/logic.py`: The heavy lifting business rules parsing raw data for validation.
  - `models/` *(optional)*: Pydantic definitions strictly ensuring API type-checking and payload validation before reaching `logic.py`.
- **`database/`**:
  - `database.json`: Dedicated JSON data specific directly for the localized feature context limiting DB collision until transitioned entirely to MongoDB.

## 4. Key Workspaces Overview

1. **`student/`**: A heavy read-write zone dedicated to standard pupil interfaces — `CourseTracking`, `Examinations` viewing, `PaymentHistory`, and `Attendance`.
2. **`faculty/`**: Tools tailored towards educators such as managing `ClassTimetable`, uploading materials via `Lms`, formatting `QuestionBanks`, and tracking `MyMentees`.
3. **`transport_coordinator/`**: Contains complex logistics mapping managing actual spatial objects like `Buses`, `Routes`, tracking `TransportRoute` and `BoardingPoints`.
4. **`super_admin/` & `team_owner/`**: The highest tier handling meta-resources like spinning up completely fresh `Institutions`, tweaking overarching global `OrganizationSettings` and user assignments.
5. **`common/`**: The standard toolkit that virtually any validated employee or member uses interactively: Centralized `Hrms`, broad scoped `NoticeBoard`, standard `Dashboard`, and logging `MyRequests`.

## 5. Development Workflow Guidelines

- **Adding a New Page**: 
  1. Simply add your `.tsx` file to the target workspace's `frontend/pages/` directory.
  2. The main navigation/router handles detection; no intricate web-weaving required.
- **Creating an Endpoint**: Generate business logic inside `<Workspace>/backend/services/logic.py`, connect it through validation inside that specific `routes.py`, and it will systematically compile safely at the `gateway/main.py`.
- **Database Interaction Phase**: Currently interacting mostly through localized JSON (NoSQL mock-format). It specifically leans on `core/backend/database/json_storage.py` to emulate standardized Read/Write/Update methods that directly clone typical PyMongo paradigms ensuring zero friction upon upcoming migration to a robust production Document DB.
