from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from controller.frmEmpleados import frmEmpleados
from controller.frmVentas import frmVentas
from controller.frmUsuarios import frmUsuarios

class Main(QMainWindow):
    def __init__(self,parent = None):
        super(Main,self).__init__(parent)
        uic.loadUi("view/Main.ui",self)
        self.mnuEmpleados.triggered.connect(self.abrirEmpleados)
        self.mnuVentas.triggered.connect(self.abrirVentas)
        self.mnuUsuarios.triggered.connect(self.abrirUsuarios)

    def abrirEmpleados(self):
        gui = frmEmpleados(self)
        gui.show()
 
    def abrirVentas(self):
        gui = frmVentas(self)
        gui.show()

    def abrirUsuarios(self):
        gui = frmUsuarios(self)
        gui.show()
        
        