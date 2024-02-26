def main():
    edadUsuario = int(input("Cual es su edad?"))
    añosASumar = int(input("Cuantos años desea sumarle a su edad?"))
    edadFinal = edadUsuario + añosASumar
    
    print("Su edad dentro de ", añosASumar, " años sera de ", edadFinal, " años")
if __name__ == "__main__":
    main()