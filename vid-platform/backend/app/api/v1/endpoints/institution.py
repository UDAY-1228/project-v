from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_all():
    return {"message": "GET all for institution"}

@router.get("/{id}")
def get_by_id(id: str):
    return {"message": f"GET institution with id {id}"}
