matriz = [[0, 2, 5, 0],
          [0, 0, 1, 8],
          [0, 0, 0, 6],
          [0, 0, 0, 0]]  # matriz con listas de listas

nodos = ["A", "B", "C", "D"]  # lista con el nombre de los nodos

nodos2 = []  # Lista solución

for i in range(len(matriz)):  # con un for anidado recorro la matriz
    for j in range(len(matriz)):
        if matriz[i][j] != 0:  # cuando esa posición no sea cero está conectada
            print(f"{nodos[i]} se comunica con  {nodos[j]} y tiene un peso de {matriz[i][j]}")  # muestro por pantalla que nodos estan conectados, y el peso que tienen, para que el usuario tenga una idea
            nodos2.append([nodos[i], nodos[j], matriz[i][j]])  # voy añadiendo sublistas, con los nodos que se conectan y su peso

for r in range(len(nodos2)):
    for q in range(len(nodos2)):  # con un for anidado sumo pesos en función de si estan conectados o no.

        if nodos2[r][1] == nodos2[q][1] and nodos2[r] != nodos2[q]:  # condiciono que cuando un mismo nodo tiene dos caminos con dierentes valores para llegar

            if nodos2[r][2] > nodos2[q][2]:  # si tienen los dos en su subposicion el mismo valor, como indico arriba y no son el mismo nodo, que compare tamaños y elimine el mayor
                nodos2.pop(r)
                nodos2.insert(r, ["ELIMINADO", "ELIMINADO",
                                  "ELIMINADO"])
            else:  # si no es r el mayor, será q y entra en el else
                nodos2.pop(q)
                nodos2.insert(r, ["ELIMINADO", "ELIMINADO", "ELIMINADO"])

        # si subposicion 1 de r es igual a subposicion 0 de q, quiere decir que estan conectadas
        if nodos2[r][1] == nodos2[q][0]:

            # por lo que sumo sus pesos, el peso de q que esta en la
            # subposición 2, es igual al susodicho mas el de r.
            nodos2[q][2] = nodos2[q][2] + nodos2[r][2]

for y in range(len(nodos2)):  # recorro la lista ya sumada.
    # y cuando un nodo de la lista tenga en su subposición 1, el string D, que imprima su
    # peso, es decir, la subposicion 2, que es el peso total para llegar a D en este caso.
    if nodos2[y][1] == "D":
        print("\nEL TIEMPO MÍNIMO EN MINUTOS PARA LLEGAR A D ES: " + str(nodos2[y][2]))
        final = nodos2[y]

for borrar in range(len(nodos2) - 2):
    if nodos2[borrar] == ["ELIMINADO", "ELIMINADO", "ELIMINADO"]: #borro lo eliminado
        nodos2.pop(borrar)

print("-----------------",nodos2)

# Imprimo el camino en el orden correcto
posicion=len(nodos2)-1
for camino in reversed(nodos2):
    if posicion>1:
        print(camino[1])
    elif posicion==1:
        print(nodos2[posicion][1])
        if nodos2[posicion][0]==nodos2[0][1]:
            print(nodos2[posicion][0])
    else:
        print(nodos2[0][0])
    posicion -=1