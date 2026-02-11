""" Simulador de consumo eléctrico.
Crea una clase Electrodomestico con nombre, potencia y horas de uso.
Utiliza un bucle para registrar varios electrodomésticos.
Emplea condicionales para indicar si el consumo supera un límite establecido.
El usuario debe insertar los datos por consola."""

class Electrodomestico:
    def __init__(self, nombre, potencia, horas_uso):
        self.nombre = nombre
        self.potencia = potencia
        self.horas_uso = horas_uso
    
    def consumo(self):
        return self.potencia * self.horas_uso

limite_consumo = 7.00

electrodomesticos = []

while True:
    nombre = input("Nombre del electrodomestico. O fin para salir: ")
    if (nombre == "fin"):
        break

    potencia = float(input("Potencia en kW: "))
    horas = float(input("Horas de uso diario: "))

    electrodomestico = Electrodomestico(nombre, potencia, horas)

    electrodomesticos.append(electrodomestico)

print("CONSUMO")
for e in electrodomesticos:
    consumo = e.consumo()
    print(f"{e.nombre}: {consumo:.2f} kWh")

    if consumo > limite_consumo:
        print("Consumo superior al límite establecido\n")
    else:
        print("Consumo dentro del límite\n")