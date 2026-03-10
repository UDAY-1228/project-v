# VID: Virtual Identification + CampX Platform

National-scale education platform for India with AI-powered attendance, identity, and campus management.

## Project Structure

```text
vid-platform/
├── backend/                # FastAPI (Python)
│   ├── app/
│   │   ├── api/v1/         # REST API Endpoints
│   │   ├── core/           # Config, Security, Auth logic
│   │   └── services/       # Business logic services
│   └── main.py             # Entry point
├── frontend-web/           # Next.js + TypeScript + Tailwind
│   ├── public/
│   └── src/
│       ├── components/     # UI Components (Sidebar, Charts, etc.)
│       ├── hooks/
│       ├── pages/          # Dashboard Pages (Admin, Teacher, Student)
│       └── styles/
├── mobile-app/             # Angular + Ionic (Cross-platform)
│   ├── src/app/
│   │   ├── academic/       # Attendance, Timetable, Exams
│   │   ├── auth/           # Login, MFA
│   │   ├── profile/        # Virtual ID
│   │   └── tabs/           # Bottom Navigation
├── database/               # MongoDB models & connection logic
│   └── models.py           # Pydantic Schemas
├── ai-services/            # Python ML services
│   ├── face_recognition.py # AI Attendance Logic
│   └── analysis.py         # Risk Detection & Predictive Analytics
└── infrastructure/         # Deployment Scripts
    ├── docker/             # Dockerfiles & Compose
    └── kubernetes/         # K8s Manifests
```

## Key Modules
1. **AI Attendance**: Face recognition via mobile camera or kiosk.
2. **Virtual ID**: QR-based digital identity for campus access.
3. **LMS**: Course management with AI Homework Assistant.
4. **Payments**: Integrated UPI (Razorpay/PhonePe) for fee collection.
5. **Analytics**: Real-time student performance and risk monitoring.

## Getting Started
### Backend
```bash
cd backend
pip install -r requirements.txt
python main.py
```

### Frontend Web
```bash
cd frontend-web
npm install
npm run dev
```

### Mobile App
```bash
cd mobile-app
npm install
ionic serve
```
