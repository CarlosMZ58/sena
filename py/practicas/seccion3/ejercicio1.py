def es_mayor_de_edad (edad):
    if edad >= 18:
        return True
    else:
        return False

edad_usuario = int(input("Introduzca su edad: "))

if  es_mayor_de_edad(edad_usuario):
    print("Usted es  mayor de edad.")
else:
    print("Usted no es mayor de edad.")