def main():
    numero_uno = float(input("Ingrese el primer número: "))
    numero_dos = float(input("Ingrese el segundo número: "))

    if numero_uno < numero_dos:
        print(f"El mayor de los dos números es {numero_dos}")
    elif numero_dos  > numero_uno:
        print(f"El mayor de los dos números es {numero_uno}")
    elif numero_dos == numero_uno:
        print(f"Los dos números son iguales ({numero_uno})")
    else:
        return
if __name__ == "__main__":
    main()