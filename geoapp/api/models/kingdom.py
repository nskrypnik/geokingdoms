from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB


class Kingdom(Base):
    __tablename__ = "kingdoms"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    king = Column(String)
    description = Column(String)
    territory = Column(JSONB)
