from pydantic import BaseModel
from typing import Optional

class KingdomCreate(BaseModel):
    """
        Kingdom create DTO
    """
    name: str
    king: Optional[str]
    description: Optional[str]

class KingdomUpdate(BaseModel):
    """
        Kingdom update DTO
    """
    name: Optional[str]
    king: Optional[str]
    description: Optional[str]
