intentos = 0

print("\n*** INICIO DE SESION ***")
nombre_usuario = input("\nIngresa tu nombre de usuario: ")

while intentos < 3:
    contrasena = input("\nIngresa tu contrasena: ")

    if nombre_usuario == "Juan" and contrasena == "123":
        print(f"Bienvenido, {nombre_usuario}!")
        break

    print("Contrasena incorrecta.")
    intentos += 1

else:
    print("\nAcceso bloqueado")
    print("Has superado el numero maximo de intentos")
