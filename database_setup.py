import sys

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class FlashRecord(Base):
    __tablename__ = 'flash_record'

    date = Column(
        String,
        primary_key = True
    )
    times = Column(
        Integer,
        default = 0
    )

###################end#of#file###################

engine = create_engine('sqlite:///flash_record.db')
Base.metadata.create_all(engine)