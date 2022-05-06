"""Archivo pora general el calendario de jornadas segun los equipos inscritos"""""

from Controladores.controlador_equipo import EquiposController
from Controladores.controlador_partido import PartidosController
from AccesoDatos.modelos import Partido

lista_equipos = EquiposController.devolver_todos_equipos()


def generar_calendario():

    lista_uno = []
    lista_dos = []
    total_equipos = len(lista_equipos)
    numero_jornadas = 0
    jornadas = []

    # EL numero de Jornadas es '(n-1)' para un numero de equipos par y '(n)' para un numero impar
    if total_equipos % 2 == 0:
        mitad = int(total_equipos/2)
        lista_uno = lista_equipos[0:mitad]
        lista_dos = lista_equipos[mitad:total_equipos]
        lista_dos = list(lista_dos + [0])  # Lugar para poder rotar los equipos.
        numero_jornadas = total_equipos - 1
        contador_jornada = 1

        for i in range(0, numero_jornadas):
            for j in range(0, mitad):
                local = None
                visitante = None
                if contador_jornada % 2 == 0:
                    local = lista_uno[j]
                    visitante = lista_dos[j]
                else:
                    local = lista_dos[j]
                    visitante = lista_uno[j]
                PartidosController.insertar_partido(contador_jornada, local.id, visitante.id, local.campo)

            # Rotar equipos
            lista_dos[-1] = lista_uno[-1]
            for a in range(len(lista_uno) - 2, 0, -1):
                lista_uno[a+1] = lista_uno[a]

            lista_uno[1] = lista_dos[0]

            for b in range(len(lista_dos) - 1):
                lista_dos[b] = lista_dos[b+1]

            contador_jornada += 1
    else:
        mitad = int((total_equipos-1)/2)
        lista_uno = lista_equipos[0:mitad+1]
        lista_dos = lista_equipos[mitad+1:total_equipos]
        # lista_dos = list(lista_dos + [0])
        equipo_descanso = None  # Un equipo va a descansar cada Jornada.
        numero_jornadas = total_equipos
        contador_jornada = 1

        for i in range(numero_jornadas):
            equipo_descanso = lista_uno[-1]
            for j in range(0, mitad):
                local = None
                visitante = None
                if contador_jornada % 2 == 0:
                    local = lista_uno[j]
                    visitante = lista_dos[j]
                else:
                    local = lista_dos[j]
                    visitante = lista_uno[j]
                PartidosController.insertar_partido(contador_jornada, local.id, visitante.id, local.campo)

            # Rotar equipos.
            for a in range(len(lista_uno) - 2, -1, -1):  # Hasta -1 para que pueda llegar al valor 0.
                lista_uno[a + 1] = lista_uno[a]

            lista_uno[0] = lista_dos[0]

            for b in range(0, len(lista_dos) - 1):
                lista_dos[b] = lista_dos[b + 1]

            lista_dos[-1] = equipo_descanso  # Sacar al equipo del descanso.

            contador_jornada += 1

