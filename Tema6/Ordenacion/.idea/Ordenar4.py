listaNumeros = [40, 21, 4, 10, 9, 35]
listaFinal = []

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
                j += 1

            elif lista[j] < pivote:
                i += 1
                lista[j], lista[i] = lista[i], lista[j]
                j += 1

            else:
                j += 1

        print(lista[:jDos])
        return ordenacion(lista[:jDos]),ordenacion(lista[jDos:])

ordenacion(listaNumeros)

print(listaFinal)