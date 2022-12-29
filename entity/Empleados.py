class Empleados:
    def __init__(self,codigo,nombre,apellido,area):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__apellido=apellido
        self.__area=area
    

    @property
    def codigo(self):
        return self.__codigo
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self,apellido):
        self.__apellido=apellido
    @property
    def area(self):
        return self.__area
    @area.setter
    def area(self,area):
        self.__area=area
 



