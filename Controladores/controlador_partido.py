""" Esta clase es un intermediario entre la capa de Presentacion y LogicaNegocio
    con la cama de AccesoDatos para los Partidos"""

from AccesoDatos.fabrica_dao import DaoPartidoFactory
from AccesoDatos.modelos import Partido


class PartidosController:

    @classmethod
    def insertar_partido(cls, numero_jornada, id_equipo_local, id_equipo_visit, campo):
        equipo = Partido(numero_jornada, id_equipo_local, id_equipo_visit, campo)
        dao = DaoPartidoFactory.create_entity()
        dao.guardar()

    @classmethod
    def devolver_todos_partidos(cls):
        dao = DaoPartidoFactory.create_entity()
        lista_partidos = list(dao.leer_todos())
        return lista_partidos
