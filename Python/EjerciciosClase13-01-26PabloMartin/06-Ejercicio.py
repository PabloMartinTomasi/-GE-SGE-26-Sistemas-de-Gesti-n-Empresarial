precio = float(input("Ingresa el precio del producto: "))

iva = precio * 0.21
precioFinal = precio + iva

print(f"El precio final con IVA es: {precioFinal}€")