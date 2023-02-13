listaNumeros = [40,21,4,9,10,35]

def ordenar(lista):
    for i in range(len(listaNumeros)):
        for j in range(len(listaNumeros)-1):
            if listaNumeros[j]>listaNumeros[j+1]:
                aux = listaNumeros[j]
                listaNumeros[j] =  listaNumeros[j+1]
                listaNumeros[j+1] = aux

    print(listaNumeros)

