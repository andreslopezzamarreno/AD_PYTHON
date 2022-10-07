"""estribir un prog que lea 4 nums por teclado y muestre por pantalla el mayor"""

max = -99999
for i in range(4):
    num  = int(input("Dime un numero: "))
    if (num > max): max = num
print('El mayor numero introducido es el:',max)