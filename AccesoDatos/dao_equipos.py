"""DaoTeam class that implement the DAO pattern.
    This class is a ConcreteProduct of the Factory pattern that is implemented
    in the factory file."""

from .modelos import Equipo
from .dao_general import DaoGeneral
from .db import session


class DaoEquipo(DaoGeneral):

    def __init__(self):
        self.session = session

    def crear(self, equipo: Equipo):
        self.session.add(equipo)
        self.session.commit()
        return True

    def leer(self, id: int):
        consulta = self.session.query(Equipo).get(id)
        return consulta

    def leer_todos(self):
        consulta = self.session.query(Equipo).all()
        return consulta;

    def actualizar(self, equipo: Equipo, *args):
        equipo = self.session.query(Equipo).get(equipo.id)
        equipo.nombre = args[0]
        equipo.representante = args[1]
        equipo.campo = args[2]

        self.session.add(equipo)
        self.session.commit()

    def borrar(self, equipo: Equipo):
        self.session.delete(equipo)
        self.session.commit()
