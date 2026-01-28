class Ventas:
    def __init__(self, dia, ventas_totales):
        self.dia = dia
        self.ventas_totales = ventas_totales
    
    def calcular_total_ventas(self):
        return sum(self.ventas_totales)
    
    def media_diaria(self):
        return self.calcular_total_ventas() / len(self.ventas_totales)
    
    def dia_con_mas_ventas(self):
        max_ventas = max(self.ventas_totales)
        dia_index = self.ventas_totales.index(max_ventas)
        return self.dia[dia_index], max_ventas
    
    def dia_con_menos_ventas(self):
        min_ventas = min(self.ventas_totales)
        dia_index = self.ventas_totales.index(min_ventas)
        return self.dia[dia_index], min_ventas

dias_mes = [f"Dia {i+1}" for i in range(30)]

ventas = []

print(f"Ingresa la venta del {dias_mes[0]}: ")

for dia in dias_mes:
    venta = float(input(f"{dia}: "))
    ventas.append(venta)

ventas_mes = Ventas(dias_mes, ventas)

print("\n--- Resumen del Mes ---")
print(f"Total de ventas: {ventas_mes.calcular_total_ventas():.2f}€")
print(f"Media diaria: {ventas_mes.media_diaria():.2f}€")

dia_max, max_ventas = ventas_mes.dia_con_mas_ventas()
print(f"Día con más ventas: {dia_max} - {max_ventas:.2f}€")

dia_min, min_ventas = ventas_mes.dia_con_menos_ventas()
print(f"Día con menos ventas: {dia_min} - {min_ventas:.2f}€")