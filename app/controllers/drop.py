from fastapi import APIRouter
from app.models.drop import DropIn, DropOut, DropCreateResponse
from app.services.drop import read_all_drops, read_drop, create_new_drop

router = APIRouter(
    prefix="/drops",
    tags=["Drops"]
)

@router.get('/', response_model=list[DropOut])
def read_all_drops():
    return read_all_drops()

@router.get("/{id}", response_model=DropOut)
def view_drop(id: int):
    return read_drop(id)

@router.post('/', status_code=201, response_model=DropCreateResponse)
def post_new_drop(drop: DropIn) -> DropOut:
	return create_new_drop(drop)