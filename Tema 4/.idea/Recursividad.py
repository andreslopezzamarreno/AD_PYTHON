'''Datos recursivos'''

'''
1- Calcula el factorial de un número
F!(n)= n*f(n-1)
si n=1->1

2- Multiplicación de dos números mayores de cero

3- MCD de dos números (mayores de cero)(Máximo común divisor)

4- Exponente de dos números (n elevado a m)

5- resta de dos números'''
def menu():
    # pregunto que opcion quiere el usuario
    print("¿Que quieres hacer?")
    print("1. Factorial")
    print("2. Multiplicar dos numeros")
    print("3. MCD de dos numeros")
    print("4. Exponente(Un numero de un numero a otro)")
    print("5. Resta de dos numeros")
    print("6. Salir")
    elegir = int(input())
    return elegir

def factorial(numero):
    if numero== 1:
        return numero
    else:
        resultado = numero * factorial(numero-1)
        return resultado

def factorialIterativo(numero):
    resultado = 1
    for i in reversed(range(numero)):
        if i != 0:
            numero *= i
    return numero


def multiplicacion(num1,num2):
    if num2 == 0:
        return num2
    else:
        resultado = num1 + multiplicacion(num1,num2-1)
        return resultado

def multiplicacionIterativa(num1, num2):
    return num1*num2

def mcd(num1,num2):
    if num2 == 0:
        return num1
    else:
        return mcd(num2,num1%num2)

def mcdIterativo(num1,num2):
    num= 1
    while num2!=0:
        num = num2
        num2 = num1%num2
        num1 = num
    return num1

def exponente(num1,num2):
    if num2 == 1:
        return num1
    else:
        resultado = num1 * exponente(num1,num2-1)
        return resultado

def exponenteIterativo(num1,num2):
    resultado = 1
    for i in range(num2):
        resultado *= num1
    return resultado

def resta(num1,num2):
    '''restar 1 num2 veces'''
    if num2 == 0:
        return num1
    else:
        resultado = resta(num1,num2-1) -1
        return resultado

def restaIterativa(num1,num2):
    return num1-num2

def inicio():
    listaCompleta = []
    while True:
        opcion = menu()

        if opcion == 1:
            print("\nFactorial")
            numero = int(input("Dime un numero"))
            print("Recursivo: " +str(factorial(numero)))
            print("Iterativo: " +str(factorialIterativo(numero)))

        elif opcion == 2:
            print("\nMultiplicar dos numeros")
            numeroUno = int(input("Dime un numero"))
            numeroDos = int(input("Dime otro numero"))
            print("Recursivo: " +str(multiplicacion(numeroUno,numeroDos)))
            print("Iterativo: " +str(multiplicacionIterativa(numeroUno,numeroDos)))

        elif opcion == 3:
            print("\nMCD de dos numeros")
            numeroUno = int(input("Dime un numero"))
            numeroDos = int(input("Dime otro numero"))
            print("Recursivo: " +str(mcd(numeroUno,numeroDos)))
            print("Iterativo: " +str(mcdIterativo(numeroUno,numeroDos)))

        elif opcion == 4:
            print("\nExponente(Un numero de un numero a otro)")
            numeroUno = int(input("Dime un numero"))
            numeroDos = int(input("Dime otro numero"))
            print("Recursivo: " +str(exponente(numeroUno,numeroDos)))
            print("Iterativo: " +str(exponenteIterativo(numeroUno,numeroDos)))

        elif opcion == 5:
            print("\nResta de dos numeros")
            numeroUno = int(input("Dime un numero"))
            numeroDos = int(input("Dime otro numero"))
            print("Recursivo: " +str(resta(numeroUno,numeroDos)))
            print("Iterativo: " +str(restaIterativa(numeroUno,numeroDos)))

        elif opcion == 6:
            print("Salir")
            break;
        else:
            print("Opcion no valida")

inicio()
