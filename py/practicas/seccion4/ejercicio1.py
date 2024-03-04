def revisar_si_es_un_triangulo():
    angulos = [float(input("angulo 1")), float(input("angulo 2")), float(input("angulo 3"))]
    suma_angulos = sum(angulos)

    if suma_angulos == 180:
        print("Si es un triangulo")
    else:
        print("No es un triangulo")

revisar_si_es_un_triangulo()

# angulos = [float(input("angulo {}: ".format(i+1))) for i in range(3)]