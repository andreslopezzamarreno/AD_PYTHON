def ordenacion(lista):
    pivote = lista[len(lista) - 1]
    i = -1
    j = 0
    jDos = 0
    if len(lista) < 2:
        listaFinal.append(lista[0])
        return lista[0]
    else:
        while j < len(lista):
            if lista[j] == pivote:
                i += 1
                jDos = j
                lista[j], lista[i] = lista[i], lista[j]

            elif lista[j] < pivote:
                i += 1
                lista[j], lista[i] = lista[i], lista[j]

            j += 1

        print(lista[:jDos])
        return ordenacion(lista[:jDos]),ordenacion(lista[jDos:])

listaNumeros = [40, 21, 4, 10, 9, 35]
listaFinal = []
ordenacion(listaNumeros)
print(listaFinal)

#SOLUCION LUISMI
def Partir(vector, bajo, alto):
    i = (bajo-1)
    pivote = vector[alto]
    for j in range(bajo, alto):
        if vector[j] <= pivote:
            i = i+1
            vector[i], vector[j] = vector[j], vector[i]
    vector[i+1], vector[alto] = vector[alto], vector[i+1]
    return (i+1)


def QuickSort(vector, bajo, alto):
    if len(vector) == 1:
        return vector
    if bajo < alto:
        vector_partido = Partir(vector, bajo, alto)
        QuickSort(vector, bajo, vector_partido-1)
        QuickSort(vector, vector_partido+1, alto)

vector = [10,7,8,9,1,5,4,12,25,65,3,2,6]
n = len(vector)

QuickSort(vector, 0, n-1)
print(vector)