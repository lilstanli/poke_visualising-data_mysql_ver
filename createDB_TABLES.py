from flask import Flask, jsonify, render_template
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Text, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base

import mysql.connector
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

import pandas as pd
import numpy as np

import re


# Saved password in config file which will be gitignored
from config import pw

protocol = 'mysql+pymysql'
username = 'root'
password = pw
host = 'localhost'
port = 3306
database_name = 'pandachams_db2'
rds_connection_string = f'{protocol}://{username}:{password}@{host}:{port}/{database_name}'
engine = create_engine(rds_connection_string)

Base = declarative_base()

# # reflect an existing database into a new model
# Base = automap_base()

# # reflect the tables
# Base.prepare(autoload_with=engine)

# # Save reference to the tables
# poke = Base.classes.poke
# gr_species_table = Base.classes.growth_rate_species
# gr_levels_table = Base.classes.growth_rate_levels

# Creating poke table
class poke(Base):
    extend_existing=True
    __tablename__ = "poke"
    
    poke_id = Column("poke_id", Integer, primary_key = True)
    name = Column("name", String(200))
    height = Column("height", Integer)
    weight = Column("weight", Integer)
    male_rate = Column("male_rate", Float)
    female_rate = Column("female_rate", Float)
    gender_neutral_rate = Column("gender_neutral_rate", Integer)
    type_1 = Column("type_1", String(200))
    type_2 = Column("type_2", String(200))
    color = Column("color", String(200))
    shape = Column("shape", String(200))
    growth_rate = Column("growth_rate", String(200))
    base_hp = Column("base_hp", Integer)
    base_attack = Column("base_attack", Integer)
    base_def = Column("base_def", Integer)
    base_sp_attack = Column("base_sp_attack", Integer)
    base_sp_def = Column("base_sp_def", Integer)
    base_speed = Column("base_speed", Integer)
    evolves_from = Column("evolves_from", String(200))
    habitat = Column("habitat", String(200))
    catch_rate = Column("catch_rate", Integer)
    is_baby = Column("is_baby", Boolean)
    is_legendary = Column("is_legendary", Boolean)
    is_mythical = Column("is_mythical", Boolean)
    standard_pic = Column("standard_pic", String(200))
    shiny_pic = Column("shiny_pic", String(200))

