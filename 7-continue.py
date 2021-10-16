numeros = [4, 8, 2, 7, 1, 9, 3, 5]
total = 0

# solo sumar los números impares
for num in numeros:
    if num % 2 == 0:
        print("Numero par, no lo sumamos")
        continue
    total += num
