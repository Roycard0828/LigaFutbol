from AccesoDatos.modelos import Partido


def generar_informacion_por_partido(partido: Partido):
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
                          'goles': goles_local,
                          'puntos': 0}
    datos_equipo_visitante = {'equipo_id': equipo_visitante,
                              'partido_ganado': 0,
                              'partido_perdido': 0,
                              'partido_empatado': 0,
                              'goles': goles_visitante,
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

    lista_resultados = [datos_equipo_local, datos_equipo_visitante]
    return lista_resultados

