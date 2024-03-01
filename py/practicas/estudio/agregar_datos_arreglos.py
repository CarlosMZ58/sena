numeros = []
while True:
    desicion = input("Desea continuar? s/n ")
    if desicion == "n" or desicion == "N":
        break
    elif desicion == "s" or  desicion == "S":
        nuevo_numero = int(input("Ingrese un numero: "))
        numeros.append(nuevo_numero)
    elif desicion != "s" or "n":
        print("Respuesta incorrecta. Por favor, ingrese 's' o 'n'.")
    elif nuevo_numero < 0 :
        print("Entrada inválida. Por favor, intente de nuevo.")
        continue

print("Lista final de numeros:", numeros)