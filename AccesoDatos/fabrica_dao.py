"""Este archivo implementa el patron factory.
    El producto esta en el archivo DaoGeneral y el producto concreto en DaoEquipo."""

from abc import ABC, abstractmethod
from .dao_equipos import DaoEquipo
from .dao_partidos import DaoPartido
from .dao_tabla_general import DaoTablaGeneral


class EntityFactory(ABC):
    """La clase EntityFactory sera la clase creadora."""

    @abstractmethod
    def create_entity(self):
        pass


class DaoEquipoFactory(EntityFactory):
    """Esta clase sera el creador concreto de equipos."""

    @classmethod
    def create_entity(cls) -> DaoEquipo:
        return DaoEquipo()


class DaoPartidoFactory(EntityFactory):
    """Esta clase sera el creador concreto de los partidos"""
    @classmethod
    def create_entity(cls):
        return DaoPartido()


class DaoTablaGeneralFactory():
    """Esta clase es el creador concreto de la tabla general"""
    @classmethod
    def create_entity(cls):
        return DaoTablaGeneral()
