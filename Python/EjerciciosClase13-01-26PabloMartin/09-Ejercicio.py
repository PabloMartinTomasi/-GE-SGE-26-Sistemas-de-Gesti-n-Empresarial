totalCompra = float(input("Ingresa el total de la compra: "))

compraDescuento = totalCompra * 0.15
totalPagar = totalCompra - compraDescuento

print(f"El total a pagar con descuento es: {totalPagar}€")