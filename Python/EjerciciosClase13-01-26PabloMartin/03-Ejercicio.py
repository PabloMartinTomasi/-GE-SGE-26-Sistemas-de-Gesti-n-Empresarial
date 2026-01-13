salario = float(input("Ingresa el salario mensual: "))

if(salario > 1000):
    bono = salario * 0.10
    salarioFinal = salario + bono
    print(f"El salario es de: {salarioFinal}€")
else:
    print(f"El salario es de: {salario}€")