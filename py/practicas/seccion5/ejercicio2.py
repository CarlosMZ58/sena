def tabla_multiplicar (n, n2):
    for i in range (1, 1+n2):
        print(n*i)

numero_tabla = 3    #int(input("Ingrese el numero del que desea saber la tabla de multiplicar: "))
numero_maximo= 50   #int(input("Hasta que numero  quiere ver su tabla? "))
tabla_multiplicar(numero_tabla, numero_maximo)