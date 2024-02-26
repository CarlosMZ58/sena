import math
def main():
    PI = math.pi
    radioCirculo = float(input("Digite el radio del circulo : "))
    areaCirculo = PI * (radioCirculo * radioCirculo)
    perimetroCirculo = (PI * radioCirculo) * 2
    
    print(f"""
        El area y perimetro de un ciculo con radio {radioCirculo} es:
        Area = {areaCirculo}
        Perimetro = {perimetroCirculo}
        """)
if __name__ == "__main__":
    main()