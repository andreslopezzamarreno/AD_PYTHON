lista = [1,2,3,4,8,100,1200,1201]
#buscar 1201 y el 2
num = int(input("Que numero quieres buscar"))

def buscar(listaNumeros,numero):
    mitad = len(listaNumeros)//2

    print(listaNumeros[mitad:])
    print(listaNumeros[mitad])

    if mitad < 1:
        if listaNumeros[mitad] == num:
            print("Numero Encrontrado")
            return num
        else:
            return print("Numero no encontrado")

    elif listaNumeros[mitad] > num:
        return buscar(listaNumeros[:mitad],numero)
    else:
        return buscar(listaNumeros[mitad:],numero)

'''def buscar2(listaNumeros,numero):
    mitad = len(listaNumeros)//2
    print(listaNumeros[mitad:])
    print(listaNumeros[mitad])

    if listaNumeros[mitad] == num:
        print("Numero Encrontrado")
        return num
    elif listaNumeros[mitad] > num:
        return buscar2(listaNumeros[:mitad],numero)
    else:
        return buscar2(listaNumeros[mitad:],numero)
'''
buscar(lista,num)