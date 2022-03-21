"""Clase para ir probando las nuevas caracteristicas"""

from AccesoDatos import db
from AccesoDatos.fabrica_dao import DaoEquipoFactory


def run():

    # real = Equipo("Atletico de Madrid", "XXXXXX", "Wanda")
    dao_equipo = DaoEquipoFactory().create_entity()
    # dao_equipo.crear(real)
    # equipo_des = dao_equipo.leer(3)
    # dao_equipo.actualizar(equipo_des, "Atletico", "Cholo", "Wanda")
    # dao_equipo.borrar(equipo_des)
    # lista = dao_equipo.leer_todos()


if __name__ == '__main__':
    db.base.metadata.create_all(db.connection)
    run()
