from AccesoDatos.fabrica_dao import DaoTablaGeneralFactory
from AccesoDatos.modelos import TablaGeneral
from .controlador_equipo import EquiposController


class TablaGeneralController:

    @classmethod
    def registrar_equipos(cls):
        dao_tabla_general = DaoTablaGeneralFactory.create_entity()
        lista_equipos = EquiposController.devolver_todos_equipos()
        for i in range(1, lista_equipos):
            equipo = lista_equipos[i]
            equipo_en_tabla = TablaGeneral(equipo)
            dao_tabla_general.guardar(equipo_en_tabla)

    @classmethod
    def actualizar_puntos_equipos(cls, datos_equipo_local: dict, datos_equipo_visitante: dict):
        pass
