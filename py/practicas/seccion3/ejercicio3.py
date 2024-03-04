def comparar_dos_numeros(n1, n2):
    if n1 == n2:
        return "Los numeros son iguales"
    elif n1 > n2:
        return f"{n1} es mayor que {n2}"
    else:
        return f"{n2} es mayor que {n1}"

numero_uno = float(input("Ingrese el primer número: "))
numero_dos = float(input("Ingrese el segundo número: "))

comparar_dos_numeros(numero_uno, numero_dos)