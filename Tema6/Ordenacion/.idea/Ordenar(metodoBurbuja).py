def ordenar(lista):
    for i in range(len(listaNumeros)):
        for j in range(len(listaNumeros)-1):
            if listaNumeros[j]>listaNumeros[j+1]:
                aux = listaNumeros[j]
                listaNumeros[j] =  listaNumeros[j+1]
                listaNumeros[j+1] = aux

    print(listaNumeros)

listaNumeros = [40,21,4,9,10,35]
ordenar(listaNumeros)

#SOLUCION LUISMI
def ord_burbuja(array):
    n = len(array)
    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

elementos = [8, 3, 1, 19, 14]
ord_burbuja(elementos)
print(elementos)