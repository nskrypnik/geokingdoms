from .database import SessionFactory
from sqlalchemy.orm import Session

def get_db_session() -> Session:
    session = SessionFactory()
    try:
        yield session
    finally:
        session.close()
