while True:
    a = int(input("Escriba un numero: "))

    if a != 0: 
        sumatoria = 0
        i = 1
        while i <= a:
            sumatoria += (1 / a) ** i
            print(f"{sumatoria}.")
            i += 1
    else:
        print("Otro que no sea 0.")
    
    break 
