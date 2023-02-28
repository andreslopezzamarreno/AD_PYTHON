'''grafo = [
    [0,2,5,8],
    [0,0,0,1],
    [0,0,0,7],
    [0,0,0,0]
]'''
grafo =[
    [0,1,0,0,0],
    [0,0,1,6,9],
    [0,0,0,1,2],
    [0,0,0,0,3],
    [0,0,0,0,0]
]
'''grafo =[
    [0,0,0,4,0],
    [0,0,0,0,0],
    [0,3,0,0,2],
    [0,0,2,0,1],
    [0,4,0,0,0]
]'''
#letras = ["A","B","C","D"]
letras = ["A","B","C","D","E"]
posibilidades2 = []
final = "E"

def Dijkstra(laberinto):
    minimo = 100
    posicion = ""

    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            valor = (letras[i]+letras[j]+str(laberinto[i][j]))
            if valor[2:] != "0":
                posibilidades2.append(valor)

                for k in range(len(posibilidades2)-1):
                    if posibilidades2[k][1] == valor[0]:
                        num = int(posibilidades2[k][2]) + int(valor[2])
                        posibilidades2[len(posibilidades2)-1] =posibilidades2[len(posibilidades2)-1][:2]+str(num)

                    if posibilidades2[k][0] == valor[1]:
                        num += int(posibilidades2[k][2])
                        posibilidades2[k] = posibilidades2[k][:2] + str(num)

    for i in posibilidades2:
        if i[1] == final and minimo > int(i[2:]):
            minimo = int(i[2:])
            posicion = i

    '''for i in reversed(posibilidades2):
        if posicion[:1] == i[1:2]:
            print(posicion[1:2])
            posicion = i
            print(f'i vale {i}')'''

    return f'El camino mas corto es llegando por {posicion}'


print(Dijkstra(grafo))
print(posibilidades2)
