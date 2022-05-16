from .modelos import TablaGeneral, Equipo
from .dao_general import DaoGeneral
from .db import session


class DaoTablaGeneral:

    def __init__(self):
        self.session = session

    def guardar(self, equipo_tabla: TablaGeneral):
        self.session.add(equipo_tabla)
        self.session.commit()
        return True

    def leer_todos(self):
        consulta = self.session.query(TablaGeneral).order_by(TablaGeneral.puntos.asc())
        return consulta

    def leer_equipo(self, id_equipo_tabla):
        consulta = self.session.query(TablaGeneral).filter(
            TablaGeneral.equipo_id == id_equipo_tabla
        )
        return consulta
