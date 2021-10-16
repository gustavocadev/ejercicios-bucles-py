"""
Crea un programa que solicite un número al usuario y devuelva el siguiente mensaje:
    • Si es mayor que 0: “Es un número positivo.”
    • Si es igual a 0: “Es igual a cero.
    • Si es menor que 0: “Es un número negativo.”
Ejemplo 1:
Introduce un número: 5
Es un número positivo

Ejemplo 2:
Introduce un número: -3
Es un número negativo
"""


def imprimirDatos(num):
    if num > 0:
        print("Es un número positivo")
    if num == 0:
        print("es igual a cero")
    if num < 0:
        print("Es un número negativo")


num = int(input("ingrese un número: "))
imprimirDatos(num)
