"""
3-- Crear la clase libro con estos atributos:
**** titulo, autor, editorial, anio_publicacion

metodos:
contructor para inicializar los atributos

determina si el libro es del año 2020 hacia atras debe inidicar que es antiguo
si es del 2020 hasta la fecha actual, debe ejecutarse hasta que encuentre editorial "Espanola"
"""

class Libro:
    def __init__(self, titulo, autor, editorial, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio_publicacion = anio_publicacion

    def es_antiguo(self):
        return self.anio_publicacion < 2020

while True:
    titulo = input("Ingresa el titulo del libro: ")
    autor = input("Ingresa el autor del libro: ")
    editorial = input("Ingresa la editorial del libro: ")
    anio_publicacion = int(input("Ingresa el año de publicación del libro: "))

    libro1 = Libro(titulo, autor, editorial, anio_publicacion)

    if libro1.es_antiguo():
        print(f"El libro '{libro1.titulo}' es antiguo.")


    if libro1.editorial == "Espanola":
        print(f"El libro '{libro1.titulo}' es de la editorial Española.")
        break

    else:
        print(f"El libro '{libro1.titulo}' no es de la editorial Española. Ingrese otro libro.")