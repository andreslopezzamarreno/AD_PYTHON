arbolPrincipal = []

def constructor(numero):
    nodo = {'izq': None, 'valor': numero, 'der': None, 'raiz': None}
    return nodo

def esVacio(nodo):
    if nodo["izq"] == None and nodo ["der"] == None:
        return True
    else:
        return False

def insertar(arbol,numero):
    print(arbol)
    nodo2 = constructor(numero)
    if len(arbol) != 0:
        if esVacio(nodo2):
            print("vacio")
            for i in arbol:
                print(i.get("valor"))
                if i.get("valor") > nodo2.get("valor"):
                    i["izq"] = nodo2.get("valor")
                    arbolPrincipal = arbol.append(nodo2)
                    break
                else:
                    i["der"] = nodo2.get("valor")
                    arbolPrincipal = arbol.append(nodo2)
                    break
        else:
            for i in arbol:
                print(i)
            arbolPrincipal = arbol.append(nodo2)
    else:
        arbolPrincipal = arbol.append(nodo2)


insertar(arbolPrincipal,10)
insertar(arbolPrincipal,8)
insertar(arbolPrincipal,6)
print(arbolPrincipal)
