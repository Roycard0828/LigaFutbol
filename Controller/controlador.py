from AccesoDatos.fabrica_dao import DaoEquipoFactory
from AccesoDatos.modelos import Equipo


def insertar_equipos(nombre, representante, campo):
    dao = DaoEquipoFactory().create_entity()
    equipo = Equipo(nombre, representante, campo)
    dao.crear(equipo)
