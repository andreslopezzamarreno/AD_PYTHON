#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#Pregunta 5
while True:
    try:
        opcion=int(input("Introduce una opción del 1 al 3:"))
        if opcion==1:
            print("opción 1")
        elif opcion==2:
            print("opción 2")
        elif opcion==3:
            print("opcion 3")
        else:
            break
    except ValueError:
        print('Ha pulsado una tecla, por favor introduzca un número')

#Pregunta 6
midiccionario = {
    'nombre': input("¿nombre?"),
    'apellido': input("¿Primer apellido?"),
    'edad': int(input("¿edad?")),
    'telefono': int(input("¿Telefono?"))
}

print(f"{midiccionario['nombre']} {midiccionario['apellido']} tiene {midiccionario['edad']} años y su telefono es {midiccionario['telefono']}")

#Pregunta 7.A
with open ("ficheroexam1.txt", "w") as f:
    f.write("-----------\n")
    numero = int(input("Escribe un numero mayor que 0"))
    for numero in range(numero+1):
        f.write(f"El numero es:{str(numero)}\n")
f.close()

#Pregunta 7.B
with open ("ficheroexam1.txt", "a") as f:
    f.write("-----------\n")
    numero = int(input("Escribe un numero mayor que 0"))
    for numero in range(numero+1):
        f.write(f"El numero es:{str(numero)}\n")
f.close()


#Pregunta 8.A
nA = int(input("Numero 1"))
nB = int(input("Numero 2"))
nC = int(input("Numero 3"))
def operacion(A,B,C):
    return (A+B)*C

resultado = operacion(nA,nB,nC)
with open ("ficheroexam2.txt", "w") as f:
    for line in range(resultado):
        f.write(f"El Resultado es: {resultado} y esta es la linea {line+1}\n")
f.close()


#Pregunta 8.B
nA = int(input("Numero 1"))
nB = int(input("Numero 2"))
nC = int(input("Numero 3"))
def operacion(A,B,C):
    return (A+B)*C

resultado = operacion(nA,nB,nC)
with open ("ficheroexam2.txt", "w+") as f:
    for line in range(resultado):
        f.write(f"El Resultado es: {resultado} y esta es la linea {line+1}\n")
f.close()

with open ("ficheroexam2.txt", "r") as f:
    texto=(linea for i,linea in enumerate(f) if i>=0 and i<nA+nB)
    print(f"Ahora se mostrara el contenido de calcular {nA} + {nB} = {nA+nB} ")
    for linea in texto:
        print(linea)
f.close()

#Pregunta 8.C
nA = int(input("Numero 1"))
nB = int(input("Numero 2"))
nC = int(input("Numero 3"))
def operacion(A,B,C):
    return (A+B)*C

resultado = operacion(nA,nB,nC)
with open ("ficheroexam2.txt", "w+") as f:
    for line in range(resultado):
        f.write(f"El Resultado es: {resultado} y esta es la linea {line+1}\n")
f.close()

fichero = "ficheroexam2.txt"

try:
    with open (fichero, "r") as f:
        texto=(linea for i,linea in enumerate(f) if i>=0 and i<nA+nB)
        for linea in texto:
            print(linea)
    f.close()
except FileNotFoundError:
    print(f"el fichero {fichero} no existe!")
'''
#Pregunta 9
def consulta_Errores():
    print("Consulta errores")


def Existe_Error():
    print("Existe Error")

def Borrar_Errores():
    print("Borrar Errores")


def menu(opcion):
    if opcion == 1:
        consulta_Errores()
    elif opcion == 2:
        Existe_Error()
    elif opcion == 3:
        Borrar_Errores()
    elif opcion == 4:
        print("Salir")
    else:
        print("Opcion no valida")

def inicio():
