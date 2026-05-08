from fastapi import APIRouter
from app.models.drop import Drop
from app.services.drop import get_available_drops
from app.services.drop import get_drop

router = APIRouter()

@router.get('/drops', response_model=list[Drop])
def view_available_drops():
    return get_available_drops()

@router.get("/drops/{id}", response_model=Drop)
def view_drop(id: int):
    return get_drop(id)

