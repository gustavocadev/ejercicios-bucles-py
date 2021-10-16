"""
Mejora el programa anterior para que solo permita 3 intentos. Cada vez vez que el usuario introduzca
datos de acceso incorrectos el programa mostrará el mensaje: “Datos incorrectos. Le quedan X
intentos.”, siendo X el número de intentos restantes. Tras el tercer fallo el programa mostrará el
mensaje “Has agotado todos tus intentos.” y finalizará.

Ejemplo:
    Introduce el nombre de usuario: root
    Introduce la contraseña: 123456
    Datos incorrectos. Le quedan 2 intentos.
    Introduce el nombre de usuario: root
    Introduce la contraseña: abcd
    Datos incorrectos. Le quedan 1 intentos.
    Introduce el nombre de usuario: root
    Introduce la contraseña: 123abc
    Datos incorrectos. Le quedan 0 intentos.

Has agotado todos tus intentos.
"""


x = 3
while x > 0:
    username = input("ingrese su nombre de usuario: ")
    password = input("ingrese su contraseña: ")
    if username == 'root' and password == 'toor':
        print("¡Bienvenido!")
        break
    x -= 1
    print(f"Datos incorrectos. Le quedan {x} intentos.\n")
else:
    print("Has agotado todos tus intentos.")
