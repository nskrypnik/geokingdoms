import os
import sys
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databases import Database
from api.models.base import Base

GEOAPP_DB_CONNECTION = "GEOAPP_DB_CONNECTION"
database_connection_url = os.getenv(GEOAPP_DB_CONNECTION)

if database_connection_url is None:
    print("GEOAPP_DB_CONNECTION env var is not set. Cannot connect to db")
    sys.exit(-1)

# create a SQLAlchemy engine
engine = create_engine(database_connection_url)

# create a session factory
SessionFactory = sessionmaker(bind=engine)

database = Database(database_connection_url)

def create_database():

    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    
    import api.models.kingdom
    # create the database tables

    Base.metadata.create_all(engine)
