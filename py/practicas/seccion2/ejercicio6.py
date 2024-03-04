def calcula_porcentaje(numero, porcentaje):
    return (numero * porcentaje) / 100

numero = float(input("Introduzca el numero del que desea calcular el porcentaje: "))
porcentaje_calcular = float(input("Introduzca el porcentaje que desea  calcular: "))

print(f"El {porcentaje_calcular}% de {numero} es: {calcula_porcentaje(numero,  porcentaje_calcular)}")