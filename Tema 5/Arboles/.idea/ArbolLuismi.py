# VARIABLES
arbol = []

# FUNCIONES
def EsVacio(arbol_EsVacio, valor_EsVacio):  # Si el nodo contiene un 0 (none), está vacío
    for i in range(len(arbol_EsVacio)):
        if valor_EsVacio == None:
            return True
        else:
            return False

def Constructor(valor_Constructor):  # Se construye nodo con valor del usuario y los demás lugares ocupan 0=none
    nodo_constructor = {'valor': valor_Constructor,
                        'padre': None,
                        'hijo_iz': None,
                        'hijo_dr': None}
    return nodo_constructor

def Insertar(arbol_Insertar, ubicacion_Insertar, nuevo_nodo_Insertar):
    if nuevo_nodo_Insertar != 0:  # si no entra un 0 que era terminar de insertar:
        if len(arbol_Insertar) == 0:  # si el arbol no tiene nada, está completamente vacío
            nuevo_nodo_Insertar = Constructor(nuevo_nodo_Insertar)
            arbol_Insertar.append(nuevo_nodo_Insertar)

        else:  # si el árbol tiene raíz:
            if nuevo_nodo_Insertar < arbol_Insertar[ubicacion_Insertar]['valor']:
                posicion = 'hijo_iz'
            else:
                posicion = 'hijo_dr'

            if EsVacio(arbol_Insertar, arbol_Insertar[ubicacion_Insertar][f'{posicion}']) == True:  # es vacío el subarbol izquierdo->inserto datos
                nuevo_nodo_Insertar = Constructor(nuevo_nodo_Insertar)
                arbol_Insertar.append(nuevo_nodo_Insertar)
                arbol_Insertar[ubicacion_Insertar][f'{posicion}'] = nuevo_nodo_Insertar['valor']
                arbol_Insertar[-1]['padre'] = arbol_Insertar[ubicacion_Insertar]['valor']

            else:  # subarbol izquierdo NO vacío, hago recursividad sobre ese subarbol izquierdo.
                for i in range(len(arbol_Insertar)):  # busco la posición del diccionario con la información de la raíz del subarbol izquierdo
                    if arbol_Insertar[i]['valor'] == arbol_Insertar[ubicacion_Insertar][f'{posicion}']:
                        pos_insertar = i
                Insertar(arbol_Insertar, pos_insertar,nuevo_nodo_Insertar)  # inserto (recursivo) del subarbol izquierdo, indicado en la posición y con el valor a insertar

def Buscar(arbol_Buscar, valor_Buscar):  # Función para buscar nodo, y mostrar su padre, hijos y hermano
    encontrado_buscar = None  # En caso de ser encontrado -> var = True
    for i in range(len(arbol_Buscar)):  # Buscamos nodo con el valor a buscar y si aparece, variable pasa a True
        if arbol_Buscar[i]['valor'] == valor_Buscar:
            encontrado_buscar = arbol_Buscar[i]
            break
    if encontrado_buscar!= None:
        print('Nodo encontrado: ' + True)
        print('Padre: ' + str(encontrado_buscar['padre']) )
        print('Hijo izquierdo: ' + str(encontrado_buscar['hijo_iz']) )
        print('Hijo derecho: ' + str(encontrado_buscar['hijo_dr']) )

        if encontrado_buscar['padre'] != 0:  # En caso de que no haya padre, no busca el hermano
            for j in range(len(arbol_Buscar)):  # Buscamos el padre del nodo
                if arbol_Buscar[j]['valor'] == arbol_Buscar[i]['padre']:
                    if arbol_Buscar[j]['hijo_iz'] != encontrado_buscar:  # Si el nodo no coincide con su padre_hijo_izquierda, lo mostramos
                        print('Hermano: ' + str(arbol_Buscar[j]['hijo_iz']))
                    else:
                        print('Hermano: ' + str(arbol_Buscar[j]['hijo_dr']))
    else:
        print('Nodo encontrado: ' +  str(encontrado_buscar))  # Nodo no encontrado

def Visualizar(arbol_Visualizar):  # Función para ver el árbol
    print('')
    for i in range(len(arbol_Visualizar)):
        print('Valor: ' + str(arbol_Visualizar[i]['valor']) + '\t\t' +
              'Padre: ' + str(arbol_Visualizar[i]['padre']) + '\t\t' +
              'Hijo Izquierda: ' + str(arbol_Visualizar[i]['hijo_iz']) + '\t\t' +
              'Hijo Derecha: ' + str(arbol_Visualizar[i]['hijo_dr']))

def NumeroHojas(arbol_NumeroHojas): # Función que cuenta el número de hojas
    if len(arbol_NumeroHojas) > 0:  # Si el árbol está creado
        contador = 0
        for i in range(len(arbol_NumeroHojas)):
            if arbol_NumeroHojas[i]['hijo_iz'] == None and arbol_NumeroHojas[i][
                'hijo_dr'] == None:  # Buscamos los valores que no tengan hijos
                contador += 1  # Los guardamos en la lista de hojas
        print('\nEl número de hojas es ' + str(contador))
    else:
        print('\n¡Primero debes generar un árbol! ')

def NumeroNodos(arbol_NumeroNodos):  # Función que cuenta el número de nodos
    print('\nEl número de nodos que contiene el árbol es ' + str(len(arbol_NumeroNodos)))

def EliminarArbol(arbol_EliminarArbol):
    arbol_EliminarArbol.clear()
    print('Árbol eliminado.')

# MAIN
def menu():
    print('\n1- Generar un árbol o insertar más nodos \n2- Ver árbol \n3- Buscar nodo \n4- Número hojas \n5- Número de nodos '
          '\n6- Eliminar árbol \n7- Finalizar\n')
    elegir = int(input('¿Qué quieres hacer?:'))
    return elegir

def inicio():
    while True:
        prog_seleccion = menu()

        if(prog_seleccion < 1 or prog_seleccion > 7):
            print('ERROR.\tElija una opción entre 1 y 7\n')
            prog_seleccion = int(input('¿Qué quieres hacer?:'))

        elif prog_seleccion == 1:  # Generar un árbol o insertar más nodos
            print('\n\t\t\tATENCIÓN.\nSOLO FUNCIONA CON NÚMEROS ENTEROS.')
            nodo = 1
            while nodo != 0:  # con 0 se sale de insertar
                nodo = int(input('\nIntroduzca el nodo (Pulse 0 en cualquier momento para salir): '))
                Insertar(arbol, 0, nodo)  # inserto en un árbol, en una posición, el valor del nodo
                Visualizar(arbol)
                visualizacion = True

        elif prog_seleccion == 2:
            Visualizar(arbol)

        elif prog_seleccion == 3:  # Buscar nodo
            if len(arbol) > 0:
                valor_buscar = int(input('\nIntroduce el nodo que quieres buscar: '))
                Buscar(arbol, valor_buscar)
            else:
                print('\n¡Primero debes generar un árbol!')

        elif prog_seleccion == 4:  # Número de hojas
            NumeroHojas(arbol)

        elif prog_seleccion == 5:  # Número de nodos
            NumeroNodos(arbol)

        elif prog_seleccion == 6:  # Eliminar árbol
            EliminarArbol(arbol)

        elif prog_seleccion == 7: # Salir
            print('ADIOS!')
            exit()

inicio()