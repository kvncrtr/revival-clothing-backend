from app.models.drop import Drop

drops = [
    Drop(
        id=1,
        name='Easter Collection Tee',
        status='available',
        price=39.99
    ),
    Drop(
        id=2,
        name='Revival Hoodie',
        status='available',
        price=79.99
    ),
    Drop(
        id=3,
        name='Summer Faith Drop',
        status='coming_soon',
        price=49.99
    )
]

def get_available_drops() -> list[Drop]:
    available_drops = []

    for drop in drops:
        if drop.status == 'available':
            available_drops.append(drop)

    return available_drops

def get_drop(id: int) -> Drop:
    for drop in drops:
        if drop.id == id:
            return drop