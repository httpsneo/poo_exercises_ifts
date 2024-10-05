# Creamos una lista
Num = []

for i in range(5):
    num = int(input("Ingrese un numero:"))
    Num.append(num)

print(f"El numero maximo ingresado fue: {max(Num)}")
print(f"El numero minimo ingresado fue: {min(Num)}")