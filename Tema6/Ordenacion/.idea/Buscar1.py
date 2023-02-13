
numeros =[1,8,7,2,15,21,17,4]
num = int(input("Que numero quieres buscar"))

def klk():
    for i in range(len(numeros)):
        if numeros[i] == num:


            prin(f'Numero encontrado en la posicion {i}')
            break

klk()