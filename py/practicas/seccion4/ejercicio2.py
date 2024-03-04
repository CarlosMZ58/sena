def es_par (n):
    if n % 2 == 0:
        return True
    else:
        return  False

numero = int(input("Ingrese  un numero: "))
if  es_par(numero) :
    print (f"{numero} si es par")
else:
    print (f"{numero} no es par")