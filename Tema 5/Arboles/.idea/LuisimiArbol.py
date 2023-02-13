#colores:https://python-para-impacientes.blogspot.com/2016/09/dar-color-las-salidas-en-la-consola.html

# LIBRERÍAS
from time import sleep

# VARIABLES
prog = True
prog1 = True
prog_seleccion = int()
titulo = str('\n\033[32m █████╗ ██████╗ ██████╗  █████╗ ██╗     ███████╗ ██████╗\n'
             '██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝██╔════╝\n'
             '███████║██████╔╝██████╦╝██║  ██║██║     █████╗  ╚█████╗ \n'
             '██╔══██║██╔══██╗██╔══██╗██║  ██║██║     ██╔══╝   ╚═══██╗\n'
             '██║  ██║██║  ██║██████╦╝╚█████╔╝███████╗███████╗██████╔╝\n'
             '╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚════╝ ╚══════╝╚══════╝╚═════╝')

arbol = []
nodo = int()
valor_buscar = int()
visualizacion = False

# FUNCIONES
def puntos():
    for i in range(3):
        print('🌳', end=' ', flush=True)
        sleep(0.5)
    print('')

def EsVacio(arbol_EsVacio, valor_EsVacio): # Si el nodo contiene un 0 (none), está vacío
    for i in range(len(arbol_EsVacio)):
        if valor_EsVacio == None:
            return True
        else:
            return False

def Constructor(valor_Constructor): # Se construye nodo con valor del usuario y los demás lugares ocupan 0=none
    nodo_constructor = {'valor': valor_Constructor,
                        'padre': None,
                        'hijo_iz': None,
                        'hijo_dr': None}
    return nodo_constructor

def Insertar(arbol_Insertar, ubicacion_Insertar, nuevo_nodo_Insertar):
    if nuevo_nodo_Insertar != 0:     # si no entra un 0 que era terminar de insertar:
        if len(arbol_Insertar) == 0:   # si el arbol no tiene nada, está completamente vacío
            nuevo_nodo_Insertar = Constructor(nuevo_nodo_Insertar)
            arbol_Insertar.append(nuevo_nodo_Insertar)

        else:        # si el árbol tiene raíz:
            if nuevo_nodo_Insertar < arbol_Insertar[ubicacion_Insertar]['valor']:
                if EsVacio(arbol_Insertar, arbol_Insertar[ubicacion_Insertar]['hijo_iz']) == True:  #es vacío el subarbol izquierdo->inserto datos
                    nuevo_nodo_Insertar = Constructor(nuevo_nodo_Insertar)
                    arbol_Insertar.append(nuevo_nodo_Insertar)
                    arbol_Insertar[ubicacion_Insertar]['hijo_iz'] = nuevo_nodo_Insertar['valor']
                    arbol_Insertar[-1]['padre'] = arbol_Insertar[ubicacion_Insertar]['valor']

                else:       #subarbol izquierdo NO vacío, hago recursividad sobre ese subarbol izquierdo.
                    for i in range(len(arbol_Insertar)):  # busco la posición del diccionario con la información de la raíz del subarbol izquierdo
                        if arbol_Insertar[i]['valor'] == arbol_Insertar[ubicacion_Insertar]['hijo_iz']:
                            pos_insertar = i
                    Insertar(arbol_Insertar, pos_insertar, nuevo_nodo_Insertar)   #inserto (recursivo) del subarbol izquierdo, indicado en la posición y con el valor a insertar
            # igual para el subarbol derecho
            elif nuevo_nodo_Insertar > arbol_Insertar[ubicacion_Insertar]['valor']:
                if EsVacio(arbol_Insertar, arbol_Insertar[ubicacion_Insertar]['hijo_dr']) == True:
                    nuevo_nodo_Insertar = Constructor(nuevo_nodo_Insertar)
                    arbol_Insertar.append(nuevo_nodo_Insertar)
                    arbol_Insertar[ubicacion_Insertar]['hijo_dr'] = nuevo_nodo_Insertar['valor']
                    arbol_Insertar[-1]['padre'] = arbol_Insertar[ubicacion_Insertar]['valor']

                else:
                    for i in range(len(arbol_Insertar)):
                        if arbol_Insertar[i]['valor'] == arbol_Insertar[ubicacion_Insertar]['hijo_dr']:
                            pos_insertar = i
                    Insertar(arbol_Insertar, pos_insertar, nuevo_nodo_Insertar)

def Buscar(arbol_Buscar, valor_Buscar): # Función para buscar nodo, y mostrar su padre, hijos y hermano
    encontrado_buscar = False # En caso de ser encontrado -> var = True

    for i in range(len(arbol_Buscar)): # Buscamos nodo con el valor a buscar y si aparece, variable pasa a True
        if arbol_Buscar[i]['valor'] == valor_Buscar:
            encontrado_buscar = True
    if encontrado_buscar == True:
        print('Nodo encontrado: ' + '\033[32m' + str(encontrado_buscar) + '\033[0m')
        for i in range(len(arbol_Buscar)):
            if arbol_Buscar[i]['valor'] == valor_Buscar: # Buscamos el nodo y mostramos su padre e hijos
                print('Padre: \033[34m' + str(arbol_Buscar[i]['padre']) + '\n\033[0mHijo izquierdo: \033[34m' + str(arbol_Buscar[i]['hijo_iz']) + '\n\033[0mHijo derecho: \033[34m' + str(arbol_Buscar[i]['hijo_dr']))
        for i in range(len(arbol_Buscar)): # Buscamos el nodo otra vez
            if arbol_Buscar[i]['valor'] == valor_Buscar:
                if arbol_Buscar[i]['padre'] != 0: # En caso de que no haya padre, no busca el hermano
                    for j in range(len(arbol_Buscar)): # Buscamos el padre del nodo
                        if arbol_Buscar[j]['valor'] == arbol_Buscar[i]['padre']:
                            if arbol_Buscar[j]['hijo_iz'] != encontrado_buscar: # Si el nodo no coincide con su padre_hijo_izquierda, lo mostramos
                                print('\033[0mHermano: \033[34m' + str(arbol_Buscar[j]['hijo_iz']) + '\033[0m')
                            else:
                                print('\033[0mHermano: \033[34m' + str(arbol_Buscar[j]['hijo_dr']) + '\033[0m')

    else:
        print('Nodo encontrado: ' + '\033[31m' + str(encontrado_buscar) + '\033[0m') # Nodo no encontrado

def Visualizar(arbol_Visualizar): # Función para ver el árbol
    print('')
    for i in range(len(arbol_Visualizar)):
        print('\033[0mValor: \033[34m' + str(arbol_Visualizar[i]['valor']) + '\t\t' + '\033[0m        Predecesor: \033[34m' + str(arbol_Visualizar[i]['padre']) + '\t\t' +  '\033[0m        Hijo Izquierda: \033[34m' + str(arbol_Visualizar[i]['hijo_iz']) + '\t\t' +  '\033[0m        Hijo Derecha: \033[34m' + str(arbol_Visualizar[i]['hijo_dr']))

def NumeroHojas(arbol_NumeroHojas): # Función que cuenta el número de hojas
    if len(arbol_NumeroHojas) > 0: # Si el árbol está creado
        lista_hojas = []
        for i in range(len(arbol_NumeroHojas)):
            if arbol_NumeroHojas[i]['hijo_iz'] == None and arbol_NumeroHojas[i]['hijo_dr'] == None: # Buscamos los valores que no tengan hijos
                lista_hojas.append(arbol_NumeroHojas[i]['valor']) # Los guardamos en la lista de hojas
        lista_hojas.sort() # Ordenamos la lista de menor a mayor
        lista_hojas = [str(x) for x in lista_hojas] # Convertimos los números enteros a strings (Para separarlos por comas sin que aparezca una al final)
        print('\nEl número de hojas es \033[34m' + str(len(lista_hojas)) + '\033[0m y son los nodos: \033[34m')
        print(*lista_hojas, sep=', ')
    else:
        print('\n\033[1;31m¡Primero debes generar un árbol! 🌳\033[0m')

def NumeroNodos(arbol_NumeroNodos): # Función que cuenta el número de nodos
    print('\nEl número de nodos que contiene el árbol es \033[34m' + str(len(arbol_NumeroNodos)) + '\033[0m')

def EliminarArbol(arbol_EliminarArbol):
    if len(arbol_EliminarArbol) > 0:
        arbol_EliminarArbol.clear()
        print('\nEliminando árbol...')
        puntos()
        print('\033[31mÁrbol eliminado.\033[0m')
        return arbol_EliminarArbol
    else:
        print('\n\033[1;31m¡Primero debes generar un árbol! 🌳\033[0m')

# MAIN
while prog == True:
    prog, prog1 = True, True
    print(titulo)
    while prog1 == True:
        prog1 = True
        print('\n\n\033[0;32m1- Generar un árbol o insertar más nodos ➕\n2- Ver árbol 🌳\n3- Buscar nodo 🔎\n4- Número hojas 🍃\n5- Número de nodos ❓\n6- Eliminar árbol  ⚠️ \n7- Finalizar\033[0m\n')
        prog_seleccion = int(input('\n\033[0;3;1m¿Qué quieres hacer?: \033[0m'))
        while prog_seleccion < 1 or prog_seleccion > 7:
            print('\033[31mERROR.\tElija una opción entre 1 y 7\n')
            prog_seleccion = int(input('\033[0;3;1m¿Qué quieres hacer?: \033[0m'))

        if prog_seleccion == 1: # Generar un árbol o insertar más nodos
            print('\n\033[31;1m                          ATENCIÓN.\n\n- SOLO FUNCIONA CON \033[4mNÚMEROS ENTEROS.\033[0m')
            nodo = int(1)
            while nodo != 0:  # con 0 se sale de insertar
                nodo = int(input('\n\033[0;1mIntroduzca el nodo (Pulse 0 en cualquier momento para salir): \033[0m'))
                Insertar(arbol, 0, nodo)  #inserto en un árbol, en una posición, el valor del nodo
                Visualizar(arbol)
                visualizacion = True

        elif prog_seleccion == 2:
            Visualizar(arbol)

        elif prog_seleccion == 3: # Buscar nodo
            if len(arbol) > 0:
                valor_buscar = int(input('\n\033[1mIntroduce el nodo que quieres buscar: \033[0m'))
                puntos()
                Buscar(arbol, valor_buscar)
            else:
                print('\n\033[1;31m¡Primero debes generar un árbol! 🌳\033[0m')

        elif prog_seleccion == 4: # Número de hojas
            NumeroHojas(arbol)

        elif prog_seleccion == 5: # Número de nodos
            NumeroNodos(arbol)

        elif prog_seleccion == 6: # Eliminar árbol
            EliminarArbol(arbol)

        elif prog_seleccion == 7:
            print('\033[32:1mADIOS! 🤝')
            exit()