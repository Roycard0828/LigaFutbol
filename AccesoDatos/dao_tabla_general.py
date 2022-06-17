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
        consulta = self.session.query(TablaGeneral).order_by(TablaGeneral.puntos.desc())
        return consulta

    def leer_equipo(self, id_equipo_tabla: int):
        consulta = self.session.query(TablaGeneral).filter(
            TablaGeneral.equipo_id == id_equipo_tabla
        )
        return consulta

    def actualizar_datos_equipo(self, equipo_tabla_general: TablaGeneral):
        self.session.add(equipo_tabla_general)
        self.session.commit()
        return True
