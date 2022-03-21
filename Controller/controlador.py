""" Esta clase es un intermediario entre la capa de Presentacion y LogicaNegocio
    con la cama de AccesoDatos"""
from AccesoDatos.fabrica_dao import DaoEquipoFactory
from AccesoDatos.modelos import Equipo


class EquiposController:

    @classmethod
    def insertar_equipos(cls, nombre, representante, campo):
        dao = DaoEquipoFactory.create_entity()
        equipo = Equipo(nombre, representante, campo)
        dao.crear(equipo)

    @classmethod
    def borrar_equipos(cls, id):
        """Metodo para borrar equipos buscandolos antes"""
        dao = DaoEquipoFactory.create_entity()
        equipo = dao.leer(id)
        if equipo is not None:
            dao.borrar(equipo)
            return True
        else:
            return False

    @classmethod
    def actualizar_equipos(cls, id, *args):
        """Metodo para actualizar equipos buscandolos antes"""
        dao = DaoEquipoFactory.create_entity()
        equipo = dao.leer(id)
        datos = args
        if equipo is not None:
            dao.actualizar(equipo, datos)
            return True
        else:
            return False
