'''Implementa (al menos) las siguientes funcinones para almacenar datos en listas enlazadas y doblemente enlazadas:
- Crear_nodo
- Insertar_nodo
- Buscar_nodo
- Eliminar_nodo

Puedes ampliarlo con listas circulares.'''
def menu():
    # pregunto que opcion quiere el usuario
    print("¿Que quieres hacer?")
    print("1. Insertar_nodo")
    print("2. Buscar_nodo")
    print("3. Eliminar_nodo")
    print("4. Salir")
    elegir = int(input())
    return elegir

def Insertar_nodo(todos, nodo):
    '''longitud = len(todos)
    if longitud >= 1:
        for i in range(longitud):
            nodo1 = todos[i]
            print(nodo1[1],nodo[1])
            if nodo[1] < nodo1[1]:
                posicion = i-1
                todos.insert(0,nodo)
                print(todos)
                break
            elif nodo[1] >= nodo1[1]:
                print("klk")
                todos.append(nodo)
                break
    else:
        todos.append(nodo)'''

    longitud = len(todos)
    if longitud > 1:
        for i in range(longitud-1):
            for j in range(longitud-1-i):
                nodo1 = todos[j]
                nodo2 = todos[j+1]
                if nodo1[1] > nodo2[1]:
                    nodoExtra = nodo1
                    todos[j] = nodo2
                    todos[j+1] = nodoExtra

    for i in range(len(todos)-1):
        todos[i][0] = todos[i+1][1]
        todos[len(todos)-1][0] =99

    #print(todos)
    #return todos

def Buscar_nodo(listaTodos,nodo):
    print("Buscar_nodo")
    for i in listaTodos:
        if i[1] == nodo[1]:
            print(i)

def Eliminar_nodo(listaTodos,nodo):
    print("Eliminar_nodo")
    for i in range(len(listaTodos)-1):
      if nodo[1] == listaTodos[i][1]:
            listaTodos.pop(i)
    return listaTodos

def inicio():
    listaCompleta = []
    while True:
        opcion = menu()
        numero = int(input("Introduce un numero"))
        nodo = [0,numero]
        if opcion == 1:
            listaCompleta.append(nodo)
            Insertar_nodo(listaCompleta,nodo)
            print(listaCompleta)
            '''listaAux = Insertar_nodo(listaCompleta,nodo)
            listaCompleta = listaAux
            #print(listaCompleta)'''
        elif opcion == 2:
            Buscar_nodo(listaCompleta, nodo)
        elif opcion == 3:
            listaCompleta = Eliminar_nodo(listaCompleta, nodo)
            print(listaCompleta)
        elif opcion == 4:
            print("Salir")
            break;
        else:
            print("Opcion no valida")


inicio()