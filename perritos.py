i = 1
lisperro = []
lisgato = []
conperros = 0
congato= 0
msj = "bienvenido al sistema veterinario de la udea"
print (f"{msj :>90}")
while i<20:
    menu = int(input("""Ingrese \n 
                 1 - ingresar nuevo paciente
                 2 - ver cantidad de pacientes
                 3 - mostrar promedio de edades
                 4 - cantidad de pacientes criticos y graves
                 5- ver paciente
                 6 - ver todos los pacientes
                 7 - salir
                 Ingrese: """))
    if menu <= 1:
        mas = []
        mas.append(input("nombre de la mascota: "))
        tipo= (int(input("Ingrese: \n 0 si es perro \n 1 si es gato")))
        if tipo == 0:
            mas.append("Perro")
        else:
            mas.append("gato)")
        mas.append(int(input("edad: ")))
        est = (int(input("ingrese /n0- Si es grave \n1- si es critico")))
        if est == 0:
            mas.append("grave")
        else:
            mas.append("critico")
        if tipo == 0:
            conperros+=1
            codigo="caninos{:03d}".format(conperros) 
            mas.append(codigo)
            lisperro.append(mas)
        elif tipo==1:
            congato+=1
            codigo="felinos{:03d}".format(conperros) 
            mas.append(codigo)
            lisgato.apend(mas)
    elif menu == 2:
        op=int(input("Ingrese 1 cantidad perros, o 2 cantidad gatos"))
        if op==1:
            print("hay {len(conperro)} perros en la lista")
        elif op==2:
            print("hay {len(congato)} gatos en la lista")
    elif menu == 3:
        sumedad = 0
        for i in lisgato:
            sumedad+= i[2]
        for i in lisperro:
            sumedad+= i[2]
        print(f"el promedio de edad es: {sumedad/(len(lisgato)+len(lisperro)):.2f}")
    elif menu == 4:
        graves = 0
        criticos = 0
        for i in lisgato:
            if i[3] == "grave":
                graves+=1
            elif i[3] == "critico":
                criticos+=1
        for i in lisperro:
             if i[3] == "grave":
                 graves+=1
             elif i[3] == "critico":
                 criticos+=1
        print(f"Hay {graves} pacientes graves y {criticos} pacientes criticos en el sistema.")
    elif menu == 5:
        codigo= input("ingrese el codigo del animal qur quiere ver").capitalize()
        if codigo.startswith("fe"):
            for i in lisgato:
                if i[4] == codigo:
                    print(f"nombre {i[0]} tipo: {i[1]} edad {i[2]} estado {i[3]} codigo {i[4]}")
    elif menu == 6:
        listo = lisperro + lisgato
        for i in listo:
            print(f"nombre {i[0]} tipo: {i[1]} edad {i[2]} estado {i[3]} codigo {i[4]}")
    elif menu == 7:
        fallos= 0
        while fallos < 3:
            SubMenu = input("\n1.Aceptar 🤙\n2.Rechazar ❌ 👌\n")
            
        
        if SubMenu == 1:
            break
        if SubMenu == 2 or SubMenu != 1:
            continue 
        
            
