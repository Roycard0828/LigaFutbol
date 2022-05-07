"""Archivo para la administracion de los modelos en base de datos"""

from AccesoDatos.db import session, base
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
    # tablageneral = relationship('TablaGeneral', backref='equipo')

    def __init__(self, nombre, representante, campo):
        self.nombre = nombre
        self.representante = representante
        self.campo = campo


class Partido(base):
    __tablename__ = "partido"
    id = Column(Integer, primary_key=True)
    numerojornada = Column(Integer)
    equipo_local_id = Column(Integer, ForeignKey('equipo.id'))
    equipo_visit_id = Column(Integer, ForeignKey('equipo.id'))
    campo = Column(String)
    resultado = Column(String, default="Sin resultado")
    # Relaciones
    equipo_local = relationship('Equipo', foreign_keys=[equipo_local_id])
    equipo_visit = relationship('Equipo', foreign_keys=[equipo_visit_id])

    def __init__(self, numerojornada, equipo_local_id: int, equipo_visitante_id: int, campo):
        self.numerojornada = numerojornada
        self.equipo_local_id = equipo_local_id
        self.equipo_visit_id = equipo_visitante_id
        self.campo = campo


class TablaGeneral(base):
    __tablename__ = "tablageneral"
    id = Column(Integer, primary_key=True)
    equipo_id = Column(Integer, ForeignKey('equipo.id'))
    partidosjugados = Column(Integer, default=0)
    partidosganados = Column(Integer, default=0)
    partidosperdidos = Column(Integer, default=0)
    goles = Column(Integer, default=0)
    puntos = Column(Integer, default=0)
    # Relaciones
    equipo = relationship('Equipo')

    def __init__(self, equipo_id):
        self.equipo_id = equipo_id
