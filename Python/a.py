class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = 0
    
    def contratar(self):
        self.empleados += 1
    
    def despedir(self):
        if self.empleados > 0:  # Evitar número negativo de empleados
            self.empleados -= 1


# --- Programa principal ---
empresa = Empresa("Tech Solutions")

for i in range(5):
    opcion = int(input("Ingresa 1 para contratar un empleado o 2 para despedir un empleado: "))
    if opcion == 1:
        empresa.contratar()
    elif opcion == 2:
        empresa.despedir()
    else:
        print("Opción inválida")

print(f"La empresa {empresa.nombre} tiene {empresa.empleados} empleados.")
