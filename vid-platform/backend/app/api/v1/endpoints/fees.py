from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_all():
    return {"message": "GET all for fees"}

@router.get("/{id}")
def get_by_id(id: str):
    return {"message": f"GET fees with id {id}"}
