from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, FlashRecord

engine = create_engine('sqlite:///flash_record.db',connect_args = {'check_same_thread':False})
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()