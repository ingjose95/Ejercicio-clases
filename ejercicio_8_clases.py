class Persona():

    def __init__(self, edad, nombre, telefono):

        self.__edad__ = edad
        self.__nombre__ =  nombre
        self.__telefono__ = telefono

    def get_edad(self):

        return self.__edad__

    def get_nombre(self):

        return self.__nombre__

    def get_telefono(self):

        return self.__telefono__

    def set_edad(self, edad):

        self.__edad__ = edad

    def set_nombre(self, nombre):

        self.__nombre__ = nombre

    def set_telefono(self, telefono):

        self.__telefono__ = telefono

persona1 = Persona(26, 'Jose', 412)

print('Los datos originales son: ')

print(persona1.get_edad())
print(persona1.get_nombre())
print(persona1.get_telefono())

print('Los nuevos datos son: ')

persona1.set_edad(30)
print(persona1.get_edad())

persona1.set_nombre('Maria')
print(persona1.get_nombre())

persona1.set_telefono(414)
print(persona1.get_telefono())
