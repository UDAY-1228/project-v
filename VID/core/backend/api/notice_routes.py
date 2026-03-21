from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import json, os, uuid
from datetime import datetime

router = APIRouter(tags=["Notices"])

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "notices.json")


def _load():
    with open(DB_PATH, "r") as f:
        return json.load(f)

def _save(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)


class NoticeCreate(BaseModel):
    title: str
    content: str
    category: str
    priority: str = "medium"
    author: str
    authorRole: str
    pinned: bool = False
    tags: Optional[List[str]] = []


@router.get("/notices")
async def get_notices():
    data = _load()
    notices = data.get("notices", [])
    # Sort: pinned first, then by date descending
    pinned = [n for n in notices if n.get("pinned")]
    rest = sorted([n for n in notices if not n.get("pinned")], key=lambda x: x.get("postedAt", ""), reverse=True)
    return {"notices": pinned + rest}


@router.get("/notices/{notice_id}")
async def get_notice(notice_id: str):
    data = _load()
    for n in data.get("notices", []):
        if n["id"] == notice_id:
            return n
    raise HTTPException(status_code=404, detail="Notice not found")


@router.post("/notices")
async def create_notice(notice: NoticeCreate):
    data = _load()
    new_notice = {
        "id": str(uuid.uuid4()),
        "title": notice.title,
        "content": notice.content,
        "category": notice.category,
        "priority": notice.priority,
        "author": notice.author,
        "authorRole": notice.authorRole,
        "postedAt": datetime.now().isoformat(),
        "pinned": notice.pinned,
        "tags": notice.tags or []
    }
    data.setdefault("notices", []).insert(0, new_notice)
    _save(data)
    return {"success": True, "notice": new_notice}


@router.put("/notices/{notice_id}/pin")
async def toggle_pin(notice_id: str):
    data = _load()
    for n in data.get("notices", []):
        if n["id"] == notice_id:
            n["pinned"] = not n.get("pinned", False)
            _save(data)
            return {"success": True, "pinned": n["pinned"]}
    raise HTTPException(status_code=404, detail="Notice not found")


@router.delete("/notices/{notice_id}")
async def delete_notice(notice_id: str):
    data = _load()
    original = len(data.get("notices", []))
    data["notices"] = [n for n in data.get("notices", []) if n["id"] != notice_id]
    if len(data["notices"]) == original:
        raise HTTPException(status_code=404, detail="Notice not found")
    _save(data)
    return {"success": True}
