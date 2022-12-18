def consulta_Errores(file):
    print("Consulta errores")
    contador = 0
    
    try:
        # abro fichero modo lectura
        with open(file, "r") as f:
            fichero = f.readlines()
            for linea in fichero:
                # cuento numero de errores
                contador += 1
                print(linea)
        f.close()
        print(f"\nExisten {contador} errores\n")
    # controlo excepcion
    except FileNotFoundError:
        print("Documento no encontrado")


def Existe_Error(file1, file2):
    print("Existe Error")
    contador = 0
    try:
        # abro fichero en modo lectura
        with open(file2, "r") as f:
            # guardo documento en un diccionari clave-valor
            errores = f.readlines()
            errores = dict([tuple(line.split(',')) for line in errores])
        f.close()
        # abro fichero en modo lectura
        with open(file1, "r") as fi:
            # guardo documento en un diccionari clave-valor
            todos = fi.readlines()
            todos = dict([tuple(line.split(',')) for line in todos])
        fi.close()
        # compruebo cuantos errores coinciden
        for i in errores:
            if i in todos:
                if errores[i] == todos[i]:
                    contador += 1

        print(
            f"Tras comprobar concidencias entre el fichero control y errores se han encontrado {contador} coincidencias de errores")
    except FileNotFoundError:
        print("Documento no encontrado")


def Borrar_Errores(file1, file2):
    print("Borrar Errores")
    print(file1,file2)
    try:
        # abro archivo metodo lectura
        with open(file2, "r") as f:
            # guardo documento en un diccionari clave-valor

            errores = f.readlines()
            errores = dict([tuple(line.split(',')) for line in errores])
        f.close()
        with open(file1, "r") as fi:
            # guardo documento en un diccionari clave-valor
            #x28:y1:z0::ang0,-0.7990214786596245
            todos = fi.readlines()
            todos = dict([tuple(line.split(',')) for line in todos])
            # guardo antigua longitud antes de borrar
            longitud = len(todos)
            # compruebo cuantos errores coinciden
            for i in errores:
                if i in todos:
                    if errores[i] == todos[i]:
                        #borro del diccionario
                        del(todos[i])
            fi.close()

        with open(file1, "w") as fil:
            for i in todos:
                #print(i+","+todos[i])
                fil.write(i+","+todos[i])
        fil.close()

        print(f"Errores eliminados\n\tAntes {longitud} registros\n\tAhora: {len(todos)} registros")
    # controlo la excepcion
    except FileNotFoundError:
        print("Documento no encontrado")


def menu():
    # pregunto que opcion quiere el usuario
    print("¿Que quieres hacer?")
    print("1. Consultar Errores")
    print("2. Existe Error")
    print("3. Borrar Errores")
    print("4. Salir")
    elegir = int(input())
    return elegir


def inicio():
    # metodo para ver en que opcion entra
    ficheroTodos = "ficheroexam3.txt"
    ficheroErrores = "ficheroexam4.txt"
    while True:
        opcion = menu()
        if opcion == 1:
            consulta_Errores(ficheroErrores)
        elif opcion == 2:
            Existe_Error(ficheroTodos, ficheroErrores)
        elif opcion == 3:
            Borrar_Errores(ficheroTodos, ficheroErrores)
        elif opcion == 4:
            print("Salir")
            break
        else:
            print("Opcion no valida")


inicio()
