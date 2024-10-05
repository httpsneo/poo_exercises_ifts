def calcular_media():
    numeros = input("ingrese los numeros separados por espacios:")
    numeros = [float(num) for num in numeros.split()]
    suma = sum(numeros)
    return suma / len(numeros)

print(f"La media de los numeros ingresados es: {calcular_media()}" )