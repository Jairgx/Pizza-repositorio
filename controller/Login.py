from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from controller.Main import Main

class Login(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("view/Login.ui",self)
        self.btnAceptar.clicked.connect(self.ingresar)
        self.btnCerrar.clicked.connect(self.cerrar)
        self.show()

    def ingresar(self):
        usuario = self.lneUsuario.text().lower()
        contraseña = self.lnePassword.text()
        if usuario == "admin" and contraseña == "admin":
            self.close()
            gui = Main(self)
            gui.show()         
        else:
            self.lblError.setText("Credenciales incorrectas")            

    def cerrar(self):
        self.close()
