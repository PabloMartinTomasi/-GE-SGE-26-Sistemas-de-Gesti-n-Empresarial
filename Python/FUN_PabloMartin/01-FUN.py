"""
Elabore una funcion que permita convertir los grados Celsius en grados Fahrenheit
"""

def celcius_a_farenheit(grados_c):
    return (grados_c * 9/5) + 32

celsius_usuario = float(input("Introduce los grados celsius que quieres convertir: "))
resultado = celcius_a_farenheit(celsius_usuario)

print(f"{celsius_usuario} grados Celsius son {resultado} grados fahrenheit")