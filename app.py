from Presentacion.ventana_principal import *
from Presentacion.ventana_actualizar import *
from Controller.controlador import EquiposController


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # ------Selecccionar paginas del 'StachWidget' segun los botones -----------
        self.BtnEquipo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PaginaEquipos))
        self.BtnTabla.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PaginaTabla))

        # ------ Metodos de equipos --------
        self.BtnInsertar.clicked.connect(lambda: self.insertar_datos_equipos())
        self.BtnActualizar.clicked.connect(lambda: self.actualizar_datos_equipos())

    def insertar_datos_equipos(self):
        nombre = str(self.TxtNombreEquipo.toPlainText())
        representante = str(self.TxtRepresentanteEquipo.toPlainText())
        campo = str(self.TxtCampoEquipo.toPlainText())

        EquiposController.insertar_equipos(nombre, representante, campo)

    def borrar_datos_equipos(self):
        id = 0  # Recopilar el id de la tabla
        EquiposController.borrar_equipos(id)

    def actualizar_datos_equipos(self):
        id = 31  # Dato recopilado de la tabla
        self.widget = QtWidgets.QMainWindow()
        self.actualizar_widget = Ui_ActualizarWIndow()
        self.actualizar_widget.setupUi(self.widget)
        self.widget.show()

        def definir_datos():
            nombre = str(self.actualizar_widget.TxtNombre.toPlainText())
            representante = str(self.actualizar_widget.TxtRepresentante.toPlainText())
            campo = str(self.actualizar_widget.TxtCampo.toPlainText())

            EquiposController.actualizar_equipos(id, nombre, representante, campo)

        self.actualizar_widget.BtnAceptar.clicked.connect(lambda: definir_datos())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
