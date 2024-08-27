
n = int(input("Escribir la base: "))
if n < 0 or n > 9:
    print("Debes poner uno no mayor a 9")
    n = int(input("Escribe la base: "))
x = 0
while x <= 9:
    potencia = n ** x
    print(f" el resultado de {n} ^ {x} es {potencia}")
    x += 1

