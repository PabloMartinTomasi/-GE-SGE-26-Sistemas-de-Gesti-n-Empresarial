"""
Crea un progrma que permita al usuario:
* ingresar notas de alumnos (valores entre 1 y 10) por el usuario
* agregar notas una por una en una lista
* finalizar la carga de notas ingresando el valor 0

Mostrar:
* las notas aprobadas (mayor o igual que 6)
* el promedio de las notas aprobadadas (Si existen)
"""

#Funciones
#######################################################################################################################################################################################
""" n1 = float(input("Ingresa una nota: ")) 
n2 = float(input("Ingresa una nota: ")) 
n3 = float(input("Ingresa una nota: ")) 
n4 = float(input("Ingresa una nota: "))

notas = [n1, n2, n3, n4]

def obtener_aprobadas(notas):
    return [nota for nota in notas if nota >= 6]

def calcular_promedio(notas):
    if len(notas) == 0:
        return None
    return sum(notas)/len(notas)

aprobadas = obtener_aprobadas(notas)
promedio = calcular_promedio(aprobadas)

print("Notas aprobadas:", aprobadas)
if promedio is not None:
    print("Promedio de aprobadas:", promedio)
else:
    print("No hay notas aprobadas para calcular el promedio.") """
#######################################################################################################################################################################################

#POO
#######################################################################################################################################################################################
""" class Alumno:
    def __init__(self, notas):
        self.notas = notas
        self.aprobadas = self.obtener_aprobadas()
        self.promedio_aprobadas = self.calcular_promedio()

    def obtener_aprobadas(self):
        return [nota for nota in self.notas if nota >= 6]

    def calcular_promedio(self):
        if len(self.aprobadas) == 0:
            return None
        return sum(self.aprobadas) / len(self.aprobadas)

    def mostrar_resultados(self):
        print("Notas aprobadas:", self.aprobadas)
        if self.promedio_aprobadas is not None:
            print("Promedio de aprobadas:", self.promedio_aprobadas)
        else:
            print("No hay notas aprobadas para calcular el promedio.")

n1 = float(input("Ingresa una nota: ")) 
n2 = float(input("Ingresa una nota: ")) 
n3 = float(input("Ingresa una nota: ")) 
n4 = float(input("Ingresa una nota: "))

notas = [n1, n2, n3, n4]

alumno = Alumno(notas)

alumno.mostrar_resultados() """
#######################################################################################################################################################################################

#Programacion funcion
#######################################################################################################################################################################################
n1 = float(input("Ingresa una nota: ")) 
n2 = float(input("Ingresa una nota: ")) 
n3 = float(input("Ingresa una nota: ")) 
n4 = float(input("Ingresa una nota: "))

notas = [n1, n2, n3, n4]

aprobadas = list(filter(lambda x: x >= 6, notas))

promedio = sum(aprobadas) / len(aprobadas) if aprobadas else None

print("Notas aprobadas:", aprobadas)
if promedio is not None:
    print("Promedio de aprobadas:", promedio)
else:
    print("No hay notas aprobadas para calcular el promedio.")
#######################################################################################################################################################################################