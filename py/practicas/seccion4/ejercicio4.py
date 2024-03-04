def es_primo(n):
    if n < 2: 
        return False
    for i in range(2, n): 
        if n % i == 0: 
            return False 
    return True

numero = int(input("Ingrese un número entre 1 y 15: "))

if numero < 1 or numero > 15:
    print("El número debe estar entre 1 y 15.")
else:
    if es_primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")