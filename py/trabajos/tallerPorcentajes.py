def main():
    print("1. Calcular el porcentaje de un número")
    print("2. Saber qué porcentaje es un número de otro número")
    print("3. Hacer un aumento porcentual a un número")
    print("4. Hacer un decremento porcentual a un número")
    opcion = int(input("Elige una opción (1-4): "))

    if opcion == 1:
        num = float(input("Introduce el número: "))
        porcentaje = float(input("Introduce el porcentaje que quieres calcular: "))
        resultado = (porcentaje / 100) * num
        print(f"El {porcentaje}% de {num} es {resultado}")
    elif opcion == 2:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        resultado = (num1 / num2) * 100
        print(f"{num1} es el {resultado}% de {num2}")
    elif opcion == 3:
        num = float(input("Introduce el número: "))
        porcentaje = float(input("Introduce el porcentaje que quieres aumentar: "))
        resultado = num + (num * (porcentaje / 100))
        print(f"El número {num} aumentado un {porcentaje}% es {resultado}")
    elif opcion == 4:
        num = float(input("Introduce el número: "))
        porcentaje = float(input("Introduce el porcentaje que quieres disminuir: "))
        resultado = num - (num * (porcentaje / 100))
        print(f"El número {num} disminuido un {porcentaje}% es {resultado}")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()