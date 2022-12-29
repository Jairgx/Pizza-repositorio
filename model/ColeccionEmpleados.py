class ColeccionEmpleados:
    def __init__(self):
        self.__listaEmpleado=[]
    
    def agregar(self,objeto):
        self.__listaEmpleado.append(objeto)

    def longitud(self):
        return len(self.__listaEmpleado)
    
    def obtener(self,pos):
        return self.__listaEmpleado[pos]

    def buscar(self,codigo):
        for i in range(self.longitud()):
            if codigo==self.__listaEmpleado[i].codigo:
                return i
        return -1 

    def eliminar(self, pos):
        del self.__listaEmpleado[pos]

    def modificar(self, objEmpleado, pos):
        self.obtener(pos).nombre = objEmpleado.nombre
        self.obtener(pos).apellido = objEmpleado.apellido
        self.obtener(pos).area = objEmpleado.area




    


