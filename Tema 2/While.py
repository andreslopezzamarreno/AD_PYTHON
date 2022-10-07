import math


def suma(x, y):
    print("La suma es: ", x + y)


def resta(x, y):
    print("La resta es: ", x - y)


def multiplicacion(x, y):
    print("La multiplicacion es: ", x * y)


def division(x, y):
    print("La division es: ", x / y)


def exponente(x, y):
    print("El exponente es: ", x ** y)


def inventada(x, y):
    print("El logaritmo es: ", math.log(x, y))


def dameNumero():
    x = int(input("introduce un numero"))
    return x

def dameNumeros():
    x = int(input("introduce un numero"))
    y = int(input("introduce un numero"))
    return x ,y
opcion = 0
a = 0
b = 0
while True:
    opcion = int(input("""Que quieres hacer ?
    1.suma
    2.resta 
    3.multiplicacion
    4.division
    5.exponente
    6.logaritmo
    7.Salir"""))

    if opcion == 1:
        suma(dameNumero(),dameNumero())
    elif opcion == 2:
        a, b = dameNumeros()
        resta(a, b)
    elif opcion == 3:
        a, b = dameNumeros()
        multiplicacion(a, b)
    elif opcion == 4:
        a, b = dameNumeros()
        division(a, b)
    elif opcion == 5:
        a, b = dameNumeros()
        exponente(a, b)
    elif opcion == 6:
        a, b = dameNumeros()
        inventada(a, b)
    elif opcion == 7:
        print("Salir")
        break
