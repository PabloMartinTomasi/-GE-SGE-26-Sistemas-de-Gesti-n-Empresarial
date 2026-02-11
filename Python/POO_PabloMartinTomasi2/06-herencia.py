"""
Herrencia
Crear una clase Persona y otra clase Estudiante
La clase Persona tiene el atributo nombre y el método mostrar_nombre()
La clase Estudiante hereda de Persona y utilizar
el método mostrar_nombre() para mostrar el nombre del estudiante
"""

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar_nombre(self):
        print(self.nombre)


class Estudiante(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def mostrar(self):
        super().mostrar_nombre()


nombre = input("Ingresa tu nombre: ")
estudiante1 = Estudiante(nombre)
estudiante1.mostrar()