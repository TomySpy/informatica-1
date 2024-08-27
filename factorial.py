while True:
    numero = int(input("Escribe el numero: "))

    if 0 <= numero <= 20:
        factorial = 1
        i = numero
        while i > 1:
            factorial *= i
            i -= 1
        print(f"El factorial de {numero} es {factorial}")
    else:
        print("ese no se puede, usa otro que sea enre 0 y 20")
    
    continue  # This will restart the loop
