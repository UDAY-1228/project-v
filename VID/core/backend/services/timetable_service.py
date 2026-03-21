import json
import os
import uuid
from typing import Any, Dict, List, Optional

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "timetable_data.json")


def _load() -> Dict[str, Any]:
    with open(DB_PATH, "r") as f:
        return json.load(f)


def _save(data: Dict[str, Any]):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)


# ──────────────────────────────────────────
# READ HELPERS
# ──────────────────────────────────────────

def get_all_classes() -> List[str]:
    data = _load()
    return [c["classId"] for c in data.get("courses", [])]


def get_faculty_list() -> List[Dict]:
    return _load().get("faculty", [])


def get_courses(class_id: str) -> Optional[Dict]:
    data = _load()
    for c in data.get("courses", []):
        if c["classId"] == class_id:
            return c
    return None


def get_timetable(class_id: str) -> Optional[Dict]:
    data = _load()
    for t in data.get("timetables", []):
        if t["classId"] == class_id:
            return t
    return None


def get_all_timetables() -> List[Dict]:
    return _load().get("timetables", [])


# ──────────────────────────────────────────
# TIMETABLE GENERATION
# ──────────────────────────────────────────

PERIODS = ["9:00-10:00", "10:00-11:00", "11:00-12:00", "12:00-1:00", "1:00-2:00", "2:00-3:00", "3:00-4:00"]
BREAK_PERIOD = "12:00-1:00"
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def generate_timetable(class_id: str, working_days: List[str], periods_per_day: int, break_time: str) -> Dict:
    """
    Simple round-robin auto generator:
    - Cycles subjects across days & periods
    - Respects break slot
    - No faculty clash tracking across classes (single-class scope is conflict-free by design)
    """
    course = get_courses(class_id)
    if not course:
        raise ValueError(f"No course found for class {class_id}")

    subjects = course["subjects"]  # [{ subject, facultyId }]
    n_subjects = len(subjects)
    idx = 0  # rolling pointer
    schedule = []

    for day in working_days:
        periods = []
        slots_used = 0
        for time_slot in PERIODS:
            if time_slot == break_time:
                periods.append({"time": time_slot, "subject": "BREAK", "facultyId": None, "isBreak": True})
                continue
            if slots_used >= periods_per_day:
                break
            sub_entry = subjects[idx % n_subjects]
            periods.append({
                "time": time_slot,
                "subject": sub_entry["subject"],
                "facultyId": sub_entry["facultyId"],
                "isBreak": False
            })
            idx += 1
            slots_used += 1
        schedule.append({"day": day, "periods": periods})

    return {
        "timetableId": str(uuid.uuid4()),
        "classId": class_id,
        "schedule": schedule
    }


def save_timetable(timetable: Dict):
    data = _load()
    # Remove old entry if exists
    data["timetables"] = [t for t in data.get("timetables", []) if t["classId"] != timetable["classId"]]
    data["timetables"].append(timetable)
    _save(data)


def update_timetable(class_id: str, schedule: List[Dict]):
    data = _load()
    for t in data.get("timetables", []):
        if t["classId"] == class_id:
            t["schedule"] = schedule
            _save(data)
            return True
    return False


# ──────────────────────────────────────────
# ABSENCE / SUBSTITUTE LOGIC
# ──────────────────────────────────────────

def mark_absent(faculty_id: str, date: str) -> Dict:
    data = _load()
    absence_id = str(uuid.uuid4())
    rec = {"absenceId": absence_id, "facultyId": faculty_id, "date": date}
    data.setdefault("absences", []).append(rec)
    _save(data)
    return rec


def get_absences() -> List[Dict]:
    return _load().get("absences", [])


def _faculty_teaches_subject(faculty_id: str, subject: str, faculty_list: List[Dict]) -> bool:
    for f in faculty_list:
        if f["facultyId"] == faculty_id:
            return subject in f.get("subjects", [])
    return False


def get_substitute_suggestions(faculty_id: str, subject: str) -> List[Dict]:
    """Return faculty who can teach the same subject (excluding the absent one)."""
    data = _load()
    faculty_list = data.get("faculty", [])
    same_subject = [
        f for f in faculty_list
        if f["facultyId"] != faculty_id and subject in f.get("subjects", [])
    ]
    # If none, suggest any other faculty as free substitute
    if not same_subject:
        same_subject = [f for f in faculty_list if f["facultyId"] != faculty_id][:3]
    return same_subject


def assign_substitute(class_id: str, day: str, time_slot: str, substitute_faculty_id: str) -> bool:
    data = _load()
    for t in data.get("timetables", []):
        if t["classId"] == class_id:
            for d in t["schedule"]:
                if d["day"] == day:
                    for p in d["periods"]:
                        if p["time"] == time_slot:
                            p["substituteId"] = substitute_faculty_id
                            _save(data)
                            return True
    return False


def get_affected_periods(faculty_id: str, date: str) -> List[Dict]:
    """Find all periods taught by this faculty on any timetable (by day-of-week match)."""
    from datetime import datetime
    try:
        day_name = datetime.strptime(date, "%Y-%m-%d").strftime("%A")
    except Exception:
        day_name = date  # allow passing day name directly

    data = _load()
    affected = []
    for t in data.get("timetables", []):
        for d in t.get("schedule", []):
            if d["day"] == day_name:
                for p in d.get("periods", []):
                    if p.get("facultyId") == faculty_id and not p.get("isBreak"):
                        affected.append({
                            "classId": t["classId"],
                            "day": day_name,
                            "time": p["time"],
                            "subject": p["subject"]
                        })
    return affected
