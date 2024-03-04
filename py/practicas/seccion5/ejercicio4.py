# def sacar_factorial(n):
#     for i in range(n, 0, -1):
#         resultado = i * (i-1)
#         if  i == 1:
#             return resultado

# numero = int(input("Ingrese un numero: "))
# print(f"El factorial de {numero} es:    {sacar_factorial(numero)}")
def sacar_factorial(n):
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(n, 0, -1):
            resultado *= i
        return resultado

numero = int(input("Ingrese un numero: "))
print(f"El factorial de {numero} es: {sacar_factorial(numero)}")