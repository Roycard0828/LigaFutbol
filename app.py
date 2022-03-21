from Presentacion.ventana_principal import *
from Controller import controlador


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # ------Selecccionar paginas del 'StachWidget' segun los botones -----------
        self.BtnEquipo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PaginaEquipos))
        self.BtnTabla.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PaginaTabla))

        # ------ Metodos de equipos --------
        self.BtnInsertar.clicked.connect(lambda: self.datos_equipos())

    def datos_equipos(self):
        nombre = str(self.TxtNombreEquipo.toPlainText())
        representante = str(self.TxtRepresentanteEquipo.toPlainText())
        campo = str(self.TxtCampoEquipo.toPlainText())

        controlador.insertar_equipos(nombre, representante, campo)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
