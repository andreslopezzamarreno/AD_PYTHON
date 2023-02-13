listaNumeros = [40,21,4,9,10,35]

def ordenar2 (lista):
    for i in range(len(listaNumeros)):
        for j in range(len(listaNumeros)):
            if listaNumeros[i] < listaNumeros[j]:
                lista[j],lista[i] = lista[i],lista[j]
    print(lista)
ordenar2(listaNumeros)