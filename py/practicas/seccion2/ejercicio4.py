def main():
    precioProducto = float(input("Digite el precio del producto : "))
    Iva = 0.19
    precioConIva = precioProducto * Iva + precioProducto
    
    print(f"El precio del producto ya con el 19% de iva es {precioConIva}")
if __name__ == "__main__":
    main()