
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#forma clasica de crear un archivo:
#creamo el archivo
'''f = open("archivotext-excepciones.txt","w")
f.write("prbando excepciones")
f.close()

nombre_fichero = "archivotext-excepciones2.txt"

try:
    with open(nombre_fichero,"r") as f:
        print(f.read())
except FileNotFoundError:
    print("No existe el fichero")'''

"""
escribe un programa que pida por teclado un numero positivo entre 1 y 100 y lo guarde en un fichero llamado ejercicio1-100.txt
"""
#opcion 1
'''f = open("ejercicio1-100.txt","w")
numero = input("Dime un numero del 1 al 100")
f.write(numero)
f.close()'''
#opcion 2
'''#!/usr/bin/env python
# -*- coding:utf-8 -*-
n = int(input("Introduce un numero entre 1 y 100"))
nombre_fichero = "ejercicio1-100.txt"
with open(nombre_fichero, 'w') as f:
    f.write(str(n))
f.close()'''

"""
escribe un progrma aque pida por teclado un numero positivo entre 1 y 10 y guarde en un fillero
llamado ejercicio2-tabla.txt la tabla de multiplicar(sin contar el 0) del numero introducido
"""
'''f = open("ejercicio2-tabla.txt","w")
numero = int(input("Dime un numero del 1 al 10"))
for i in range(1,11):
    f.write(str(numero) + ' X ' + str(i)+'\n')
f.close()'''

"""
escribe programa que escriba todas las tablas de multiplicar
"""
'''f = open("ejercicio2-tabla.txt","w")
numero = int(input("Dime un numero"))
for n1 in range(1,numero +1):
    for n2 in range(0,11):
        print(f'{n1} x {n2} = {n1*n2}')
f.close()'''

"""
 modificar el ej 2 para que el fichero tenga el nombre del número con el que se crea la tabla de multiplicar.
 por ejemplo si es la del 9 que el fichero se llame "ejercicio2-tabla-del-9.txt"
"""
'''numero = int(input("Dime un numero del 1 al 10"))
fichero = 'ejercicio2-tabla del ' + str(numero)+ '.txt'
f= open(fichero,"w")
for i in range(1,11):
    f.write(str(numero) + ' X ' + str(i)+'\n')
f.close()'''

"""
escribe un progrma que pida un numero entero positivo n entre 1-10
y en base al numero leido, busque el fichero llamado: "fichero-tabla"
del-n.txt. este fichero contendra la tabla de multiplicar del numero n
introducido por teclado y debera mostrarse por pantalla. si el fichero no existe,
debera indicarse por pantalla por pantalla con un mensaje que avise del problema
"""
'''numero = int(input("Dime un numero del 1 al 10"))

nombre_fichero = 'ejercicio2-tabla del ' + str(numero) + '.txt'

try:
    with open(nombre_fichero,"r") as f:
        print(f.read())
except FileNotFoundError:
    print("No existe el fichero")'''

"""
escribir un programa en python que lea un numero n por teclado y
 a partir de ese numero, lea las n primeras lineas del fichero creado en el ej2
"""
numero = int(input("Dime un numero del 1 al 10"))

nombre_fichero = 'ejercicio2-tabla del 1.txt'
with open(nombre_fichero,"r") as f:
    texto = (linea for i, linea in enumerate(f) if i>= 0 and i<numero)
    for linea in texto:
        print(linea)
