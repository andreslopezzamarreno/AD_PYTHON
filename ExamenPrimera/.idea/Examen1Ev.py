#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#Pregunta 5
while True:
    try:
        #pedir numero
        opcion=int(input("Introduce una opción del 1 al 3:"))
        if opcion==1:
            print("opción 1")
        elif opcion==2:
            print("opción 2")
        elif opcion==3:
            print("opcion 3")
        else:
            #se se pulsa cualquier cosa diferente a 1,2,3 break que rompe la ejecucion
            break
    #coger excepcion
    except ValueError:
        print('Ha pulsado una tecla, por favor introduzca un número')

#Pregunta 6
#creacion del diccionario y a la vez pidiendo los datos para meterlos en la clave
diccionario = {
    'nombre': input("¿nombre?"),
    'apellido': input("¿Primer apellido?"),
    'edad': int(input("¿edad?")),
    'telefono': int(input("¿Telefono?"))
}
#imprimir datos
print(f"{midiccionario['nombre']} {midiccionario['apellido']} tiene {midiccionario['edad']} años y su telefono es {midiccionario['telefono']}")

#Pregunta 7.A
#abro archivo en modo escritura
with open ("ficheroexam1.txt", "w") as f:
    f.write("-----------\n")
    #pido numero por consola
    numero = int(input("Escribe un numero mayor que 0"))
    for numero in range(numero+1):
        #escribo en el achivo
        f.write(f"El numero es:{str(numero)}\n")
f.close()

#Pregunta 7.B
#abro archivo en modo escritura al final
with open ("ficheroexam1.txt", "a") as f:
    f.write("-----------\n")
    #pido numero por consola
    numero = int(input("Escribe un numero mayor que 0"))
    for numero in range(numero+1):
        #escribo en el achivo
        f.write(f"El numero es:{str(numero)}\n")
f.close()



#Pregunta 8.A
#pido numeros por consola
nA = int(input("Numero 1"))
nB = int(input("Numero 2"))
nC = int(input("Numero 3"))

#metodo de la operacion
def operacion(A,B,C):
    return (A+B)*C

resultado = operacion(nA,nB,nC)
#abro archivo en modo escritura
with open ("ficheroexam2.txt", "w") as f:
    #recorro resultado veces
    for line in range(resultado):
        #escribo en el fichero
        f.write(f"El Resultado es: {resultado} y esta es la linea {line+1}\n")
f.close()


#Pregunta 8.B
#pido numeros por consola
nA = int(input("Numero 1"))
nB = int(input("Numero 2"))
nC = int(input("Numero 3"))

#metodo de la operacion
def operacion(A,B,C):
    return (A+B)*C

resultado = operacion(nA,nB,nC)
#abro archivo en modo lectura-escritura
with open ("ficheroexam2.txt", "w+") as f:
    #recorro resultado veces
    for line in range(resultado):
        #escribo en el fichero
        f.write(f"El Resultado es: {resultado} y esta es la linea {line+1}\n")
f.close()
#abro fichero modo lectura
with open ("ficheroexam2.txt", "r") as f:
    #guardo el numero de las lineas que quiero mostrar
    texto=(linea for i,linea in enumerate(f) if i>=0 and i<nA+nB)
    print(f"Ahora se mostrara el contenido de calcular {nA} + {nB} = {nA+nB} ")
    #muestro las lineas
    for linea in texto:
        print(linea)
f.close()

#Pregunta 8.C
#pido numeros por consola
nA = int(input("Numero 1"))
nB = int(input("Numero 2"))
nC = int(input("Numero 3"))
#metodo de la operacion
def operacion(A,B,C):
    return (A+B)*C

resultado = operacion(nA,nB,nC)

#abro archivo en modo lectura-escritura
with open ("ficheroexam2.txt", "w+") as f:

    #recorro resultado veces
    for line in range(resultado):
        #escribo en el fichero
        f.write(f"El Resultado es: {resultado} y esta es la linea {line+1}\n")
f.close()

fichero = "ficheroexam2.txt"

try:
    #abro fichero modo lectura
    with open (fichero, "r") as f:
        #guardo el numero de las lineas que quiero mostrar
        texto=(linea for i,linea in enumerate(f) if i>=0 and i<nA+nB)
        #muestro las lineas
        for linea in texto:
            print(linea)
    f.close()
#controlo la excepcion
except FileNotFoundError:
    print(f"el fichero {fichero} no existe!")
'''
#Pregunta 9

def consulta_Errores(file):
    print("Consulta errores")
    contador = 0
    try:
        #abro fichero modo lectura
        with open (file, "r") as f:
            fichero = f.readlines()
            for linea in fichero:
                #cuento numero de errores
                contador += 1
                print(linea)
        f.close()
        print(f"\nExisten {contador} errores\n")
    #controlo excepcion
    except FileNotFoundError:
        print("Documento no encontrado")

def Existe_Error(file1,file2):
    print("Existe Error")
    contador = 0
    try:
        #abro fichero en modo lectura
        with open (file2, "r") as f:
            #guardo documento en un diccionari clave-valor
            errores = f.readlines()
            errores = dict([tuple(line.split(',')) for line in errores])
        f.close()
        #abro fichero en modo lectura
        with open (file1, "r") as fi:
            #guardo documento en un diccionari clave-valor
            todos = fi.readlines()
            todos = dict([tuple(line.split(',')) for line in todos])
        fi.close()
        #compruebo cuantos errores coinciden
        for i in errores:
            if i in todos:
                if errores[i] == todos[i]:
                    contador+=1

        print(f"Tras comprobar concidencias entre el fichero control y errores se han encontrado {contador} coincidencias de errores")
    except FileNotFoundError:
        print("Documento no encontrado")

def Borrar_Errores(file1,file2):
    print("Borrar Errores")
    try:
        #abro archivo metodo lectura
        with open (file2, "r") as f:
            #guardo documento en un diccionari clave-valor
            errores = f.readlines()
            errores = dict([tuple(line.split(',')) for line in errores])
        f.close()
        with open (file1, "r") as fi:
            #guardo documento en un diccionari clave-valor
            todos = fi.readlines()
            todos = dict([tuple(line.split(',')) for line in todos])
            #guardo antigua longitud antes de borrar
            longitud = len(todos)
        fi.close()
        #compruebo cuantos errores coinciden
        for i in errores:
            if i in todos:
                if errores[i] == todos[i]:
                    #borro del diccionario
                    del(todos[i])
        print(f"Errores eliminados\n\tAntes {longitud} registros\n\tAhora: {len(todos)} registros")
    #controlo la excepcion
    except FileNotFoundError:
        print("Documento no encontrado")

def menu():
    #pregunto que opcion quiere el usuario
    print("¿Que quieres hacer?")
    print("1. Consultar Errores")
    print("2. Existe Error")
    print("3. Borrar Errores")
    print("4. Salir")
    elegir = int(input())
    return elegir

def inicio():
    #metodo para ver en que opcion entra
    ficheroTodos = "ficheroexam3.txt"
    ficheroErrores = "ficheroexam4.txt"
    while True:
        opcion = menu()
        if opcion == 1:
            consulta_Errores(ficheroErrores)
        elif opcion == 2:
            Existe_Error(ficheroTodos,ficheroErrores)
        elif opcion == 3:
            Borrar_Errores(ficheroTodos,ficheroErrores)
        elif opcion == 4:
            print("Salir")
            break
        else:
            print("Opcion no valida")

inicio()