n = int(input("Escribe el numero: "))

suma = 0
indicador = 1

while indicador <= n:
    if indicador % 2 != 0:  
        suma += indicador
    indicador += 1

print(f"La suma de los impares desde 1 hasta {n} es {suma} :D ")
