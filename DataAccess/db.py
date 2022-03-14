"""Archivo de acceso y configuracion a la base de datos con el ORM sqlalchemy y psycopg2"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

connection = create_engine('postgresql+psycopg2://rodrigogm:011128@localhost:5432/LigaFutbol')

Session = sessionmaker(bind=connection)
session = Session()

base = declarative_base()
