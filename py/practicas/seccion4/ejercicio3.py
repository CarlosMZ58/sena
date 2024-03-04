def revisar_divisibilidad_por_cinco(n):
    if n % 5 == 0:
        print("El número es divisible por 5.")
    else:
        print("El número no es divisible por 5.")

numero = int(input("Por favor, ingrese un número: "))

revisar_divisibilidad_por_cinco(numero)