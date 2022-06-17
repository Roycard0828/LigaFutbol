"""Clase abstracta DaoGeneral."""

from abc import ABC, abstractmethod


class DaoGeneral(ABC):
    """DaoGeneral trabaja como una clase abstracta que sera heredada por clases concretas para cada entidad.
        Esta clase es un Producto del patron factory implementado en el archivo Fabrica.py."""

    @abstractmethod
    def guardar(self, pojo):
        pass

    @abstractmethod
    def leer(self, id: int):
        pass

    @abstractmethod
    def leer_todos(self):
        pass

    @abstractmethod
    def actualizar(self, id: int, *args):
        pass

    @abstractmethod
    def borrar(self, pojo):
        pass
