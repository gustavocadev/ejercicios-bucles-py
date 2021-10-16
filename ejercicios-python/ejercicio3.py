"""
Mejora el programa anterior para que muestre por separado la suma de los números pares y los
impares.
Ejemplo 1:
Introduce el número de inicio: 4
Introduce el número de fin: 8
Los pares suman 18 y los impares 12

Ejemplo 2:
Introduce el número de inicio: 10
Introduce el número de fin: 15
Los pares suman 36 y los impares 39
"""


def imprimir_respuesta(num1, num2):
    # Imprimir pares
    pares = 0
    for i in range(num1, num2+1, 2):
        pares += i
    print(f"los números pares son: {pares}")
    # Imprimir impares
    impares = 0
    for i in range(num1+1, num2+1, 2):
        impares += i
    print(f'los números impares son: {impares}')


# Pedir datos
num1 = int(input("ingrese un número: "))
num2 = int(input("ingrese otro número: "))

# invocar función
imprimir_respuesta(num1, num2)
