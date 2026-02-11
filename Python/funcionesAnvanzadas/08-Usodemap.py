"""
Funciones_avanzadas

Dada una lista de números enteros:
  numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Se pide:
* Filtrar los numeros que sean pares
* Multiplicar por 2 cada uno de los numeros pares obtenidos
* Mostrar por la pantalla la lista final resultante
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#filtros (filter), lamda, map

pares = filter(lambda x: x % 2 == 0, numeros)



#multiplicar por 2 los numeros pares

resutado = map(lambda x: x * 2, pares)

print(list(filter(lambda x: x % 2 == 0, numeros)))
print(list(map(lambda x: x * 2, pares)))