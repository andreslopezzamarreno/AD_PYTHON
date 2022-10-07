
from http.client import SWITCHING_PROTOCOLS
from sys import setswitchinterval


print("klk")

a = 5

print(a)
a = "hola que tal"

# type(a)
"""list[] = Arrylist en Java
tuplas() = Array en Java"""
# Esto es una lista
lista = ["casa", "coche", "puerta"]
print(lista)
print(lista[1])
lista.append(3)
print(lista)

"""Añade a la lista lo introcucio y cada caracter
es un elemento"""
lista.extend("Curso de informatica")

# introduce en la posicion el valor
lista.insert(3, "cohete")

a = 9
b = 6

if a > b:
    print(" es mayor que ")


a = 2+4
if a == 4:
    print("A es igual a cuatro")
elif a == 5:
    print("A es igual a cinco")
elif a == 6:
    print("A es igual a seis")
else:
    print("No se cumple la condicion")

#introduce dos años y decir si la diferencia es mayor de 100 o no
año = int(input("Dime un año: "))
año2 = int(input("Dime otro año: "))
diferecia = abs(año - año2)
if diferecia >= 100:
    print("La diferencia es mas de un siglo")
else:
    print("La diferencia es menos de un siglo")


for palabra in lista:
    print(palabra)


#pregunta si quieres pares impares o todos y te los imprime
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

opcion = int(input("1:pares\n2:impares\n3.todos"))

if opcion == 1: 
        for num in numeros:
            if num % 2 == 0:
                print(num, end=" ")
                pass
elif opcion == 2: 
        for num in numeros:
            if num % 2 != 0:
                print(num, end=" ")
elif opcion == 3: 
        for num in numeros:
            print(num, end=" ")

print()
palabras = ["peine","pelo","ventana","refrigerador","adolescente","dentista","asesino"]

#imprime la longitud de todas las palabras
for caracteres in palabras:
    print((caracteres),('###longitud'),(len(caracteres)))

frase = "hola estoy programando en python"
a = 0

caracter1 = str(input("Que letra quieres"))
for caracter in frase:
    if caracter == str(caracter1):
        a += 1

print(a)