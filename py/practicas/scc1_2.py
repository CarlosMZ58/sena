def main():
    num1 = float(input("introduzca el primer numero: "))
    num2 = float(input("introduzca el segundo numero: "))
    modulo = num1 % num2
    producto = num1 * num2
    suma = num1 + num2
    resta = num1 - num2
    cociente = num1/num2
    
    print(f"""
        Los resultados del producto, cociente, suma, resta y el modulo los siguientes dos numeros:  numero 1 = {num1}   numero 2 = {num2} son:
        Producto = {producto}
        Cociente = {cociente}
        Suma = {suma}
        Resta = {resta}
        Modulo = {modulo}
        """)
    
if __name__ == "__main__":
    main()