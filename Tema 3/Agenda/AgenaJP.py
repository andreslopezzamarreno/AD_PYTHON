
seguir = True
try:
    fichero2 = "C:/Users/jgp19/Desktop/AD/miagenda.txt"

    with open(fichero2, "w") as f:
            f.write("Jorge,666666666 \n")
            f.write("Maria,777777777 \n")      
            f.write("Pedro,888888888 \n")
            f.write("Sara,999999999")  
            agenda = [
                "Jorge",666666666,
                "Maria",777777777, 
                "Pedro",888888888,
                "Sara",999999999
            ]

    f.close()
except FileNotFoundError:
    print("El archivo no existe")

print(agenda)
while seguir:
    print("¿Que desea hacer?")
    print("1. Crear fichero")
    print("2. Añadir contacto") 
    print("3. Consultar teléfono")
    print("4. Borrar contacto")
    print("5. Salir")
    opc = input()
    if opc == "1":
        input("¿Como desea que se llame el fichero?")
        fichero_nombre = input()
        fichero_usuario = open("C:/Users/jgp19/Desktop/AD/agenda_usuario.txt","w")
        print("Agenda creada.")

    elif opc == "2":
        nombre = input("Introduzca nombre: ")
        telefono = input("Introduzca telefono: ")
        agenda.append(nombre)
        agenda.append(telefono)
        print("Contacto añadido.")
        print(agenda)

    elif opc == "3":
        nombre = input("Introduzca nombre: ")
        if nombre in agenda:
            telefono = (agenda.index(nombre) + 1)
            print(nombre+","+str(agenda[telefono]))
        else:
             print("Ese nombre no existe.")

    elif opc == "4":
        nombre = input("Introduzca nombre a eliminar de la agenda: ")
        if nombre in agenda:
            telefono = (agenda.index(nombre) + 1)
            print(nombre+","+str(agenda[telefono]))
        
            agenda.pop(agenda.index(nombre) + 1)
            agenda.pop(agenda.index(nombre))
            print(agenda)
        else:
             print("Ese nombre no existe.")

    elif opc == "5":
        seguir = False
                

