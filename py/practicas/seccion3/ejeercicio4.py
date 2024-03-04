def comparar_numeros(lista_numeros):
    lista_numeros.sort(reverse=True)

    if lista_numeros.count(lista_numeros[0]) == len(lista_numeros):
        print("Todos los números son iguales")
        return

    print("Aca se muestan los numeros desde el mayor al menor:  ")
    for j in lista_numeros:
        print(j)

cantidad_numeros = int(input("Cuantos numeros desea comparar?  "))
numeros = []

for i in range (0, cantidad_numeros):
    numero = int(input(f"ingrese el numero  {i+1}:   "))
    numeros.append(numero)

comparar_numeros(numeros)