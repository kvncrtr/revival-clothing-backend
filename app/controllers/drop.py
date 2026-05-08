from fastapi import APIRouter
from app.models.drop import DropIn, DropOut, DropCreateResponse
from app.services.drop import get_available_drops, get_drop, create_new_drop

router = APIRouter()

@router.get('/drops', response_model=list[DropOut])
def view_available_drops():
    return get_available_drops()

@router.get("/drops/{id}", response_model=DropOut)
def view_drop(id: int):
    return get_drop(id)

@router.post('/drops', status_code=201, response_model=DropCreateResponse)
def post_new_drop(drop: DropIn) -> DropOut:
	return create_new_drop(drop)