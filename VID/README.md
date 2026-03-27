# VID (Virtual Identification System)

## Project Overview
VID is an enterprise-level education and institutional management platform. It leverages a scalable, modular, workspace-based architecture to centralize all institutional operations into a unified platform.

## Key Features
- **AI Integration**: AI Indra for analytics and a Voice Agent for parent communication.
- **Auto-Generation**: Backend APIs, services, and schemas are automatically generated based on frontend definitions.
- **Single Login System**: JWT-based single login for all roles.
- **Multi-Tenant Isolation**: Institution-level isolation for data and permissions.

## Tech Stack
- **Frontend**: Angular (TypeScript).
- **Backend**: Python (FastAPI).
- **Database**: MongoDB (Auto-generated).
- **Authentication**: JWT Single Sign-On (SSO).
- **Architecture**: Modular Workspace-Based.

## Project Structure
```
VID/
├── admin-panels/
│   ├── Frontend/           # Angular Components
│   │   ├── super-admin/
│   │   ├── admin/
│   │   └── core-system/
│   └── Backend/            # FastAPI Auto-Generated APIs
│       ├── super-admin/
│       ├── admin/
│       ├── core-system/
│       └── auto_api_generator.py # Base Logic for API Generation
└── workspaces/             # Modular Business Units
    ├── student/
    ├── faculty/
    └── [28+ other workspaces]
```

## Getting Started
1. **Frontend Development**: Launch individual Angular modules for Super Admin, Admin, and Core System.
2. **Backend Development**: Utilize the `auto_api_generator.py` to spin up services matching the frontend requirements.
3. **AI Services**: Configure AI Indra and Voice Agent settings in the corresponding workspace.

---
© 2026 Virtual Identification System (VID) - Enterprise Edition.
