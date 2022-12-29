from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from model.ColeccionVentas import ColeccionVentas
from entity.Ventas import Ventas

objColeccionVentas = ColeccionVentas()

class frmVentas(QMainWindow):
    def __init__(self,parent=None):
        super(frmVentas,self).__init__(parent)
        uic.loadUi("view/Ventas.ui",self)
        self.btnGrabar.clicked.connect(self.grabar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.tblVentas.itemClicked.connect(self.mostrar)
        self.tblVentas.verticalHeader().setVisible(False)
        self.listar()

    def grabar(self):
        codigo=self.lneCodigo.text()
        pizza=self.lnePizza.text()
        cantidad=int(self.lneCantidad.text())
        costo=float(self.lneCosto.text())
        fechadepedido=self.lneFechadePedido.text()
        fechadeentrega=self.lneFechadeEntrega.text()
        factura=self.lneFactura.text()
        objVentas=Ventas(codigo,pizza,cantidad,costo,fechadepedido,fechadeentrega,factura)
        posicion = objColeccionVentas.buscar(codigo) 
        if posicion==-1:
            objColeccionVentas.agregar(objVentas)
        else:
            objColeccionVentas.modificar(objVentas,posicion)
        objColeccionVentas.grabar()
        self.listar()
        self.limpiar()

    def listar(self):
        self.tblVentas.setRowCount(objColeccionVentas.longitud())
        for i in range(objColeccionVentas.longitud()):
            self.tblVentas.setItem(i,0,QTableWidgetItem(objColeccionVentas.obtener(i).codigo))
            self.tblVentas.setItem(i,1,QTableWidgetItem(objColeccionVentas.obtener(i).pizza))
            self.tblVentas.setItem(i,2,QTableWidgetItem(str(objColeccionVentas.obtener(i).cantidad)))
            self.tblVentas.setItem(i,3,QTableWidgetItem(str(objColeccionVentas.obtener(i).costo)))
            self.tblVentas.setItem(i,4,QTableWidgetItem(str(objColeccionVentas.obtener(i).calcularMonto())))
            self.tblVentas.setItem(i,5,QTableWidgetItem(objColeccionVentas.obtener(i).fechadepedido))
            self.tblVentas.setItem(i,6,QTableWidgetItem(objColeccionVentas.obtener(i).fechadeentrega))
            self.tblVentas.setItem(i,7,QTableWidgetItem(objColeccionVentas.obtener(i).factura))

            
    def limpiar(self):
        self.lneCodigo.setText("")
        self.lnePizza.setText("")
        self.lneCantidad.setText("")
        self.lneCosto.setText("")
        self.lneFechadePedido.setText("")
        self.lneFechadeEntrega.setText("")
        self.lneFactura.setText("")

    def mostrar(self):
        fila = self.tblVentas.selectedItems()
        indiceFila = fila[0].row()
        codigo = self.tblVentas.item(indiceFila,0).text()
        pizza = self.tblVentas.item(indiceFila,1).text()
        cantidad = self.tblVentas.item(indiceFila,2).text()
        costo = self.tblVentas.item(indiceFila,3).text()
        fechadepedido = self.tblVentas.item(indiceFila,5).text()
        fechadeentrega = self.tblVentas.item(indiceFila,6).text()
        factura = self.tblVentas.item(indiceFila,7).text()
        self.lneCodigo.setText(codigo)
        self.lnePizza.setText(pizza)
        self.lneCantidad.setText(cantidad)
        self.lneCosto.setText(costo)
        self.lneFechadePedido.setText(fechadepedido)
        self.lneFechadeEntrega.setText(fechadeentrega)
        self.lneFactura.setText(factura)

    def eliminar(self):
        rpta=QMessageBox.question(self,"Eliminar","Está seguro de eliminar el pedido",QMessageBox.Ok|QMessageBox.Cancel)
        if rpta==QMessageBox.Ok:
            fila = self.tblVentas.selectedItems()
            indiceFila = fila[0].row()
            codigo=self.tblVentas.item(indiceFila,0).text()
            posicion=objColeccionVentas.buscar(codigo)
            objColeccionVentas.eliminar(posicion)
            objColeccionVentas.grabar()
            self.tblVentas.clearContents()
            self.tblVentas.setRowCount(0)
            self.listar()
            self.limpiar()





