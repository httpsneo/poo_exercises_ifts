def tiempo():
    # Contadores
    horas_totales = 0
    minutos_totales = 0
    segundos_totales = 0

    # Peticion al usuario 2 veces
    for i in range(2):
        print("--Ingreso de segundo intervalo--" if i >= 1 else "--Ingreso de primer intervalo--")
        hora = int(input("Ingrese la cantidad de horas:"))
        minutos = int(input("Ingrese la cantidad de minutos:"))
        segundos = int(input("Ingrese la cantidad de segundos:"))
        horas_totales += hora
        minutos_totales += minutos
        segundos_totales += segundos
        if minutos_totales >= 60:
            horas_totales += 1
            minutos_totales -= 60
        if segundos_totales >= 60:
            minutos_totales += 1
            segundos_totales -= 60

    print(f"La cantidad de horas es: {horas_totales}")
    print(f"La cantidad de minutos es: {minutos_totales}")
    print(f"La cantidad de segundos es: {segundos_totales}")

tiempo()