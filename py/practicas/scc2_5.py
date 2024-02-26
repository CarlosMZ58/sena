def main():
    precioProducto = float(input("Digite el precio del producto : "))
    Descuento = 0.1
    precioConDescuento =  precioProducto - (precioProducto * Descuento)
    
    print(f"El precio del producto ya con el 10% de descuento es {precioConDescuento}")
if __name__ == "__main__":
    main()