// ── TypeScript Models for EIMS Frontend ─────────────────────────────────────

export type UserRole = 'super_admin' | 'institution_admin' | 'faculty' | 'ed_official' | 'student' | 'parent';
export type Gender = 'male' | 'female' | 'other';
export type AttendanceStatus = 'present' | 'absent' | 'late' | 'excused';
export type FeeStatus = 'pending' | 'paid' | 'overdue' | 'waived' | 'partial';
export type ExamType = 'unit_test' | 'mid_term' | 'final' | 'practice';
export type RiskLevel = 'high' | 'medium' | 'low';
export type NotificationType = 'info' | 'warning' | 'alert' | 'reminder';

// ── Address ────────────────────────────────────────────────────────────────
export interface Address {
  street: string;
  city: string;
  state: string;
  pincode: string;
  country: string;
}

// ── Institution ───────────────────────────────────────────────────────────
export interface Institution {
  id: string;
  name: string;
  code: string;
  type: string;
  address: Address;
  phone: string;
  email: string;
  website?: string;
  logo_url?: string;
  affiliation_board?: string;
  academic_year: string;
  languages: string[];
  total_capacity: number;
  is_active: boolean;
  created_at: string;
}

// ── User ──────────────────────────────────────────────────────────────────
export interface User {
  id: string;
  full_name: string;
  email: string;
  phone: string;
  role: UserRole;
  institution_id?: string;
  gender: Gender;
  date_of_birth?: string;
  address?: Address;
  language_preference: string;
  profile_photo?: string;
  is_active: boolean;
  created_at: string;
  virtual_id?: string;
  qr_code_url?: string;
  face_enrolled: boolean;
}

// ── Auth ──────────────────────────────────────────────────────────────────
export interface LoginRequest {
  email: string;
  password: string;
  institution_code?: string;
}

export interface TokenResponse {
  access_token: string;
  refresh_token: string;
  token_type: string;
  expires_in: number;
  role: UserRole;
  user: User;
}

// ── Virtual ID ────────────────────────────────────────────────────────────
export interface VirtualId {
  user_id: string;
  institution_id: string;
  virtual_id_number: string;
  qr_code_url: string;
  qr_code_data: string;
  face_encoding_hash?: string;
  face_enrolled: boolean;
  face_enrollment_date?: string;
  is_active: boolean;
  issued_at: string;
  expires_at?: string;
}

// ── Attendance ────────────────────────────────────────────────────────────
export interface AttendanceLog {
  id?: string;
  student_id: string;
  institution_id: string;
  class_name: string;
  section: string;
  date: string;
  subject?: string;
  status: AttendanceStatus;
  method: 'manual' | 'face_ai' | 'qr' | 'kiosk';
  marked_by: string;
  ai_confidence?: number;
  override_reason?: string;
  timestamp: string;
}

export interface AttendanceSummary {
  student_id: string;
  total_days: number;
  present_days: number;
  absent_days: number;
  late_days: number;
  percentage: number;
  at_risk: boolean;
}

// ── Timetable ─────────────────────────────────────────────────────────────
export interface TimetableSlot {
  day: string;
  period: number;
  start_time: string;
  end_time: string;
  subject: string;
  faculty_id: string;
  room: string;
  class_name: string;
  section: string;
}

export interface Timetable {
  id?: string;
  institution_id: string;
  class_name: string;
  section: string;
  academic_year: string;
  term: string;
  slots: TimetableSlot[];
  generated_by_ai: boolean;
  created_at: string;
}

// ── Fees ──────────────────────────────────────────────────────────────────
export interface FeeItem {
  description: string;
  amount: number;
  due_date: string;
}

export interface FeeInvoice {
  id?: string;
  student_id: string;
  institution_id: string;
  invoice_number: string;
  academic_year: string;
  term: string;
  items: FeeItem[];
  total_amount: number;
  paid_amount: number;
  status: FeeStatus;
  payment_date?: string;
  payment_method?: string;
  transaction_id?: string;
  waiver_reason?: string;
  created_at: string;
}

// ── LMS ───────────────────────────────────────────────────────────────────
export interface CourseContent {
  title: string;
  content_type: 'video' | 'pdf' | 'quiz' | 'link';
  url: string;
  duration_minutes?: number;
  order: number;
}

export interface Course {
  id?: string;
  institution_id: string;
  title: string;
  subject: string;
  class_name: string;
  faculty_id: string;
  description: string;
  thumbnail_url?: string;
  contents: CourseContent[];
  published: boolean;
  created_at: string;
}

export interface Assignment {
  id?: string;
  institution_id: string;
  title: string;
  description: string;
  subject: string;
  class_name: string;
  section: string;
  faculty_id: string;
  due_date: string;
  max_marks: number;
  allow_late: boolean;
  attachments: string[];
  status: 'draft' | 'published' | 'submitted' | 'graded';
  created_at: string;
}

// ── Exams ─────────────────────────────────────────────────────────────────
export interface ExamResult {
  id?: string;
  exam_id: string;
  student_id: string;
  marks_obtained: number;
  grade: string;
  rank?: number;
  remarks?: string;
  subject_scores: { [subject: string]: number };
  published: boolean;
  published_at?: string;
}

// ── Analytics ─────────────────────────────────────────────────────────────
export interface AtRiskStudent {
  student_id: string;
  full_name: string;
  class: string;
  risk_score: number;
  risk_level: RiskLevel;
  risk_factors: string[];
  recommendations: string[];
}

export interface DashboardStats {
  total_students: number;
  total_faculty: number;
  today_attendance: number;
  today_attendance_pct: number;
  fee_collected: number;
  fee_overdue: number;
  weekly_attendance_trend: { date: string; present: number }[];
}

// ── Notifications ─────────────────────────────────────────────────────────
export interface Notification {
  id?: string;
  user_id: string;
  title: string;
  message: string;
  type: NotificationType;
  action_url?: string;
  read: boolean;
  created_at: string;
}

// ── AI Homework Helper ────────────────────────────────────────────────────
export interface HomeworkHintResponse {
  hint: string;
  answer?: string;
  subject: string;
  class?: number;
  ai_powered: boolean;
  note?: string;
}

// ── API Response Wrapper ──────────────────────────────────────────────────
export interface ApiResponse<T> {
  data?: T;
  message?: string;
  error?: string;
  success: boolean;
}

// ── Pagination ────────────────────────────────────────────────────────────
export interface PaginatedResponse<T> {
  items: T[];
  total: number;
  page: number;
  per_page: number;
  total_pages: number;
}
