num = int(input("Introduzca el número de notas que vas a poner: "))
suma = 0.0
cont = 0
while cont < num:
    nota = float(input("Introduce la nota: "))
    while nota < 0 or nota > 5:
        print("Esa no se puede. Debe estar entre 0 y 5.")
        nota = float(input(f"Introduce la nota {contador + 1} (de 0 a 5): "))
    suma += nota
    cont += 1

prom = suma / num
print(f"El promedio de las notas es {prom} :D")