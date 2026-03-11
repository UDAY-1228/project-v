from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_all():
    return {"message": "GET all for lms"}

@router.get("/{id}")
def get_by_id(id: str):
    return {"message": f"GET lms with id {id}"}
