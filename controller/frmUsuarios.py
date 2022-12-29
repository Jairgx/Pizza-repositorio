from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from model.ColeccionUsuarios import ColeccionUsuarios
from entity.Usuarios import Usuarios

objColeccionUsuarios = ColeccionUsuarios()

class frmUsuarios(QMainWindow):
    def __init__(self,parent=None):
        super(frmUsuarios,self).__init__(parent)
        uic.loadUi("view/Usuarios.ui",self)
        self.btnGrabar.clicked.connect(self.grabar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.tblUsuarios.itemClicked.connect(self.mostrar)
        self.tblUsuarios.verticalHeader().setVisible(False)
        self.listar()
 
    def grabar(self):
        codigo = self.lneCodigo.text()
        nombre = self.lneNombre.text()
        apellido = self.lneApellido.text()
        dni = self.lneDNI.text()
        telefono = self.lneTelefono.text()

        objUsuarios = Usuarios(codigo,nombre,apellido,dni,telefono)
        posicion = objColeccionUsuarios.buscar(codigo)
        if posicion==-1:
            objColeccionUsuarios.agregar(objUsuarios)
        else:
            objColeccionUsuarios.modificar(objUsuarios,posicion)

        self.listar()
        self.limpiar()

    def listar(self):
        self.tblUsuarios.setRowCount(objColeccionUsuarios.longitud())
        for i in range(objColeccionUsuarios.longitud()):
            self.tblUsuarios.setItem(i,0,QTableWidgetItem(objColeccionUsuarios.obtener(i).codigo))
            self.tblUsuarios.setItem(i,1,QTableWidgetItem(objColeccionUsuarios.obtener(i).nombre))
            self.tblUsuarios.setItem(i,2,QTableWidgetItem(objColeccionUsuarios.obtener(i).apellido))
            self.tblUsuarios.setItem(i,3,QTableWidgetItem(objColeccionUsuarios.obtener(i).dni))
            self.tblUsuarios.setItem(i,4,QTableWidgetItem(objColeccionUsuarios.obtener(i).telefono))

    def limpiar(self):
        self.lneCodigo.setText("")
        self.lneNombre.setText("")
        self.lneApellido.setText("")
        self.lneDNI.setText("")
        self.lneTelefono.setText("")

    def mostrar(self):
        filas = self.tblUsuarios.selectedItems()
        indiceFila = filas[0].row()
        codigo = self.tblUsuarios.item(indiceFila,0).text()
        nombre = self.tblUsuarios.item(indiceFila,1).text()
        apellido = self.tblUsuarios.item(indiceFila,2).text()
        dni = self.tblUsuarios.item(indiceFila,3).text()
        telefono = self.tblUsuarios.item(indiceFila,4).text()
        self.lneCodigo.setText(codigo)
        self.lneNombre.setText(nombre)
        self.lneApellido.setText(apellido)
        self.lneDNI.setText(dni)
        self.lneTelefono.setText(telefono)

    def eliminar(self):
        rpta = QMessageBox.question(self,"Eliminar Usuario","¿Está seguro que desea eliminar el usuario?",QMessageBox.Ok|QMessageBox.Cancel)
        if rpta==QMessageBox.Ok:
            filas = self.tblUsuarios.selectedItems()
            indiceFila = filas[0].row()
            codigo = self.tblUsuarios.item(indiceFila,0).text()
            posicion = objColeccionUsuarios.buscar(codigo)
            objColeccionUsuarios.eliminar(posicion)
            self.tblUsuarios.clearContents()
            self.tblUsuarios.setRowCount(0)
            self.listar()
            self.limpiar()