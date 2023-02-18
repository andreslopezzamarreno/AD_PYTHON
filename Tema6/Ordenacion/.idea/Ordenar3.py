listaNumeros = [40,21,4,9,10,35]

def dividir(listaNumero):
    if len(listaNumero)<2:
        return listaNumero
    else:
        mitad = len(listaNumero)//2
        return ordenar(dividir(listaNumero[:mitad]),dividir(listaNumero[mitad:]))

def ordenar(lista1,lista2):
    listaNum = []
    i = 0
    j = 0
    while (len(lista2) > j) and (len(lista1) > i):
        if lista1[i]>lista2[j]:
            listaNum.append(lista2[j])
            j = j+1
        else:
            listaNum.append(lista1[i])
            i = i+1
    listaNum += lista1[i:]
    listaNum += lista2[j:]
    return listaNum

listaNumeros = dividir(listaNumeros)
print(listaNumeros)






#SOLUCION LUISMI

# Función merge_sort
def merge_sort(lista):
    """
    Lo primero que se ve en el psudocódigo es un if que
    comprueba la longitud de la lista. Si es menor que 2 (1 ó 0) se devuelve la lista.
    ¿Por que? Ya esta ordenada.
    """
    if len(lista) < 2:
        return lista
    # De lo contrario, se divide en 2
    else:
        middle = len(lista) // 2
        right = merge_sort(lista[:middle])
        left = merge_sort(lista[middle:])
        return merge(right, left)
        #return(merge(merge_sort(lista[:middle]),merge_sort(lista[middle:])))

# Función merge
def merge(lista1, lista2):
    """
    merge se encargara de intercalar los elementos de las dos
    divisiones.
    """
    i, j = 0, 0 # Variables de incremento
    result = [] # Lista de resultado

    # Intercalar ordenadamente
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1

    # Agregamos los resultados a la lista
    result += lista1[i:]
    result += lista2[j:]

    # Retornamos el resultados
    return result

# Prueba del algoritmo

lista = [40,21,4,9,10,35]

print(merge_sort(lista))