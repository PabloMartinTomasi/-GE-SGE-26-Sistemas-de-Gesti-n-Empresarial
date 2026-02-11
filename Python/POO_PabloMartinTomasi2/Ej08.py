"""Simulación de un videojuego de personajes.
Crea una clase Personaje con nombre, vida y nivel.
Utiliza condicionales para verificar si el personaje sigue con vida.
Emplea un bucle para simular varias rondas de juego.
El usuario debe insertar los datos por consola."""

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 10
        self.nivel = 1
    
    def pierde_vida(self):
        self.vida -= 1
    
    def sube_nivel(self):
        self.nivel += 1


nombre = input("Ingresa el nombre de tu personaje: ")
personaje = Personaje(nombre)

while personaje.vida > 0:
    accion = input("¿Quieres enfrentarte a un desafío? (s/n): ").lower()

    if accion != "s":
        print("Has decidido descansar. Fin de la sesión.")
        break

    from random import randint
    resultado = randint(0, 1)

    if resultado == 0:
        personaje.pierde_vida()
        print(f"¡Oh no! Perdiste 1 de vida. Vida actual: {personaje.vida}")
    else:
        personaje.sube_nivel()
        print(f"¡Genial! Subiste de nivel. Nivel actual: {personaje.nivel}")

    if personaje.vida <= 0:
        print(f"\n{personaje.nombre} ha sido derrotado. Juego terminado.")
        break

print(f"\nEstado final de {personaje.nombre}: Vida = {personaje.vida}, Nivel = {personaje.nivel}")
