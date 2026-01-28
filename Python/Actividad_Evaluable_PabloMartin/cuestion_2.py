class Alumno:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
    def aprobado_o_suspenso(self):
        if self.calcular_media() >= 5:
            return f"\nEl alumno {self.nombre} ha aprobado con una media de {self.calcular_media():.2f}"
        else:
            return f"\nEl alumno {self.nombre} ha suspendido con una media de {self.calcular_media():.2f}"
        
    
alumnos = []

while True:
    print("\n***GESTOR DE NOTAS DE ALUMNOS***")
    print("1- Añadir un nuevo alumno")
    print("2- Calcular la media de cada alumno")
    print("3- Mostrar si cada alumno ha aprobado o suspendido")
    print("4- Mostrar el alumno con la mejor media")
    print("5- Salir")

    opcion_menu = int(input("\nIngresa una opcion del menu: "))

    if (opcion_menu == 1):
        nombre = input("\nIngresa el nombre del alumno: ")

        notas = []
        for i in range(3):
            nota = float(input(f"Ingresa la nota {i+1} del alumno: "))
            notas.append(nota)
        
        alumno = Alumno(nombre, notas)
        alumnos.append(alumno)
        continue

    elif (opcion_menu == 2):
        print("\nNota media de cada alumno")
        for alumno in alumnos:
            print(f"La media de {alumno.nombre} es {alumno.calcular_media():.2f}")
        continue

    elif (opcion_menu == 3):
        for alumno in alumnos:
            print(alumno.aprobado_o_suspenso())
        continue

    elif (opcion_menu == 4):
        if not alumnos:
            print("\nNo hay alumnos registrados.")
            continue

        mejor_alumno = max(alumnos, key=lambda a: a.calcular_media())
        print(f"\nEl alumno con la mejor media es {mejor_alumno.nombre} con una media de {mejor_alumno.calcular_media():.2f}")
        continue

    elif (opcion_menu == 5):
        print("\nSaliendo del gestor de notas de alumnos")
        break

    else:
        print("\nEscoje una opcion del menu")
        continue
