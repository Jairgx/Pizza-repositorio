from ast import alias
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from model.ColeccionEmpleados import ColeccionEmpleados
from entity.Empleados import Empleados

objColeccionEmpleados = ColeccionEmpleados()

class frmEmpleados(QMainWindow):
    def __init__(self,parent=None):
        super(frmEmpleados,self).__init__(parent)
        uic.loadUi("view/Empleados.ui",self)
        self.tblEmpleados.verticalHeader().setVisible(False)
        self.btnGrabar.clicked.connect(self.grabar)
        self.tblEmpleados.itemClicked.connect(self.mostrar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.listar()

    def grabar(self):
        codigo = self.lneCodigo.text()
        nombre = self.lneNombre.text()
        apellido = self.lneApellido.text()
        area = self.lneArea.text()
    
        objEmpleado = Empleados(codigo,nombre,apellido,area)
        posicion = objColeccionEmpleados.buscar(codigo)
        if posicion==-1:
            objColeccionEmpleados.agregar(objEmpleado)
        else:
            objColeccionEmpleados.modificar(objEmpleado,posicion)

        self.listar()
        self.limpiar()

    def listar(self):
        self.tblEmpleados.setRowCount(objColeccionEmpleados.longitud())
        for i in range(objColeccionEmpleados.longitud()):
            self.tblEmpleados.setItem(i,0,QTableWidgetItem(objColeccionEmpleados.obtener(i).codigo))
            self.tblEmpleados.setItem(i,1,QTableWidgetItem(objColeccionEmpleados.obtener(i).nombre))
            self.tblEmpleados.setItem(i,2,QTableWidgetItem(objColeccionEmpleados.obtener(i).apellido))
            self.tblEmpleados.setItem(i,3,QTableWidgetItem(objColeccionEmpleados.obtener(i).area))
            
            
    def limpiar(self):
        self.lneCodigo.setText("")
        self.lneNombre.setText("")
        self.lneApellido.setText("")
        self.lneArea.setText("")
    

    def mostrar(self):
        filas = self.tblEmpleados.selectedItems()
        indiceFila = filas[0].row()
        codigo = self.tblEmpleados.item(indiceFila,0).text()
        nombre = self.tblEmpleados.item(indiceFila,1).text()
        apellido = self.tblEmpleados.item(indiceFila,2).text()
        area = self.tblEmpleados.item(indiceFila,3).text()

        self.lneCodigo.setText(codigo)
        self.lneNombre.setText(nombre)
        self.lneApellido.setText(apellido)
        self.lneArea.setText(area)
      

    def eliminar(self):
        rpta = QMessageBox.question(self,"Eliminar Empleado","¿Está seguro que desea eliminar el registro?",QMessageBox.Ok|QMessageBox.Cancel)
        if rpta==QMessageBox.Ok:
            filas = self.tblEmpleados.selectedItems()
            indiceFila = filas[0].row()
            codigo = self.tblEmpleados.item(indiceFila,0).text()
            posicion = objColeccionEmpleados.buscar(codigo)
            objColeccionEmpleados.eliminar(posicion)
            self.tblEmpleados.clearContents()
            self.tblEmpleados.setRowCount(0)
            self.listar()
            self.limpiar()



