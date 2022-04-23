from Presentacion.ventana_principal import *
from Presentacion.ventana_actualizar import *
from Presentacion.mensaje_exitoso import *
from Controladores.controlador_equipo import EquiposController
from Controladores.controlador_partido import PartidosController
from PyQt5 import Qt


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.widget = QtWidgets.QMainWindow()

        # ------Selecccionar paginas del 'StachWidget' segun los botones -----------
        self.BtnEquipo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PaginaEquipos))
        self.BtnTabla.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PaginaTabla))
        self.BtnJornada.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PaginaJornada))

        # ------ Botones para los equipos equipos --------
        self.BtnInsertar.clicked.connect(lambda: self.insertar_datos_equipos())
        self.BtnActualizar.clicked.connect(lambda: self.actualizar_datos_equipos())
        self.btnlistar.clicked.connect(lambda: self.cargar_tabla_equipos())
        self.BtnBorrar.clicked.connect(lambda: self.borrar_equipos())

        # Botones para los partidos
        self.BtnBuscarJornada.clicked.connect(lambda: self.cargar_tabla_partidos())
        self.BtnAsignarResultado.clicked.connect(lambda: self.asignar_resultados())
        self.BtnActualizarDatos.clicked.connect(lambda: self.actualizar_resultados())

    # Metodos generales
    def boton_mensaje_exitoso(self):
        self.mensaje_exitoso = Ui_Dialog()
        self.mensaje_exitoso.setupUi(self.widget)
        self.widget.show()
        self.mensaje_exitoso.pushButton.clicked.connect(lambda: self.widget.close())

    # Metodos para las operaciones con los equipos
    def insertar_datos_equipos(self):
        nombre = str(self.TxtNombreEquipo.toPlainText())
        representante = str(self.TxtRepresentanteEquipo.toPlainText())
        campo = str(self.TxtCampoEquipo.toPlainText())

        EquiposController.insertar_equipos(nombre, representante, campo)
        self.boton_mensaje_exitoso()

    def borrar_equipos(self):
        id = int(self.tablaEquipos.currentItem().text())
        EquiposController.borrar_equipos(id)
        self.boton_mensaje_exitoso()

    def actualizar_datos_equipos(self):
        # Actualizar eqipos seleccionando la columna ID
        id = int(self.tablaEquipos.currentItem().text())
        self.actualizar_widget = Ui_ActualizarWIndow()
        self.actualizar_widget.setupUi(self.widget)
        self.widget.show()

        def definir_datos():
            nombre = str(self.actualizar_widget.TxtNombre.toPlainText())
            representante = str(self.actualizar_widget.TxtRepresentante.toPlainText())
            campo = str(self.actualizar_widget.TxtCampo.toPlainText())

            EquiposController.actualizar_equipos(id, nombre, representante, campo)
            self.widget.close()

        self.actualizar_widget.BtnAceptar.clicked.connect(lambda: definir_datos())

    def cargar_tabla_equipos(self):
        equipos = EquiposController.devolver_todos_equipos()
        self.tablaEquipos.setRowCount(len(equipos))
        for i in range(0, len(equipos)):
            row = i
            id = str(equipos[i].id)
            self.tablaEquipos.setItem(row, 0, QtWidgets.QTableWidgetItem(id))
            self.tablaEquipos.setItem(row, 1, QtWidgets.QTableWidgetItem(equipos[i].nombre))
            self.tablaEquipos.setItem(row, 2, QtWidgets.QTableWidgetItem(equipos[i].representante))
            self.tablaEquipos.setItem(row, 3, QtWidgets.QTableWidgetItem(equipos[i].campo))

        self.tablaEquipos.sortItems(0)

    # Metodos para las operaciones con los partidos
    def cargar_tabla_partidos(self):
        numerojornada = int(self.NumJornada.text())
        lista_partidos = PartidosController.devolver_partido_por_numerojornada(numerojornada)
        self.TablaPartidos.setRowCount(len(lista_partidos))
        for i in range(0, len(lista_partidos)):
            self.TablaPartidos.setItem(i, 0, QtWidgets.QTableWidgetItem(lista_partidos[i].equipo_local.nombre))
            self.TablaPartidos.setItem(i, 1, QtWidgets.QTableWidgetItem(lista_partidos[i].equipo_visit.nombre))
            self.TablaPartidos.setItem(i, 2, QtWidgets.QTableWidgetItem(lista_partidos[i].campo))
            self.TablaPartidos.setItem(i, 3, QtWidgets.QTableWidgetItem(lista_partidos[i].resultado))

    def asignar_resultados(self):
        resultado = self.TxtResultado.toPlainText()
        self.TablaPartidos.currentItem().setText(resultado)

    def actualizar_resultados(self):
        # Actualizar el resultado de los partidos segun su id y el resultado asignado
        numero_jornada = int(self.NumJornada.text())
        lista_partidos = PartidosController.devolver_partido_por_numerojornada(numero_jornada)
        numero_partidos = len(lista_partidos)
        for i in range(0, numero_partidos):
            id = lista_partidos[i].id
            resultado = self.TablaPartidos.item(i, 3).text()
            PartidosController.actualizar_resultados(id, resultado)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
