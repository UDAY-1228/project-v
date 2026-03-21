import json
import os
from typing import Dict, List, Any

import json
import os
from typing import Dict, List, Any

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_PATH = os.path.join(BASE_DIR, "users.json")
INSTS_PATH = os.path.join(BASE_DIR, "institutions.json")
WS_PATH = os.path.join(BASE_DIR, "workspaces.json")

def ensure_file(path: str, default_data: Any = []):
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            json.dump(default_data, f)

def read_json(path: str) -> Any:
    ensure_file(path)
    with open(path, 'r') as f:
        return json.load(f)

def write_json(path: str, data: Any):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def add_institution(inst: Dict[str, Any]):
    data = read_json(INSTS_PATH)
    data.append(inst)
    write_json(INSTS_PATH, data)

def add_user(user: Dict[str, Any]):
    data = read_json(USERS_PATH)
    data.append(user)
    write_json(USERS_PATH, data)

def get_institutions() -> List[Dict[str, Any]]:
    return read_json(INSTS_PATH)

def get_users() -> List[Dict[str, Any]]:
    return read_json(USERS_PATH)

def get_workspaces() -> List[Dict[str, Any]]:
    return read_json(WS_PATH)

