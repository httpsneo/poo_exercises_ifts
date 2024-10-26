def agregar_una_vez(lista, elem):
    if elem in lista:
        raise ValueError(f"Error: Imposible añadir elementos duplicados => {elem}")
    else:
        lista.append(elem)

def main():
    elementos = [1, 5, -2]
    
    valores_a_agregar = [10, -2, "Hola"]
    
    for valor in valores_a_agregar:
        try:
            agregar_una_vez(elementos, valor)
        except ValueError as e:
            print(e)
    
    print("Contenido final de la lista:", elementos)

main()