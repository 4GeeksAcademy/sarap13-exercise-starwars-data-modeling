import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    id_films = Column(Integer, ForeignKey('films.id'))
    id_starships = Column(Integer, ForeignKey('starships.id'))
    id_species = Column(Integer, ForeignKey('species.id'))
    id_vehicles = Column(Integer, ForeignKey('vehicles.id'))



class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    id_people = Column(Integer, ForeignKey('people.id'))
    id_films = Column(Integer, ForeignKey('films.id'))


class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    max_atmosphering_speed = Column(String(250), nullable=False)
    cargo_capacity = Column(String(250), nullable=False)
    consumables = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    id_people = Column(Integer, ForeignKey('people.id'))
    id_films = Column(Integer, ForeignKey('films.id'))


class Species(Base):
    __tablename__ = 'species'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    classification = Column(String(250), nullable=False)
    designation = Column(String(250), nullable=False)
    average_heigth = Column(String(250), nullable=False)
    average_lifespan = Column(String(250), nullable=False)
    eye_colors = Column(String(250), nullable=False)
    hair_colors = Column(String(250), nullable=False)
    skin_colors = Column(String(250), nullable=False)
    language = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    id_people = Column(Integer, ForeignKey('people.id'))
    id_films = Column(Integer, ForeignKey('films.id'))


class Films(Base):
    __tablename__ = 'films'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    episode_id = Column(String(250), nullable=False)
    opening_crawl = Column(String(250), nullable=False)
    director = Column(String(250), nullable=False)
    producer = Column(String(250), nullable=False)
    release_date = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    id_people = Column(Integer, ForeignKey('people.id'))
    id_planets = Column(Integer, ForeignKey('planets.id'))
    id_vehicles = Column(Integer, ForeignKey('vehicles.id'))
    id_species = Column(Integer, ForeignKey('species.id'))
    id_starships = Column(Integer, ForeignKey('starships.id'))

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    starship_class = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    max_atmosphering_speed = Column(String(250), nullable=False)
    hiper_drive_rating = Column(String(250), nullable=False)
    MGLT = Column(String(250), nullable=False)
    cargo_capacity = Column(String(250), nullable=False)
    consumables = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    id_people = Column(Integer, ForeignKey('people.id'))
    id_films = Column(Integer, ForeignKey('films.id'))

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    id_people = Column(Integer, ForeignKey('people.id'))
    id_vehicles = Column(Integer, ForeignKey('vehicles.id'))
    id_species = Column(Integer, ForeignKey('species.id'))
    id_films = Column(Integer, ForeignKey('films.id'))
    id_starships = Column(Integer, ForeignKey('starships.id'))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)





    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
