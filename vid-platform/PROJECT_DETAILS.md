# 🏥 VID Platform: Full Project Overview

This document provides a highly detailed, tabular breakdown of every component, page, and service within the **Virtual Identification + CampX** education platform.

---

## 💻 1. Frontend Web (React + Vite)
**Total Pages:** 122 | **Tech Stack:** React, TypeScript, Tailwind CSS, Vite

| Module Folder | Pages (Implemented) | Purpose |
| :--- | :--- | :--- |
| `src/pages/auth/` | Login, ForgotPassword, ResetPassword, ChangePassword, Logout, ActiveSessions | Security & Session Mgmt |
| `src/pages/profiles/` | StudentProfile, ParentProfile, TeacherProfile, AdminProfile, DeveloperProfile, VirtualID (QR/Face), ProfileEdit | User Identity & IDs |
| `src/pages/roles/` | RoleList, AssignRole, PermissionMatrix, RoleChangeHistory | RBAC (Access Control) |
| `src/pages/privacy/` | PrivacySettings, BiometricConsent, DataDownloadRequest | GDPR & Data Privacy |
| `src/pages/attendance/` | StudentDashboard, ClassDashboard, AttendanceDetail, FaceEnrollment, FlaggedAttendance, OverrideRequests, Policy, HolidaySetup, AlertSettings, NotificationLog | Smart AI Attendance Suite |
| `src/pages/cctv/` | CCTVLiveView, KioskList, KioskSettings | Hardware Integration |
| `src/pages/timetable/` | MyTimetableStudent, MyTimetableTeacher, ClassTimetable, TimetableGenerator, ConflictResolver, History | AI Schedule Management |
| `src/pages/calendar/` | InstitutionCalendar, MyCalendar, EventDetails, EventManagement | Academic Events |
| `src/pages/fees/` | FeePlanSetup, InvoiceList, WaiverScholarship, FeeDueList, PaymentHome, PaymentMethods, PaymentConfirmation, ReceiptDownload, StudentHistory, AdminOnlineTransactions, ManualPayment, FailedTransactions, RefundMgmt | Financial Ecosystem |
| `src/pages/lms/` | MyCourses, CourseDetail, LessonsTopics, ResourcesHandouts, StudentAssignments, TeacherAssignments, AssignmentDetail, SubmitAssignment, GradeFeedback | Learning Management |
| `src/pages/homework/` | HomeworkList, AIHomeworkHelper, AIExplanationView, HomeworkProgress | AI-Assisted Study |
| `src/pages/chatbot/` | AskAssistant, ChatHistory, HumanSupport | NLP Communication |
| `src/pages/exams/` | ExamCalendar, ExamTimetable, ExamSetup, HallTicket | Formal Assessment |
| `src/pages/results/` | MarksEntry, ResultVerification, PublishResults, StudentResultCard | Grading & Verification |
| `src/pages/practice/` | PracticeTestsList, StartAITest, TestResultAnalysis, TeacherTestRequest | AI Test Preparation |
| `src/pages/analytics/` | StudentAnalytics, ClassAnalytics, DepartmentAnalytics, InstitutionAnalytics, AtRiskStudents | Predictive Data Science |
| `src/pages/noticeboard/` | Feed, Announcements, NoticeDetails, CreateNotice | Official Broadcasts |
| `src/pages/messaging/` | MessagesInbox, MessagesOutbox, ClassChannel, ParentTeacherChat, PTMScheduler, SlotBooking, Summary | Unified Chat & PTM |
| `src/pages/clubs/` | ClubsDirectory, MyClubs, ClubDetail, CoCurricularCalendar, ClubAdmin | Student Life |
| `src/pages/tools/` | ToolsHome (Central System Hub) | Platform Directory |
| `src/pages/helpdesk/` | CreateTicket, TicketStatus, FAQ, ContactSupport | Technical Support |
| `src/pages/audit/` | UserActivityLog, SystemAuditLog | Security Verification |

---

## 📱 2. Mobile App (Ionic + Angular)
**Total Screens:** 119 | **Tech Stack:** Angular, Ionic Framework, Capacitor

| Path Folder | Screens (Native implementation) | Key Features |
| :--- | :--- | :--- |
| `app/auth/` | Login, Forgot, Reset, ChangePassword, Logout | Fast Mobile Auth |
| `app/profile/` | Student, Parent, Teacher, Admin, Virtual-ID, Edit | Mobile Digital ID (QR) |
| `app/academic/` | Attendance(Dash, Class, Detail), Timetable, Calendar, Exams, Results | Portable Classroom |
| `app/finance/` | Fees (Setup, Invoices, Payment-Home, Receipt, History) | Integrated Mobile Pay |
| `app/lms/` | Courses, Detail, Lessons, Resources, Assignments | Mobile Learning |
| `app/homework/` | List, AI-Helper (Chat), AI-Explanation, Progress | Pocket AI Tutor |
| `app/chatbot/` | Ask, History, Support | Instant AI Support |
| `app/practice/` | List, AI-Test, Analysis | On-the-go Practice |
| `app/analytics/` | Student, Class, Dept, Institution | Performance Tracking |
| `app/noticeboard/`| Feed, Announcements, Details | Push-based Timeline |
| `app/messaging/` | Inbox, Outbox, Channel, PTM-Scheduler | Instant Communication |
| `app/tools/` | Home | Native Command Center |

---

## ⚙️ 3. Backend API (FastAPI)
**Architecture:** Micro-router Architecture | **Total Routers:** 14

| Router | Major Functionality | Database Collections Impacted |
| :--- | :--- | :--- |
| `auth.py` | JWT Token creation, multi-role verification. | `User`, `ActiveSession` |
| `system.py` | Unified config sync for Web & Mobile. | `SystemSettings` |
| `attendance.py`| Face AI processing, log generation, flags. | `AttendanceLog`, `FaceEnrollment` |
| `fees.py` | Invoice generation, transaction processing. | `FeePlan`, `Invoice`, `Transaction` |
| `lms.py` | Course management, AI-grading engine. | `Course`, `Assignment`, `Submission` |
| `exams.py` | Timetable logic, hall ticket generation. | `Exam`, `ExamSchedule` |
| `analytics.py` | predictive At-Risk detection algorithms. | `PerformanceMetric` |
| `messaging.py` | Real-time chat & PTM scheduling. | `Message`, `ChatRoom` |
| `profiles.py` | Virtual ID generation (Face/QR). | `StudentProfile`, `TeacherProfile` |

---

## 🤖 4. AI Services & Training Hub

| Area | Folder / File | Logic / Content |
| :--- | :--- | :--- |
| **CV Engine** | `ai-services/face_recognition.py` | MediaPipe Face Detection + Anti-Spoofing |
| **NLP Engine** | `ai-services/chatbot.py` | Transformers-based study and support chat |
| **Datasets** | `ai-services/training/datasets/` | `face_data`, `nlp_data`, `analytics_data` |
| **Training** | `ai-services/training/scripts/` | `train_face_embeddings.py`, `train_analytics_models.py` |
| **Models** | `ai-services/training/models/` | Trained binary files (.pkl, .onnx) |

---

## 📡 5. Synchronization & Hub System
The project uses a **Unified Tools Hub** architecture where:
1.  **Backend** publishes module availability.
2.  **Web & Mobile** hubs auto configure based on backend state.
3.  **Responsiveness** is guaranteed via Tailwind (Web) and Ionic Native Components (Mobile).

**Last Mapping Update:** March 11, 2026
**Status:** All folders and pages scaffolded and version-controlled.
