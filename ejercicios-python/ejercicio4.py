"""
Escribe un programa que solicite al usuario un nombre de usuario y contraseña. El programa
mostrará el mensaje “¡Bienvenido!” si el usuario introduce los siguientes datos:
• Nombre de usuario: root
• Contraseña: toor

Si los datos de acceso son incorrectos mostrará el mensaje “Acceso fallido” y el programa finalizará.

Ejemplo 1:
Introduce el nombre de usuario: root
Introduce la contraseña: toor
¡Bienvenido!

Ejemplo 2:
Introduce el nombre de usuario: root
Introduce la contraseña: 123456
Acceso fallido
"""


def imprimir_respuesta(username, password):
    if username == 'root' and password == 'toor':
        print("¡Bienvenido!")
    else:
        print("Acceso fallido")


username = input("ingrese su nombre de usuario: ")
password = input("ingrese su contraseña: ")

imprimir_respuesta(username, password)
