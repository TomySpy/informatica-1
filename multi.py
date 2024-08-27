
n = int(input("Escribe el primer número: "))
u = int(input("Escribe el segundo número: "))

res = 0
cont = 0

while cont< u:
    res += n
    cont += 1
    print (res)
print(f"La multiplicación de {n} y {u} es {res}.")
