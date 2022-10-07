# suma,resta,multip,divid,exponente, y otra que te inventes
import math

a = int(input("introduce un numero"))
b = int(input("introduce otro numero"))


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


def todas(x, y):
    suma(x, y)
    resta(x, y)
    multiplicacion(x, y)
    division(x, y)
    exponente(x, y)
    inventada(x, y)


todas(a, b)
