"""
Escribe un funcion que pida por teclado la distancia y la velocidad
de un movil en movimiento MRU y determinada el tiempo de viaje
"""

def tiempo_mru(distancia, velocidad):
    return distancia / velocidad

distancia = float(input("Introduce la distancia: "))
velocidad = float(input("Introduce la velocidad: "))

tiempo = tiempo_mru(distancia, velocidad)

print(f"El tiempo de viaje es de {tiempo} horas")