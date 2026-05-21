from fastapi import APIRouter, Depends
from app.database.db import get_db
from sqlalchemy.orm import Session

from app.models.drop import DropCreate, DropOut, DropCreateResponse
from app.services import drop as drop_service

router = APIRouter(
    prefix="/drops",
    tags=["Drops"]
)

@router.get("", response_model=list[DropOut])
def get_all_drops(db: Session = Depends(get_db)):
    return drop_service.read_all_drops(db)

@router.get("/{id}", response_model=DropOut)
def get_drop(id: int):
    return drop_service.read_drop(id)

@router.post("", status_code=201, response_model=DropCreateResponse)
def post_new_drop(drop: DropCreate) -> DropOut:
	return drop_service.create_new_drop(drop)