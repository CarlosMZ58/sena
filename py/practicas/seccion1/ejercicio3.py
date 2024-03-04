def main():
    valorPrestamo = float(input("Cual es el monto del prestamo "))
    plazoPrestamo = int(input("A cuantos meses solicitó el prestamo? "))
    interes = 0.027
    
    valorCuotas = ((valorPrestamo*interes) + valorPrestamo) /plazoPrestamo
    print(valorCuotas)

if __name__ == "__main__":
    main()