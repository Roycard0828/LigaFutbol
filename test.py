"""Clase para ir probando las nuevas caracteristicas"""

from AccesoDatos import db
from AccesoDatos.fabrica_dao import DaoEquipoFactory
from Controller import controlador


def run():

    # real = Equipo("Atletico de Madrid", "XXXXXX", "Wanda")
    # dao_equipo = DaoEquipoFactory().create_entity()
    # dao_equipo.crear(real)
    # equipo_des = dao_equipo.leer(31)
    # dao_equipo.actualizar(equipo_des, "RealMadrid", "Ancelotti", "Bernabeu")
    # dao_equipo.borrar(equipo_des)
    dao = controlador.EquiposController.devolver_todos_equipos()
    lista = dao.leer_todos()
    print(len(lista))


if __name__ == '__main__':
    db.base.metadata.create_all(db.connection)
    run()
