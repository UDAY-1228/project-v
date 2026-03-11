from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_all():
    return {"message": "GET all for audit"}

@router.get("/{id}")
def get_by_id(id: str):
    return {"message": f"GET audit with id {id}"}
