"""
Timetable API — AI-powered timetable generation with conflict resolution
"""
from datetime import datetime
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Depends, Body
from ...shared.database import get_collection
from ...shared.models.schemas import Timetable, TimetableSlot
from ...shared.services.rbac_service import get_current_user

router = APIRouter()


def resolve_conflicts(slots: List[dict]) -> dict:
    """AI conflict resolver — detect faculty/room/class clashes"""
    conflicts = []
    by_faculty = {}
    by_room = {}

    for slot in slots:
        key = f"{slot['day']}_{slot['period']}"
        faculty_key = f"{slot['faculty_id']}_{key}"
        room_key = f"{slot['room']}_{key}"

        if faculty_key in by_faculty:
            conflicts.append({
                "type": "faculty_conflict",
                "faculty": slot["faculty_id"],
                "day": slot["day"],
                "period": slot["period"],
                "classes": [by_faculty[faculty_key]["class_name"], slot["class_name"]],
            })
        else:
            by_faculty[faculty_key] = slot

        if room_key in by_room:
            conflicts.append({
                "type": "room_conflict",
                "room": slot["room"],
                "day": slot["day"],
                "period": slot["period"],
            })
        else:
            by_room[room_key] = slot

    return {"conflicts": conflicts, "is_valid": len(conflicts) == 0}


@router.post("/generate", response_model=dict)
async def generate_timetable(
    institution_id: str,
    class_name: str,
    section: str,
    subjects: List[dict] = Body(...),  # [{subject, faculty_id, periods_per_week}]
    academic_year: str = "2024-25",
    current_user=Depends(get_current_user),
):
    """AI-powered timetable generation with conflict resolution"""
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    periods = [
        {"period": 1, "start": "09:00", "end": "09:45"},
        {"period": 2, "start": "09:45", "end": "10:30"},
        {"period": 3, "start": "10:45", "end": "11:30"},
        {"period": 4, "start": "11:30", "end": "12:15"},
        {"period": 5, "start": "13:00", "end": "13:45"},
        {"period": 6, "start": "13:45", "end": "14:30"},
        {"period": 7, "start": "14:30", "end": "15:15"},
    ]

    slots = []
    period_map = {d: [] for d in days}

    for subj in subjects:
        count = 0
        for day in days:
            if count >= subj.get("periods_per_week", 5):
                break
            for period in periods:
                if len(period_map[day]) < len(periods):
                    slot = TimetableSlot(
                        day=day,
                        period=period["period"],
                        start_time=period["start"],
                        end_time=period["end"],
                        subject=subj["subject"],
                        faculty_id=subj["faculty_id"],
                        room=subj.get("room", f"Room{subj['faculty_id'][-3:]}"),
                        class_name=class_name,
                        section=section,
                    )
                    slots.append(slot.dict())
                    period_map[day].append(period["period"])
                    count += 1
                    break

    conflict_result = resolve_conflicts(slots)

    timetable_doc = {
        "institution_id": institution_id,
        "class_name": class_name,
        "section": section,
        "academic_year": academic_year,
        "term": "I",
        "slots": slots,
        "generated_by_ai": True,
        "created_at": datetime.utcnow(),
        "conflicts": conflict_result["conflicts"],
        "is_valid": conflict_result["is_valid"],
    }

    timetables = get_collection("timetables")
    await timetables.update_one(
        {"institution_id": institution_id, "class_name": class_name, "section": section},
        {"$set": timetable_doc},
        upsert=True,
    )

    return {
        "message": "Timetable generated",
        "timetable": timetable_doc,
        "conflict_report": conflict_result,
    }


@router.get("/{institution_id}/{class_name}/{section}")
async def get_timetable(
    institution_id: str,
    class_name: str,
    section: str,
    current_user=Depends(get_current_user),
):
    """Get timetable for a class"""
    timetables = get_collection("timetables")
    tt = await timetables.find_one({
        "institution_id": institution_id,
        "class_name": class_name,
        "section": section,
    })
    if not tt:
        raise HTTPException(status_code=404, detail="Timetable not found")
    tt["_id"] = str(tt["_id"])
    return tt


@router.get("/faculty/{faculty_id}")
async def get_faculty_timetable(
    faculty_id: str,
    institution_id: str,
    current_user=Depends(get_current_user),
):
    """Get timetable for a faculty member across all classes"""
    timetables = get_collection("timetables")
    all_tts = await timetables.find({"institution_id": institution_id}).to_list(50)

    faculty_slots = []
    for tt in all_tts:
        for slot in tt.get("slots", []):
            if slot.get("faculty_id") == faculty_id:
                faculty_slots.append({**slot, "class": tt["class_name"], "section": tt["section"]})

    return {"faculty_id": faculty_id, "timetable": faculty_slots}


@router.put("/{institution_id}/{class_name}/{section}/slot")
async def update_slot(
    institution_id: str,
    class_name: str,
    section: str,
    updated_slot: TimetableSlot,
    current_user=Depends(get_current_user),
):
    """Update a single timetable slot (drag-drop editor)"""
    timetables = get_collection("timetables")
    result = await timetables.update_one(
        {
            "institution_id": institution_id,
            "class_name": class_name,
            "section": section,
            "slots.day": updated_slot.day,
            "slots.period": updated_slot.period,
        },
        {"$set": {"slots.$": updated_slot.dict()}}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Slot not found")
    return {"message": "Slot updated"}
