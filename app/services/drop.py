from datetime import datetime
from fastapi import HTTPException, Depends

from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.models.drop import Base, Drop, DropIn, DropCreateResponse

def read_all_drops(db: Session):
    try:
        stmt = text("""
            SELECT * FROM drops;
        """)
        
        result = db.execute(stmt)
        drops = result.mappings.all()
        
        return drops 
    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Database error while reading drops."
        )

drops = [
    Drop(
        id=1,
        name='Easter Collection Tee',
        status='available',
        price=39.99,
        number_of_units=77,
        created_at=datetime.now(),
        team="Founding Team"
    ),
    Drop(
        id=2,
        name='Revival Hoodie',
        status='available',
        price=79.99,
        number_of_units=30,
        created_at=datetime.now(),
        team="Founding Team"
    ),
    Drop(
        id=3,
        name='Summer Faith Drop',
        status='coming_soon',
        price=49.99,
        number_of_units=178,
        created_at=datetime.now(),
        team="Founding Team"
    )
]

def create_new_drop(drop_data: DropIn) -> DropCreateResponse:
    if any(d.name == drop_data.name for d in drops):
        raise HTTPException(
            status_code=400, 
            detail="This collection currently exist in our database, Choose another name!"
        )
    
    new_drop = Drop(
        id=len(drops) + 1,
        name=drop_data.name,
        status=drop_data.status,
        price=drop_data.price,
        number_of_units=drop_data.number_of_units,
        created_at=datetime.now(),
        team="Founding Team"
    )

    drops.append(new_drop)

    return {
		"message": "Drop created!",
		"drop": new_drop
	}

def read_available_drops() -> list[Drop]:
    available_drops = []

    for drop in drops:
        if drop.status == 'available':
            available_drops.append(drop)

    return available_drops

def read_drop(id: int) -> Drop:
    for drop in drops:
        if drop.id == id:
            return drop