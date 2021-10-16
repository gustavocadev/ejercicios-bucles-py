"""
Escribe un programa que solicite dos números enteros al usuario y muestre por pantalla la suma de
todos los números enteros que hay entre los dos números (ambos números incluidos).
Ejemplo 1:
    Introduce el número de inicio: 4
    Introduce el número de fin: 8
    El resultado es: 30
Ejemplo 2:
    Introduce el número de inicio: 10
    Introduce el número de fin: 15
    El resultado es: 75
"""


def sumar_numeros(num1, num2):
    acumular = 0
    for i in range(num1, num2+1):
        acumular += i
    print(f"El resultado es: {acumular}")


num1 = int(input("ingrese un número: "))
num2 = int(input("ingrese otro número: "))

sumar_numeros(num1, num2)
