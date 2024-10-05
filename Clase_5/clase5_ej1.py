import random


class Password:
    # Atributos de clase
    __LONGITUD = 8
    __CARACTERES_VALIDOS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

    __MIN_CARACTERES = 6
    __MAX_CARACTERES = 15

    def __init__(self, longitud):
        self.__longitud = Password.__LONGITUD
        if longitud >= Password.__MIN_CARACTERES and longitud <= Password.__MAX_CARACTERES:
            self.__longitud = longitud
        else:
            print(f"La longitud ingresada debe de ser entre {Password.__MIN_CARACTERES} y {
                  Password.__MAX_CARACTERES}. Se generara una contraseña con el valor por default({Password.__LONGITUD}).")
        self.__contrasenia = Password.generarPassword(self)

    def generarPassword(self):
        return "".join(random.choice(Password.__CARACTERES_VALIDOS) for i in range(self.__longitud))

    def esFuerte(self):
        tiene_mayuscula = any(c.isupper() for c in self.__contrasenia)
        tiene_minuscula = any(c.islower() for c in self.__contrasenia)
        tiene_numero = any(c.isdigit() for c in self.__contrasenia)
        tiene_especial = any(c in "<=>@#%&+" for c in self.__contrasenia)
        return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial

    def getPassword(self):
        return self.__contrasenia

    def getLongitud(self):
        return self.__longitud

    def setPassword(self, contrasenia):
        if len(contrasenia) >= Password.__MIN_CARACTERES and len(contrasenia) <= Password.__MAX_CARACTERES:
            print("Contraseña cambiada con exito.")
            self.__contrasenia = contrasenia
            self.__longitud = len(contrasenia)
        else:
            print(f"No se ah cambiado la contraseña. La contraseña debe de tener entre {
                  Password.__MIN_CARACTERES} y {Password.__MAX_CARACTERES} caracteres.")

    def setLongitud(self, longitud):
        if longitud >= Password.__MIN_CARACTERES and longitud <= Password.__MAX_CARACTERES:
            print("Longitud cambiana con exito.")
            self.__longitud = longitud
            self.__contrasenia = Password.generarPassword(self)
        else:
            print(f"No se ah cambiado la longitud. La longitud ingresada debe de ser entre {
                  Password.__MIN_CARACTERES} y {Password.__MAX_CARACTERES}.")

    def __str__(self):
        return f"{self.__contrasenia} -- {self.esFuerte()}"


""" 
c1 = Password(10)
print(f"{c1}\n")

c1.setPassword("Holaa")
print(f"{c1.getPassword()}")
print(f"{c1.getLongitud()} \n")

c1.setLongitud(7)
print(f"{c1.getPassword()}")
print(f"{c1.getLongitud()}")
"""
passwords = []

while True:
    longitud = int(
        input("Ingrese la longitud de la contraseña a generar (0 para salir): \n"))
    if longitud == 0:
        break
    password = Password(longitud)
    passwords.append(password)

for password in passwords:
    print(password)
