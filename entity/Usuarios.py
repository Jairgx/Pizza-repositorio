class Usuarios:
    def __init__(self,codigo,nombre,apellido,dni,telefono):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__apellido=apellido
        self.__dni=dni
        self.__telefono=telefono
         
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
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self,dni):
        self.__dni=dni
    @property
    def telefono(self):
        return self.__telefono	
    @telefono.setter
    def telefono(self,telefono):
        self.__telefono=telefono
