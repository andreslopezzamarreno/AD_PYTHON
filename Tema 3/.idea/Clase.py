'''
Escribe un programa en PYTHON QUE ESCRIBA DE LA FORMA QUE queráis en
un fichero llamado "ficheroenpython.txt" el siguiente mensaje:
with open() as f
    f.write()
    f.close()
'''
'''
with open ("ficheroenpython.txt","w") as f:
    f.write("with open() as f\n f.write()\n f.close()")
f.close()
'''
'''
Escribe un progrma que pida por teclado un nro postivo entre 1 y 100 y lo guarde 
en un fichero llamado "ejercicio-100.txt"
'''
'''
nro=int(input("ingrese un nro entre el 1 y 100"))
nombrefichero="ejercicio1-100.txt"
while nro >0 and nro <100:
    numero = int(input("El numero debe ser entre 1 y 100. Inténtelo de nuevo \n"))

    with open(nombrefichero,"w") as f:
        f.write(str(nro))
    f.close()
'''

'''
Escribo un programa que pida por teclado un nro positivo entre 1 y 10 y guarde en un 
fichero llamado "ejercicio2-tabla.txt" la tabla de multiplicacar de l nro introducido.
9x1=0
9x2=18
'''
'''
nro=int(input("ingrese un nro entre el 1 y 10 \n"))
nombFichero="ejercicio2-tabla.txt"
while nro >0 and nro <10:
    print("realizado en fichero")
    with open(nombFichero, "w") as f:
        for i in range(1,11):
            f.write(str(i)+"x" +str(nro)+"="+str(i*nro)+"\n")
    nro=int(input("ingrese el siguiente nro entre el 1 y 10 \n"))
    f.close()
'''
'''
Modificar ejercicio 2 para que el fichero tenga el nombre del numero con el que se crea la tabla
de multiplicar. Por ejemplo, si se introduce por teclado el 9, que el fichero se llame
"ejercicio2-tablaDel9.txt"
'''
'''
numero = int(input("Escribe un numero del 1 al 10 para hallar su tabla \n"))

while numero < 1 or numero > 10:
   numero = int(input("El numero debe ser entre 1 y 10. Inténtelo de nuevo \n"))

nombreFichero = "Ejercicio2-tablaDel"+str(numero)+".txt"
with open(nombreFichero,"w") as f:
   for i in range(0,11):
       solucion = numero * i
       f.write(str(numero)+"x"+str(i)+"="+str(solucion)+"\n")
f.close()
'''
'''
Escribe un progrmaa que pida un nro entero positivo entre n 1 y 10,
y en base al nro leido ,busque el fichero llamado:"fichero-tabladel-n.txt.Este fichero
  contendrá la tabla de multiplicar del nro n introducido por teclado y deberá mostrarse
por pantalla.Si el fichero no existe,deberá indicarse por pantalla un mensaje que avise del programa"
'''

"""
## Me falta ver video antes hora 10:13
"""

"""
Escribir un programa en py que lea un nro n por teclado y a partir de ese nro,lea las n 
primeras lineas del fichero creado en el ejercicio 2
"""
"""
nro=int(input("ingrese el nro \n"))
nomFichero="ejercicio2-tabla.txt"

with open(nomFichero, "w") as f:
    texto=(linea for i, linea in enumerate(f)if  i>=0 and i<nro)  #enumerate cuenta líneas
    for linea in texto:
        print(linea)
f.close()
"""

"""
Apellido, edad (18),género,Padres(James,Lili)
"""


MiDiccionario = {
    'Nombre':"Harry",
    'Apellido':"Potter",
    'edad':"18",
    'Genero':"Masculimo",
    'Padres':["jame","Lili"]
}
#2
print(MiDiccionario)
#3
print(MiDiccionario["Apellido"],"\n\n")
#4
print(MiDiccionario["Padres"][0:2])# 0desde donde:2 hasta donde
#dime el VALOR del segundo elemento de mi diccionario del campo padres
print(MiDiccionario["Padres"][0])
#5
#print(MiDiccionario["Edad"])
MiDiccionario["Edad"]=22
print(MiDiccionario["Edad"])
#6 Añador im campo "Grupo nuevo (Al final)
MiDiccionario["Grupo "]=""
print(MiDiccionario)
#7 Cambiar el nombre de una clave por otro.Por ejemplo
#cambiar la clave Grupo por la clave Casa .Sin necesidad
#usar un for para recorrer la clave ni el diccionario
'''MiDiccionario["Casa"]=MiDiccionario.pop("Grupo")
print(MiDiccionario)'''
#8 Borrar la clave-valor
#del MiDiccionario["Edad"]
#la forma esctricta
#del (MiDiccionario["Edad"]) #ESTA SIRVE PARA MI VERSION
print(MiDiccionario)
#9 DOS FORMAS DE OBTENER EL VALOR DE UNA CLAVE
print(MiDiccionario["Apellido"])#forma 1
print(MiDiccionario.get("Apellido"))#forma 2:dicc.get
#10 Añadir a una variable el valor de una clave
valorvariable=MiDiccionario.get("Apellido")
print(valorvariable)
#11 Imprimir las claves del diccionario:.keys()
print(MiDiccionario.keys())
#12Imprimir todos los valores: .value
print(MiDiccionario.values())

#-------------------
#TUPLAS TUPLAS TUPLAS TUPLAS TUPLAS
#------------------

#13 Crear una tupla:()
Cosas = ("casa","puerta","reloj","mesa","silla","banco","cuadro"
         ,"alfombra")
Numeros =(1,2,3,4,55)

#14 Cómo ver el par (clave-valor) de un diccionario
print("\n\n ----------")
print(MiDiccionario.items())

Numeros2 =[111,222,333,444,555,666]

#15 Slice: vamos a imprimir partes (rebanadas)de una tupla
#vamos a seleccionar (imprimir) los tres primeros elementos de la tupla
print(Numeros2)
print(Numeros2[0:3])
print(Numeros2[1:3])
print(Numeros2[:-2])#con un - indico desde el final
print(Numeros2[2:])
print(Numeros2[-2])
#16: cómo saber la longitud de un diccionario
print("\n\n --- LONGITUD DICCIONARIO ----")
print(len(MiDiccionario))
#17:cómo saber la longitud de una clave de un diccionario
#quiero saber la longitud de la clave padres, es decir cuantos elementos
# contiene esa clave,que deberian ser 2
print("\n\n --- LONGITUD CLAVE DE DICCIONARIO ----")
print(len(MiDiccionario["Padres"]))
print(len(MiDiccionario))

"""
Escribe el siguiente texto y pártelo
yton es un lenguahe de programacion que permite
      tipar pero no permite compilar,ya que es un lenguaje interpretado"
      
"""
texto="Pyton es un lenguahe de programacion que permite" \
      " tipar pero no permite compilar,ya que es un lenguaje interpretado"
print(texto)
print(texto.split())
print(texto.split(","))

"""
#20 Crear un programa que a partir del fichero de texto:"prueba1.txt", el cual contiene EXÁCTAMENTE esto:
A,1
B,2
C,3
D,4

Abra el fichero en modo lectura y para cada línea del fichero, imprima:
20.a: el contenido de la línea
20.b el contenido de cada línea desglosado por caracteres:
->("A",",","1"\n)
20.c el contenido de cada línea en formato "primer elemento","segundo elemento"(o lo que es lo mismo clave,valor):
("A","1"\n)
"""

#pista
print("\n\n---TUPLEANDO---")
mitupla = tuple([1,4,6])
print(mitupla)

mitupla2 = tuple("texto")
print(mitupla2)

mitupla3 = tuple({4:'one',6:'two'})
print(mitupla3)
print(mitupla3[0])

#como crear un diccionario directamente: dict
midic2= dict(nombre="lm",altura = 195,ojos= "azules")
print(midic2)

'''Pasos a seguir para el eje20
- abrir el fichero en modo lectura
- guardar el contenido del fichero en una variable
- cerrar el fichero
- iterar sobre el contenido cada linea
- imprimir lo que se pide:
    a.cada linea
    b.tuplear
    c.tuplear'''

midic2= dict(nombre="lm",altura = 195,ojos= "azules")
print(midic2)

file = "prueba1.txt"
f = open(file,'r')
contenido = f.readlines()
f.close()

line = str()
for line in contenido:
    print("el contenido de cada linea es: ",line)
    print(tuple(line))
    print(tuple(line.split(',')))

"""
#20 Crear un programa que a partir del fichero de texto:"prueba2.txt", el cual contiene EXÁCTAMENTE esto:
A,1
B,2
C,3
D,4

Abra el fichero en modo lectura e indique si una letra introducida por teclado esta dentro del fichero,
y de estarlo que valor tiene asociado
En caso de no estar la letra introducida, mostraré un mensaje indicado
"la letra leida:" letra leida "no se encuentra en el fichero".
"""
file = "prueba1.txt"
f = open(file,'r')
contenido = f.readlines()
f.close()
letra = input("introduce una letra a buscar: ")
for line in contenido:
    linea = tuple(line.split(','))
    if linea[0] == letra:
        print("la letra leida es ",letra," dato asociado ",linea[1])
    else:
        print("La letra ",letra, " no esta")

#otra forma
letra = input("introduce una letra a buscar: ")
contenido = dict([tuple(line.split(','))for line in contenido])
if letra in contenido:
    print("la letra leida es ",letra," dato asociado ",contenido[letra])
else:
    print("La letra ",letra," no esta")
