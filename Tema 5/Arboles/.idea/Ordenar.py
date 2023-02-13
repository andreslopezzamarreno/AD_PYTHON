listaNumeros = [40,21,4,9,10,35]

for i in listaNumeros:
    for i in listaNumeros-1:
        if i>listaNumeros[i+1]:
            aux = listaNumeros[i+1]
            listaNumeros[i+1] = aux
            listaNumeros[i] = aux
