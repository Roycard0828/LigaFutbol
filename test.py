"""Clase para ir probando las nuevas caracteristicas"""

from AccesoDatos import db
from AccesoDatos.fabrica_dao import DaoEquipoFactory, DaoPartidoFactory, DaoTablaGeneralFactory
from AccesoDatos.modelos import Partido, TablaGeneral
# from Controladores import controlador_equipo
# from LogicaNegocio.jornadas import generar_calendario


def run():
    pass
    # real = Equipo("Atletico de Madrid", "XXXXXX", "Wanda")
    # dao_equipo = DaoEquipoFactory().create_entity()
    # dao_equipo.crear(real)
    # equipo_local = dao_equipo.leer(1)
    # equipo_visitante = dao_equipo.leer(2)
    # dao_equipo.actualizar(equipo_des, "RealMadrid", "Ancelotti", "Bernabeu")
    # dao_equipo.borrar(equipo_des)
    # dao = controlador.EquiposController.devolver_todos_equipos()
    # lista = dao.leer_todos()
    # partido = Partido(1, equipo_local.id, equipo_visitante.id , "Bernabeu")
    # dao_partido = DaoPartidoFactory().create_entity()
    # consulta = dao_partido.leer_por_jornada(1)
    # print(consulta[0].equipo_local.nombre)
    # dao_partido.guardar(partido)
    # partido = dao_partido.leer(2)
    # print(partido.equipo_local.nombre)
    # generar_calendario()
    # dao_tabla = DaoTablaGeneralFactory.create_entity()
    # consulta = dao_tabla.leer_equipo(1)
    # print(consulta[0].equipo.nombre)


if __name__ == '__main__':
    db.base.metadata.create_all(db.connection)
    run()
