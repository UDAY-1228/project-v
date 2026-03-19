// MongoDB Initialization Script for EIMS — Specialized Structure
// Run via docker-compose on first startup

db = db.getSiblingDB('eims_db');

// ── Collections with index setup ──────────────────────────────
db.createCollection('institutions');
db.institutions.createIndex({ "code": 1 }, { unique: true });

db.createCollection('users');
db.users.createIndex({ "email": 1 }, { unique: true });
db.users.createIndex({ "role": 1 });
db.users.createIndex({ "institution_id": 1 });

db.createCollection('attendance');
db.attendance.createIndex({ "student_id": 1, "date": 1 });

db.createCollection('virtual_ids');
db.virtual_ids.createIndex({ "user_id": 1 }, { unique: true });

db.createCollection('lms_courses');
db.lms_courses.createIndex({ "institution_id": 1 });

db.createCollection('assignments');
db.assignments.createIndex({ "course_id": 1 });

db.createCollection('ptm_slots');
db.ptm_slots.createIndex({ "faculty_id": 1, "date": 1 });

db.createCollection('fee_plans');
db.fee_plans.createIndex({ "institution_id": 1 });

db.createCollection('invoices');
db.invoices.createIndex({ "student_id": 1 });

db.createCollection('audit_logs');
db.audit_logs.createIndex({ "institution_id": 1, "created_at": -1 });

// ── Demo Seed Data ───────────────────────────────────────────

const instId = ObjectId();

// 🏫 Institution: DPS Hyderabad
db.institutions.insertOne({
  _id: instId,
  name: "Delhi Public School, Hyderabad",
  code: "DPS-HYD",
  type: "CBSE School",
  academic_year: "2024-25",
  is_active: true,
  created_at: new Date()
});

// 👥 Specialized Admin Users
db.users.insertMany([
  // 👔 Super Admin (Platform-wide)
  {
    full_name: "EIMS Super Admin",
    email: "superadmin@eims.edu.in",
    password: "$pbkdf2-sha256$29000$P98x.z4V9vH... (hashed)", // Example hash
    role: "super_admin",
    is_active: true,
    created_at: new Date()
  },
  // 🏫 Institution Admin (DPS Hyderabad)
  {
    full_name: "DPS Principal Admin",
    email: "admin@dpshyd.edu.in",
    password: "$pbkdf2-sha256$29000$P98x.z4V9vH... (hashed)",
    role: "institution_admin",
    institution_id: instId,
    is_active: true,
    created_at: new Date()
  },
  // 🎓 Faculty (Teacher Admin)
  {
    full_name: "Dr. Nivas Teacher",
    email: "teacher@dpshyd.edu.in",
    password: "$pbkdf2-sha256$29000$P98x.z4V9vH... (hashed)",
    role: "faculty",
    institution_id: instId,
    is_active: true,
    created_at: new Date()
  },
  // 🤵 Student (DPH Hyderabad)
  {
    full_name: "Rahul Student",
    email: "student@dpshyd.edu.in",
    password: "$pbkdf2-sha256$29000$P98x.z4V9vH... (hashed)",
    role: "student",
    institution_id: instId,
    is_active: true,
    created_at: new Date(),
    class_name: "Class 10",
    section: "A"
  }
]);

// 📚 LMS: Demo Course
const courseId = ObjectId();
db.lms_courses.insertOne({
  _id: courseId,
  institution_id: instId,
  name: "Applied Mathematics 101",
  teacher_id: "teacher@dpshyd.edu.in",
  active: true,
  created_at: new Date()
});

// 📝 Assignments
db.assignments.insertMany([
  { course_id: courseId, title: "Trigonometry Basics", due_date: new Date(), max_marks: 20 },
  { course_id: courseId, title: "Calculus Introduction", due_date: new Date(), max_marks: 50 }
]);

// 👨👩👧 PTM Slots
db.ptm_slots.insertMany([
  { faculty_id: "teacher@dpshyd.edu.in", time: "10:00 AM", status: "booked", parent_name: "Anita Ravi Kumar" },
  { faculty_id: "teacher@dpshyd.edu.in", time: "10:15 AM", status: "available" }
]);

// 💰 Finance: Demo Fee Plan
db.fee_plans.insertOne({
  institution_id: instId,
  name: "Annual Tuition Fee 2024",
  amount: 45000,
  frequency: "annual",
  created_at: new Date()
});

// 📊 Audit Logs
db.audit_logs.insertOne({
  institution_id: instId,
  user: "admin@dpshyd.edu.in",
  action: "FEE_PLAN_CREATED",
  details: "Created Annual Tuition Fee 2024",
  created_at: new Date()
});

print("✅ MongoDB Initialization & Seed Data Injection Complete");
