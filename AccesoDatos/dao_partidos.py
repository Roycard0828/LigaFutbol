from .modelos import Partido
from .dao_general import DaoGeneral
from .db import session


class DaoPartido(DaoGeneral):

    def __init__(self):
        self.session = session

    def guardar(self, partido: Partido):
        self.session.add(partido)
        self.session.commit()
        return True

    def leer(self, id: int):
        consulta = self.session.query(Partido).get(id)
        return consulta

    def leer_por_jornada(self, numero_jornada: int):
        consulta = self.session.query(Partido).filter(
            Partido.numerojornada == numero_jornada
        )
        return consulta

    def leer_todos(self):
        pass

    def actualizar(self, id: int, *args):
        pass

    def borrar(self, partido: Partido):
        pass
