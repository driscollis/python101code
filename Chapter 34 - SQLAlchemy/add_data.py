# add_data.py
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist

engine = create_engine('sqlite:///mymusic.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Create an artist
new_artist = Artist(name="Newsboys")
new_artist.albums = [Album(title="Read All About It",
                           release_date=datetime.date(1988,12,1),
                           publisher="Refuge", media_type="CD")]

# add more albums
more_albums = [Album(title="Hell Is for Wimps",
                     release_date=datetime.date(1990,7,31),
                     publisher="Star Song", media_type="CD"),
               Album(title="Love Liberty Disco",
                     release_date=datetime.date(1999,11,16),
                     publisher="Sparrow", media_type="CD"),
               Album(title="Thrive",
                     release_date=datetime.date(2002,3,26),
                     publisher="Sparrow", media_type="CD")]
new_artist.albums.extend(more_albums)

# Add the record to the session object
session.add(new_artist)

# commit the record the database
session.commit()

# Add several artists
session.add_all([
    Artist(name="MXPX"),
    Artist(name="Kutless"),
    Artist(name="Thousand Foot Krutch")
])
session.commit()