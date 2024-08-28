while True:
    a = int(input("Escriba un numero: "))
    n = int(input("Escriba la cantidad de sumas: "))

    if a != 0: 
        sumatoria = 0
        i = 1
        while i <= n:
            sumatoria += (1 / a) ** i
            print(f"{sumatoria}.")
            i += 1
   
