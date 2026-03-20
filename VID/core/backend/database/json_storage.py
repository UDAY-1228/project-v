import json
import os
from typing import Dict, List, Any

STORAGE_PATH = "/Users/nivas/Documents/React apps/VID/core/backend/database/storage.json"

def ensure_storage():
    if not os.path.exists(STORAGE_PATH):
        os.makedirs(os.path.dirname(STORAGE_PATH), exist_ok=True)
        with open(STORAGE_PATH, 'w') as f:
            json.dump({"institutions": [], "users": []}, f)

def read_storage() -> Dict[str, Any]:
    ensure_storage()
    with open(STORAGE_PATH, 'r') as f:
        return json.load(f)

def write_storage(data: Dict[str, Any]):
    with open(STORAGE_PATH, 'w') as f:
        json.dump(data, f, indent=4)

def add_institution(inst: Dict[str, Any]):
    data = read_storage()
    data["institutions"].append(inst)
    write_storage(data)

def add_user(user: Dict[str, Any]):
    data = read_storage()
    data["users"].append(user)
    write_storage(data)

def get_institutions() -> List[Dict[str, Any]]:
    return read_storage().get("institutions", [])

def get_users() -> List[Dict[str, Any]]:
    return read_storage().get("users", [])
