"""
dada una lista de numeros, crear un programa que:
* determina si un numeros es positivo
* obtenga una lista con los numeros positivos
* multiplique esos numeros por 2
* muestre el resultado final
"""

#Opcion 1
#######################################################################################################################################################################################
""" def es_positivo(numero):
    return numero > 0

def filtrar_positivos(lista):
    positivos = []
    for n in lista:
        if es_positivo(n):
            positivos.append(n)
    return positivos

def duplicar_lista(lista):
    duplicados = []
    for n in lista:
        duplicados.append(n * 2)
    return duplicados

numeros = [-5, -67, 67, 8, 40, -9, 50, 10, -8, 70, -80, -60, -69, 69]

positivos = filtrar_positivos(numeros)
resultado = duplicar_lista(positivos)

print(resultado)
print(positivos) """
#######################################################################################################################################################################################


#Opcion 2
#######################################################################################################################################################################################
""" class procesadores_numeros:
    def __init__(self, numeros):
        self.numeros = numeros

    def obtener_positivos(self):
        return [n for n in self.numeros if n > 0]
    
    def duplicar(self, lista):
        return [n * 2 for n in lista]
    
    def procesar(self):
        positivos = self.obtener_positivos()
        return self.duplicar(positivos)
    
numeros = [-5, -67, 67, 8, 40, -9, 50, 10, -8, 70, -80, -60, -69, 69]

procesador = procesadores_numeros(numeros)
print(procesador.procesar()) """
#######################################################################################################################################################################################


#Opcion 3
#######################################################################################################################################################################################
""" numeros = [-5, -67, 67, 8, 40, -9, 50, 10, -8, 70, -80, -60, -69, 69]

positivos = filter(lambda x: x > 0, numeros)
resultado = map(lambda x : x * 2, positivos)

print(list(resultado)) """
#######################################################################################################################################################################################