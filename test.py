"""Clase para ir probando las nuevas caracteristicas"""

from AccesoDatos import db
# from AccesoDatos.fabrica_dao import DaoEquipoFactory, DaoPartidoFactory
# from AccesoDatos.modelos import Partido
# from Controladores import controlador_equipo
from LogicaNegocio.jornadas import generar_calendario


def run():


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
    # dao_partido.guardar(partido)
    # partido = dao_partido.leer(2)
    # print(partido.equipo_local.nombre)
    generar_calendario()


if __name__ == '__main__':
    db.base.metadata.create_all(db.connection)
    run()
