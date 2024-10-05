num = []
repetidos = False

#Pedimos los 5 numeros
for i in range(5):
    num.append(int(input("Ingrese un numero:")))

#Verificamos si hay repetidos
for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if num[i] == num[j]:
            repetidos = True
            break

print("HAY DUPLICADOS" if repetidos else "NO HAY DUPLICADOS")