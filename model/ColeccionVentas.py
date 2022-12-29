from entity.Ventas import Ventas

class ColeccionVentas:
    def __init__(self):
        self.__listaVentas=[]
        self.cargar()

    def agregar(self,objVentas):
        self.__listaVentas.append(objVentas)
    
    def longitud(self):
        return len(self.__listaVentas)

    def obtener(self,posicion):
        return self.__listaVentas[posicion]

    def buscar(self,codigo):
        for posicion in range(self.longitud()):
            if codigo == self.__listaVentas[posicion].codigo:
                return posicion
        return -1

    def eliminar(self,posicion):
        del self.__listaVentas[posicion]

    def modificar(self,objNuevoPedido,posicion):
        self.obtener(posicion).nombre=objNuevoPedido.nombre
        self.obtener(posicion).pizza=objNuevoPedido.pizza
        self.obtener(posicion).cantidad=objNuevoPedido.cantidad
        self.obtener(posicion).costo=objNuevoPedido.costo
        self.obtener(posicion).fechadepedido=objNuevoPedido.fechadepedido
        self.obtener(posicion).fechadeentrega=objNuevoPedido.fechadeentrega
        self.obtener(posicion).factura=objNuevoPedido.factura

    def cargar(self):
        try:
            archivo=open("data/Ventas.txt","r",encoding="utf-8")
            for linea in archivo.readlines():
                columna=str(linea).split(";")
                codigo=columna[0]
                pizza=columna[1]
                cantidad=int(columna[2])
                costo=float(columna[3])
                fechadepedido=columna[4]
                fechadeentrega=columna[5]
                factura=columna[6]
                objVentas=Ventas(codigo,pizza,cantidad,costo,fechadepedido,fechadeentrega,factura)
                self.agregar(objVentas)
            archivo.close()
        except IOError:
            print("Error de E/S")


    def grabar(self):
        archivo=open("data/Ventas.txt","w",encoding="utf-8")
        for posicion in range(self.longitud()):
            cadena=self.obtener(posicion).codigo+";"
            cadena+=self.obtener(posicion).pizza+";"
            cadena+=str(self.obtener(posicion).cantidad)+";"
            cadena+=str(self.obtener(posicion).costo)+";"
            cadena+=self.obtener(posicion).fechadepedido+";"
            cadena+=self.obtener(posicion).fechadepedido+";"
            cadena+=self.obtener(posicion).factura+"\n"
            archivo.write(cadena)
        archivo.close()



