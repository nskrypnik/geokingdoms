from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.dtos.kingdom import KingdomCreate, KingdomUpdate
from api.models.kingdom import Kingdom
from api.utils.dependency import get_db_session

HTTP_404_MESSAGE = "Sir, this Kingdom is not found, perhaps you have to search the other universe"

kingdom_router = APIRouter()

@kingdom_router.post("/kingdoms/")
async def create_kingdom(kingdom: KingdomCreate, db_session: Session = Depends(get_db_session)):
    """
        Create new kingdom
    """
    new_kingdom = Kingdom(
        name=kingdom.name,
        king=kingdom.king,
        description=kingdom.description,
        territory=kingdom.territory.json()
    )

    db_session.add(new_kingdom)
    db_session.commit()
    db_session.refresh(new_kingdom)
    return new_kingdom

@kingdom_router.get("/kingdoms/{kingdom_id}")
async def read_kingdom(kingdom_id: int, db_session: Session = Depends(get_db_session)):
    """
        Return information about a kingdom with given id
    """
    kingdom = db_session.query(Kingdom).filter(Kingdom.id == kingdom_id).first()
    if kingdom is None:
        raise HTTPException(
            status_code=404,
            detail=HTTP_404_MESSAGE)
    return kingdom

@kingdom_router.get("/kingdoms/")
async def get_kingdoms(db_session: Session = Depends(get_db_session)):
    """
        Show all the kingdoms in the known universe
    """
    return db_session.query(Kingdom).all()

@kingdom_router.put("/kingdoms/{kingdom_id}")
async def update_kingdom(kingdom_id: int, updated: KingdomUpdate, db_session: Session = Depends(get_db_session)):
    """
        Update kingdom information of a kingdom with given id
    """
    kingdom = db_session.query(Kingdom).filter(Kingdom.id == kingdom_id).first()
    if kingdom is None:
        raise HTTPException(
            status_code=404,
            detail=HTTP_404_MESSAGE)
    
    kingdom.name = updated.name or kingdom.name
    kingdom.description = updated.description or kingdom.description
    kingdom.king = updated.king or kingdom.king
    kingdom.territory = updated.territory.json() if updated.territory else kingdom.territory

    db_session.commit()
    db_session.refresh(kingdom)

    return kingdom
