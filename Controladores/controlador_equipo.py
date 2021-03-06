""" Esta clase es un intermediario entre la capa de Presentacion y LogicaNegocio
    con la cama de AccesoDatos"""
from AccesoDatos.fabrica_dao import DaoEquipoFactory
from AccesoDatos.modelos import Equipo


class EquiposController:
    """Clase encargada de conectar la capa de Presentacion con la capa de acceso a datos"""

    @classmethod
    def insertar_equipos(cls, nombre, representante, campo):
        dao = DaoEquipoFactory.create_entity()
        equipo = Equipo(nombre, representante, campo)
        dao.guardar(equipo)

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
        nombre = args[0]
        representante = args[1]
        campo = args[2]
        if equipo is not None:
            dao.actualizar(equipo, nombre, representante, campo)
            return True
        else:
            return False

    @classmethod
    def devolver_todos_equipos(cls):
        dao = DaoEquipoFactory.create_entity()
        lista_equipos = list(dao.leer_todos())
        return lista_equipos
