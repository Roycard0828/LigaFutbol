from AccesoDatos.modelos import Partido
from Controladores.controlador_tabla_general import TablaGeneralController
from Controladores.controlador_partido import PartidosController


def actualizar_datos_equipos_en_tabla(partido: Partido):
    """ Genera informacion para los equipos con base al partido jugado y hace
        una actualizacion en base de datos."""
    equipo_local = partido.equipo_local.id
    equipo_visitante = partido.equipo_visit.id
    resultado = str(partido.resultado)
    # Validar si se le asigno resultado a un partido
    if resultado != "Sin resultado":
        goles = resultado.split(sep='-')
        goles_local = goles[0]
        goles_visitante = goles[1]
    else:
        goles_local = 0
        goles_visitante = 0

    # Crear diccionarios para estructurar la informacion
    datos_equipo_local = {'equipo_id': equipo_local,
                          'partido_ganado': 0,
                          'partido_perdido': 0,
                          'partido_empatado': 0,
                          'goles': int(goles_local),
                          'puntos': 0}
    datos_equipo_visitante = {'equipo_id': equipo_visitante,
                              'partido_ganado': 0,
                              'partido_perdido': 0,
                              'partido_empatado': 0,
                              'goles': int(goles_visitante),
                              'puntos': 0}

    if goles_local > goles_visitante:
        datos_equipo_local['partido_ganado'] = 1
        datos_equipo_local['puntos'] = 3

        datos_equipo_visitante['partido_perdido'] = 1
    elif goles_local < goles_visitante:
        datos_equipo_visitante['partido_ganado'] = 1
        datos_equipo_visitante['puntos'] = 3

        datos_equipo_local['partido_perdido'] = 1
    else:
        datos_equipo_local['puntos'] = 1
        datos_equipo_local['partido_empatado'] = 1

        datos_equipo_visitante['puntos'] = 1
        datos_equipo_visitante['partido_empatado'] = 1

    TablaGeneralController.actualizar_puntos_equipos(datos_equipo_local, datos_equipo_visitante)


def terminar_jornada(numero_jornada: int):
    """ Reune los partidos jugados por jornada y actualiza los
        datos de los equipos participantes en la tabla general
        del torneo """
    partidos = PartidosController.devolver_partido_por_numerojornada(numero_jornada)
    for partido in partidos:
        actualizar_datos_equipos_en_tabla(partido)


def iniciar_torneo():
    TablaGeneralController.registrar_equipos()

