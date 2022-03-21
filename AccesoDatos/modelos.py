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

