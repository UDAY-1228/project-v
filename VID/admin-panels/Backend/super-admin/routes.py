from fastapi import APIRouter, HTTPException, Depends
from .models import Institution, Statistic
from .services import InstitutionService, StatisticsService, MonitoringService
from typing import List

router = APIRouter()

# Institution Management APIs
@router.post("/institutions", response_model=str)
def create_institution(inst: dict):
    return InstitutionService.create_institution(inst)

@router.get("/institutions", response_model=List[dict])
def get_institutions():
    return InstitutionService.get_all_institutions()

@router.get("/institutions/{inst_id}", response_model=dict)
def get_institution(inst_id: str):
    res = InstitutionService.get_institution_by_id(inst_id)
    if not res:
        raise HTTPException(status_code=404, detail="Institution not found")
    return res

@router.put("/institutions/{inst_id}")
def update_institution(inst_id: str, data: dict):
    return InstitutionService.update_institution(inst_id, data)

@router.delete("/institutions/{inst_id}")
def delete_institution(inst_id: str):
    return InstitutionService.delete_institution(inst_id)

@router.patch("/institutions/{inst_id}/activation")
def patch_activation(inst_id: str, payload: dict):
    return InstitutionService.activate_deactivate_institution(inst_id, payload.get("is_active", True))

# Statistics & Monitoring APIs
@router.get("/statistics", response_model=dict)
def get_stats():
    return StatisticsService.get_overview_statistics()

@router.get("/monitoring/logs", response_model=List[dict])
def get_logs():
    return MonitoringService.get_system_logs()

# Terms & Policies APIs (simple fetch logic for now)
@router.get("/terms-policies", response_model=dict)
def get_terms():
    return {
        "terms": "Default Terms and Conditions",
        "privacy": "Default Privacy Policy",
        "agreements": "Default Institution Agreements"
    }
