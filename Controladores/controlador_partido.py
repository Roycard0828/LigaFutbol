""" Esta clase es un intermediario entre la capa de Presentacion y LogicaNegocio
    con la cama de AccesoDatos para los Partidos"""

from AccesoDatos.fabrica_dao import DaoPartidoFactory
from AccesoDatos.modelos import Partido


class PartidosController:

    @classmethod
    def insertar_partido(cls, numero_jornada, id_equipo_local, id_equipo_visit, campo):
        partido = Partido(numero_jornada, id_equipo_local, id_equipo_visit, campo)
        dao = DaoPartidoFactory.create_entity()
        dao.guardar(partido)

    @classmethod
    def devolver_todos_partidos(cls):
        dao = DaoPartidoFactory.create_entity()
        lista_partidos = list(dao.leer_todos())
        return lista_partidos

    @classmethod
    def devolver_partido_por_numerojornada(cls, numerojornada):
        dao = DaoPartidoFactory.create_entity()
        lista_partidos = list(dao.leer_por_jornada(numerojornada))
        return lista_partidos

    @classmethod
    def actualizar_resultados(cls, id: int, resultado: str):
        dao = DaoPartidoFactory.create_entity()
        dao.actualizar_resultado(id, resultado)

    @classmethod
    def devolver_un_partido(cls, id: int):
        dao = DaoPartidoFactory.create_entity()
        consulta = dao.leer(id)
        return consulta
