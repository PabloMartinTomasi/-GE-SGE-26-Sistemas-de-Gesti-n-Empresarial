""" Gestión de turnos en una clínica.
Crea una clase Turno con paciente, hora y estado (pendiente o atendido).
Utiliza condicionales para cambiar el estado del turno.
Emplea un bucle para mostrar todos los turnos registrados.
El usuario debe insertar los datos por consola."""


class Turno:
    def __init__(self, paciente, hora):
        self.paciente = paciente
        self.hora = hora
        self.estado = "pendiente"

    def cambiar_estado_turno(self):
        self.estado = "atendido"


turnos = []

while True:
    paciente = input("Nombre del paciente o 'fin' para terminar: ")
    if paciente == "fin":
        break

    hora = input("Hora del turno (ej. hh:mm): ")

    turno = Turno(paciente, hora)

    atendido = input(f"{turno.paciente} ha sido atendido (s/n): ").lower()
    if atendido == "s":
        turno.cambiar_estado_turno()

    turnos.append(turno)

print("\nListado de turnos registrados:\n")

for t in turnos:
    print(f"Paciente: {t.paciente} | Hora: {t.hora} | Estado: {t.estado}")
