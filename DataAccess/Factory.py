"""Este archivo implementa el patron factory.
    El producto esta en el archivo DaoGeneral y el producto concreto en DaoEquipo."""

from abc import ABC, abstractmethod
from DaoEquipos import DaoEquipo
from DaoGeneral import DaoGeneral


class EntityFactory(ABC):
    """La clase EntityFactory sera la clase creadora."""

    @abstractmethod
    def create_entity(self) -> DaoGeneral:
        pass


class DaoEquipoFactory(EntityFactory):
    """Esta clase sera el creador concreto de equipos."""

    def create_entity(self) -> DaoEquipo:
        return DaoEquipo()
