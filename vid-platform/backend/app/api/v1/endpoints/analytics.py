from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_all():
    return {"message": "GET all for analytics"}

@router.get("/{id}")
def get_by_id(id: str):
    return {"message": f"GET analytics with id {id}"}
