"""
Crea un programa que reciba 5 números del usuario y muestre el mayor de todos por pantalla.
Ejemplo:
Introduce un número: 5
Introduce un número: -10
Introduce un número: 2
Introduce un número: 14
Introduce un número: 7
El número más alto es: 14
"""

numeros = []

for value in range(0, 5):
    num = int(input("ingrese un número: "))
    numeros.append(num)

numeros.sort()
print(f'El número más alto es: {numeros[-1]}')
