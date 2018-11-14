# table_def.py
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///mymusic.db', echo=True)
Base = declarative_base()

class Artist(Base):
    """"""
    __tablename__ = "artists"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    class Album(Base):
        """"""
        __tablename__ = "albums"
        
        id = Column(Integer, primary_key=True)
        title = Column(String)
        release_date = Column(Date)
        publisher = Column(String)
        media_type = Column(String)
        
        artist_id = Column(Integer, ForeignKey("artists.id"))
        artist = relationship("Artist", backref=backref("albums", order_by=id))
        
# create tables
Base.metadata.create_all(engine)