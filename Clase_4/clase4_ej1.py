class Persona:
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def mostrar_edad(self):
        return self.edad

    def es_mayor_de_edad(self):
        return self.__edad >= 18


mis_datos = Persona("Juan", 30, "12345678A")

print(f"{mis_datos._Persona__nombre} es mayor de edad" if mis_datos.es_mayor_de_edad() else f"{mis_datos._Persona__nombre} no es mayor de edad")

print(vars(mis_datos))  # Retornar estado de los objetos
