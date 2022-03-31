"""Este archivo implementa el patron factory.
    El producto esta en el archivo DaoGeneral y el producto concreto en DaoEquipo."""

from abc import ABC, abstractmethod
from .dao_equipos import DaoEquipo


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
