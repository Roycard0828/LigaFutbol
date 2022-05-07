from AccesoDatos.modelos import Partido


def generar_informacion_por_partido(partido: Partido):
    equipo_local = partido.equipo_local.id
    equipo_visitante = partido.equipo_visit.id
    resultado = partido.resultado
    goles = resultado.split(sep='-')
    goles_local = goles[0]
    goles_visitante = goles[1]

