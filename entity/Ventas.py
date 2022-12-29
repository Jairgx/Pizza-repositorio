class Ventas:
    def __init__(self,codigo,pizza,cantidad,costo,fechadepedido,fechadeentrega,factura):
        self.__codigo=codigo
        self.__pizza=pizza
        self.__cantidad=cantidad
        self.__costo=costo
        self.__fechadepedido=fechadepedido
        self.__fechadeentrega=fechadeentrega
        self.__factura=factura

    @property
    def codigo(self):
        return self.__codigo
    @property
    def pizza(self):
        return self.__pizza
    @pizza.setter
    def pizza(self,pizza):
        self.__pizza=pizza
    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad=cantidad
    @property
    def costo(self):
        return self.__costo
    @costo.setter
    def costo(self,costo):
        self.__costo=costo
    @property
    def fechadepedido(self):
        return self.__fechadepedido
    @fechadepedido.setter
    def fechadepedido(self,fechadepedido):
        self.__fechadepedido=fechadepedido
    @property
    def fechadeentrega(self):
        return self.__fechadeentrega
    @fechadeentrega.setter
    def fechadeentrega(self,fechadeentrega):
        self.__fechadeentrega=fechadeentrega
    @property
    def factura(self):
        return self.__factura
    @factura.setter
    def factura(self,factura):
        self.__factura=factura
        
    def calcularMonto(self):
        return self.__costo*self.__cantidad

   

