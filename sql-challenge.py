from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.orm import sessionmaker, declarative_base

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "VideoGames" table
class VideoGame(base):
    __tablename__ = "VideoGame"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_year = Column(Integer)
    platforms = Column(String)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our VideoGame table
halo_combat_evolved = VideoGame(
    title = "Halo: Combat Evolved",
    release_year = 2001,
    platforms = ["Xbox", "PC", "Mac"],
)

mafia = VideoGame(
    title = "Mafia",
    release_year = 2002,
    platforms = ["Xbox", "PC", "PS2"],
)

just_cause_2 = VideoGame(
    title = "Just Cause 2",
    release_year = 2010,
    platforms = ["PC", "PS3", "Xbox360"],
)

bully = VideoGame(
    title = "Bully",
    release_year = 2006,
    platforms = ["PS2", "Wii", "PC", "Xbox360"],
)
session.add(bully)


portal = VideoGame(
    title = "Portal",
    release_year = 2007,
    platforms = ["PC","Mac","Linux","Xbox360","PS3","Switch"],
)
session.add(portal)

half_life = VideoGame(
    title = "Half-Life",
    release_year = 1998,
    platforms = ["PC","PS2","Mac","Linux"],
)
session.add(half_life)

dark_souls = VideoGame(
    title = "Dark Souls",
    release_year = 2011,
    platforms = ["PS3","Xbox360","PC","PS4","XboxOne","Switch"],
)
session.add(dark_souls)

sleeping_dogs = VideoGame(
    title = "Sleeping Dogs",
    release_year = 2012,
    platforms = ["PC","PS3","Xbox360","PS4","XboxOne","Mac"],
)
session.add(sleeping_dogs)

la_noire = VideoGame(
    title = "L.A. Noire",
    release_year = 2011,
    platforms = ["PC","PS3","Xbox360","PS4","XboxOne","Switch"],
)
session.add(la_noire)

the_getaway = VideoGame(
    title = "The Getaway",
    release_year = 2002,
    platforms = ["PS2"],
)
session.add(the_getaway)

metal_gear_solid_2 = VideoGame(
    title = "Metal Gear Solid 2: Sons of Liberty",
    release_year = 2001,
    platforms = ["PS2","Xbox","PC"],
)
session.add(metal_gear_solid_2)

#  = VideoGame(
#     title = "",
#     release_year = ,
#     platforms = [""],
# )
# session.add()

# add each instance of our VideoGames to our session
# session.add(halo_combat_evolved)
# session.add(mafia)
# session.add(just_cause_2)

# # commit our session to the database
session.commit()

# delete multiple records
# games = session.query(VideoGame)
# for game in games:
#     # session.delete(game)
#     game.id -= 3
#     session.commit()

# query the database to find all Programmers
videoGames = session.query(VideoGame)
for game in videoGames:
    print(
        game.id,
        game.release_year,
        game.platforms,
        game.title,
        sep=" | "
    )