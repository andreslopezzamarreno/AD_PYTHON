listaNumeros = [40,21,4,9,10,35]

def ordenar2 (lista):
    for i in range(len(listaNumeros)):
        for j in range(len(listaNumeros)):
            if listaNumeros[i] < listaNumeros[j]:
                lista[j],lista[i] = lista[i],lista[j]
    print(lista)
ordenar2(listaNumeros)


#SOLUCION LUISMI
def alg_InsertSort(array):

    if (n := len(array)) <= 1:
        return

    for i in range(1, n):
        key = array[i]
        j = i-1
        while j >=0 and key < array[j] :
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key


lista = [40,21,4,9,10,35]
alg_InsertSort(lista)
print(lista)