"""Archivo para la administracion de los modelos en base de datos"""

from DataAccess.db import session, base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Equipo(base):
    # ---Atributos de la base de datos---
    __tablename__ = "equipo"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    representante = Column(String)
    campo = Column(String)
    # Relaciones
    tablageneral = relationship('TablaGeneral', backref='equipo')

    def __init__(self, nombre, representante, campo):
        self.nombre = nombre
        self.representante = representante
        self.campo = campo


class Partido(base):
    # ---Atributos de la base de datos---
    __tablename__ = 'partido'
    id = Column(Integer, primary_key=True)
    equipo_local_id = Column(Integer, ForeignKey('equipo.id'))
    equipo_visit_id = Column(Integer, ForeignKey('equipo.id'))
    resultado = Column(String, default="Sin resultado")
    # Relaciones
    equipo_local = relationship('Equipo', foreign_keys=[equipo_local_id])
    equipo_visit = relationship('Equipo', foreign_keys=[equipo_visit_id])
    jornada = relationship('Jornadas', backref='partido')

    def __init__(self, equipo_local, equipo_visit):
        self.equipo_local = equipo_local
        self.equipo_visit = equipo_visit

    @property
    def resultado(self):
        return self.resultado

    @resultado.setter
    def resultado(self, resultado: String):
        self.resultado = resultado


class Jornadas(base):
    # ---Atributos de la base de datos---
    __tablename__ = 'jornadas'
    id = Column(Integer, primary_key=True)
    partido_id = Column(Integer, ForeignKey('partido.id'))


class TablaGeneral(base):
    # ---Atributos de la basde de datos---
    __tablename__ = 'tablageneral'
    equipo_id = Column(Integer, ForeignKey('equipo.id'))
    numero_juegos = Column(Integer, default=0)
    juegos_ganados = Column(Integer, default=0)
    juegos_perdidos = Column(Integer, default=0)
    juegos_empatados = Column(Integer, default=0)
    numero_goles = Column(Integer, default=0)
    numero_puntos = Column(Integer, default=0)

