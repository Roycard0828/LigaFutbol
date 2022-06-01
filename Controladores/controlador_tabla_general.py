from AccesoDatos.fabrica_dao import DaoTablaGeneralFactory
from AccesoDatos.modelos import TablaGeneral
from .controlador_equipo import EquiposController


class TablaGeneralController:

    @classmethod
    def registrar_equipos(cls):
        dao_tabla_general = DaoTablaGeneralFactory.create_entity()
        lista_equipos = EquiposController.devolver_todos_equipos()
        for equipo in lista_equipos:
            equipo_en_tabla = TablaGeneral(equipo)
            dao_tabla_general.guardar(equipo_en_tabla)

    @classmethod
    def actualizar_puntos_equipos(cls, datos_equipo_local: dict, datos_equipo_visitante: dict):
        dao_tabla_general = DaoTablaGeneralFactory.create_entity()
        # Actualizar datos equipo visitante
        equipo_local = dao_tabla_general.leer_equipo(datos_equipo_local['equipo_id'])[0]
        equipo_local.partidosjugados += 1
        equipo_local.partidosganados += datos_equipo_local['partido_ganado']
        equipo_local.partidosempatados += datos_equipo_local['partido_empatado']
        equipo_local.partidosperdidos += datos_equipo_local['partido_perdido']
        equipo_local.goles += datos_equipo_local['goles']
        equipo_local.puntos += datos_equipo_local['puntos']
        dao_tabla_general.actualizar_datos_equipo(equipo_local)
        # Actualizar datos equipo visitante
        equipo_visitante = dao_tabla_general.leer_equipo(datos_equipo_visitante['equipo_id'])[0]
        equipo_visitante.partidosjugados += 1
        equipo_visitante.partidosganados += datos_equipo_visitante['partido_ganado']
        equipo_visitante.partidosempatados += datos_equipo_visitante['partido_empatado']
        equipo_visitante.partidosperdidos += datos_equipo_visitante['partido_perdido']
        equipo_visitante.goles += datos_equipo_visitante['goles']
        equipo_visitante.puntos += datos_equipo_visitante['puntos']
        dao_tabla_general.actualizar_datos_equipo(equipo_visitante)

    @classmethod
    def leer_equipos(cls):
        dao_tabla_general = DaoTablaGeneralFactory.create_entity()
        lista_equipos = dao_tabla_general.leer_todos()
        return list(lista_equipos)
