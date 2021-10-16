contador = 0
while contador < 5:
    contador = contador+1
    if contador == 3:
        continue
    print("Iteración número {}".format(contador))
    print("¡Fin!")
