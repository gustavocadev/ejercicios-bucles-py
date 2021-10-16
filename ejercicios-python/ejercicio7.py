"""
Mejora el programa anterior, de forma que el usuario pueda introducir tantos números como quiera.
El programa solicitará números al usuario hasta que introduzca la palabra “fin”. Entonces mostrará
el mayor de todos por pantalla.
Ejemplo:
Introduce un número: 6
Introduce un número: 9
Introduce un número: 11
Introduce un número: 3
Introduce un número: 5
Introduce un número: fin
El número más alto es: 11
"""

numeros = []

while True:
    num = input("ingrese un número: ")
    if num.lower() == 'final':
        break
    else:
        numeros.append(num)

numeros = list(map(int, numeros))
numeros.sort()
print(f'El número más alto es: {numeros[-1]}')
