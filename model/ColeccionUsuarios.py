class ColeccionUsuarios:
    def __init__(self):
        self.__listaUsuarios=[]
    
    def agregar(self,objeto):
        self.__listaUsuarios.append(objeto)

    def longitud(self):
        return len(self.__listaUsuarios)
    
    def obtener(self,pos):
        return self.__listaUsuarios[pos]

    def buscar(self,codigo):
        for i in range(self.longitud()):
            if codigo==self.__listaUsuarios[i].codigo:
                return i
        return -1 

    def eliminar(self, pos):
        del self.__listaUsuarios[pos]

    def modificar(self, objUsuario, pos):
        self.obtener(pos).nombre = objUsuario.nombre
        self.obtener(pos).apellido = objUsuario.apellido
        self.obtener(pos).dni = objUsuario.dni
        self.obtener(pos).telefono = objUsuario.telefono