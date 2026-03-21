// Shared sidebar items + types for Timetable pages
export const TIMETABLE_SIDEBAR_ACADEMIC = [
  { label: "Digital Notice Board", icon: "announcement", path: "/academic-coordinator/notice-board" },
  { label: "Activities", icon: "event", path: "/academic-coordinator/activities" },
  { label: "Principal Dashboard", icon: "dashboard_customize", path: "/academic-coordinator/principal-dashboard" },
  { label: "Academics", icon: "school", path: "/academic-coordinator/academics" },
  { label: "Academic Setup", icon: "settings_suggest", path: "/academic-coordinator/setup" },
  { label: "Courses", icon: "menu_book", path: "/academic-coordinator/courses" },
  { label: "Master Courses", icon: "library_books", path: "/academic-coordinator/master-courses" },
  { label: "Assessment", icon: "assignment_turned_in", path: "/academic-coordinator/assessment" },
  { label: "Timetable", icon: "calendar_month", path: "/academic-coordinator/timetable" },
  { label: "Faculty Absence", icon: "person_off", path: "/academic-coordinator/timetable-absence" },
  { label: "Data Management", icon: "storage", path: "/academic-coordinator/data-management" },
  { label: "Configurations", icon: "settings", path: "/academic-coordinator/config" },
];

export const SUBJECT_COLORS: Record<string, string> = {
  Math: "bg-blue-100 text-blue-800 border-blue-200",
  Physics: "bg-purple-100 text-purple-800 border-purple-200",
  English: "bg-green-100 text-green-800 border-green-200",
  Chemistry: "bg-orange-100 text-orange-800 border-orange-200",
  "Computer Science": "bg-indigo-100 text-indigo-800 border-indigo-200",
  "Data Structures": "bg-cyan-100 text-cyan-800 border-cyan-200",
  Networks: "bg-teal-100 text-teal-800 border-teal-200",
  "Operating Systems": "bg-rose-100 text-rose-800 border-rose-200",
  Electronics: "bg-yellow-100 text-yellow-800 border-yellow-200",
  Signals: "bg-pink-100 text-pink-800 border-pink-200",
  Microprocessors: "bg-lime-100 text-lime-800 border-lime-200",
  BREAK: "bg-slate-100 text-slate-400 border-slate-200",
};

export function subjectColor(subject: string): string {
  return SUBJECT_COLORS[subject] || "bg-violet-100 text-violet-800 border-violet-200";
}
