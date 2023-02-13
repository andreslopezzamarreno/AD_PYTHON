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