"""Seguimiento de hábitos diarios.
Crea una clase Habito con nombre y número de días cumplidos.
Utiliza un bucle para registrar el progreso diario.
Emplea condicionales para mostrar mensajes según el nivel de constancia.
El usuario debe insertar los datos por consola."""

class Habito:
    def __init__(self, nombre):
        self.nombre = nombre
        self.numero_dias_cumplidos = 0

    def registro_progreso(self):
        self.numero_dias_cumplidos += 1


nombre = input("Nombre del hábito: ")
habito = Habito(nombre)

while True:
    respuesta = input("¿Se ha cumplido el hábito hoy? (s/n): ").lower()

    if respuesta == "s":
        habito.registro_progreso()

    if habito.numero_dias_cumplidos == 0:
        print("Aún no has comenzado, mañana es una buena oportunidad.")
    elif habito.numero_dias_cumplidos < 5:
        print("Buen comienzo, sigue así.")
    elif habito.numero_dias_cumplidos < 10:
        print("Excelente constancia, ya es un hábito.")
    else:
        print("Impresionante disciplina, sigue imparable.")

    continuar = input("¿Deseas registrar otro día? (s/n): ").lower()
    if continuar != "s":
        break


print(f"\nHábito: {habito.nombre}")
print(f"Días cumplidos: {habito.numero_dias_cumplidos}")
