from pydantic import BaseModel
from pydantic_geojson import PolygonModel
from typing import Optional

class KingdomCreate(BaseModel):
    """
        Kingdom create DTO
    """
    name: str
    king: Optional[str]
    description: Optional[str]
    territory: PolygonModel

class KingdomUpdate(BaseModel):
    """
        Kingdom update DTO
    """
    name: Optional[str]
    king: Optional[str]
    description: Optional[str]
    territory: Optional[PolygonModel]
