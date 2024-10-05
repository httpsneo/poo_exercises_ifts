def tiempo():
    hora = int(input("Ingrese la cantidad de horas:"))
    minutos = int(input("Ingrese la cantidad de minutos:"))
    segundos = int(input("Ingrese la cantidad de segundos:"))
    return hora*3600 + minutos*60 + segundos

print(f"La cantidad de segundos son ingresados son: {tiempo()}")