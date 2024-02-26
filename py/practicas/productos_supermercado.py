def main():
    CON__IVA = ["crema", "vino"]
    SIN_IVA = ["lentejas", "arroz"]
    producto_preguntado = input("¿Sobre qué producto desea averiguar si tiene iva?")

    if producto_preguntado.lower() in CON__IVA:
        print("Este producto paga iva")
    elif producto_preguntado.lower() in SIN_IVA:
        print("El producto no paga iva")
    else:
        print("El producto no esta en la lista de productos")
if __name__ == "__main__":
    main()