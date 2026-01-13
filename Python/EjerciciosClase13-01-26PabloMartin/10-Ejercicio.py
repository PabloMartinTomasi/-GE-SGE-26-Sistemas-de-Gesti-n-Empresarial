ventasRealizadas = float(input("Ingresa el total de ventas realizadas: "))

comision = ventasRealizadas * 0.08
salarioFinal = ventasRealizadas + comision

print(f"El salario final con comisión es: {salarioFinal}€")