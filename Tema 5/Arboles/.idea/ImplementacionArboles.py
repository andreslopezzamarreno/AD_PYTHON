arbolPrincipal = {}

def constructor(numero):
    nodo = {'izq': None, 'valor': numero, 'der': None, 'raiz': None}
    return nodo

def esVacio(nodo):
    if nodo["izq"] == None:
        return True
    else:
        return False

def insertar(arbol,numero):
    nodo2 = constructor(numero)
    if len(arbol) != 0:
        if esVacio(nodo2):
            print("vacio")
            arbolPrincipal = arbol[str(numero)]= nodo2
        else:
            arbolPrincipal = arbol[str(numero)]= nodo2
    else:
        arbolPrincipal = arbol[str(numero)]= nodo2


insertar(arbolPrincipal,10)
print(arbolPrincipal)
print(arbolPrincipal)