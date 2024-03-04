def calcular_promedio():
    n = int(input("Ingrese el número de estudiantes: "))
    for i in range(n):
        print(f"Estudiante {i+1}")
        notas = []  
        for u in range(3):  
            nota = float(input(f"Ingrese la nota {u+1}: "))
            notas.append(nota)  
        promedio = sum(notas) / len(notas)  
        print(f"El promedio de las notas es: {promedio}")

calcular_promedio()