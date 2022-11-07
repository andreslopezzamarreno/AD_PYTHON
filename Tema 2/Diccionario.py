"""Crea un diccionario que tenga. nomrbre,apellido,alias,edad, género,estado Civil,mascota, nombre de la mascota"""

midiccionario = {
    'nombre':'',
    'apellido':'Lopez',
    'alias':'Zama',
    'edad':125,
    'genero':'Hombre',
    'estado civil':'soltero',
    'mascota':'perro',
    'nomrbe mascota':'klk',
}

for i in midiccionario:
    print(str(i) +" "+ str(midiccionario.get(i)))


"""Añadri nuevo campo al diccionario"""

midiccionario['nuevoCampo'] = 1000


"""controlar error de no encontrar la key"""

print(midiccionario.get('nuevoCampo2','no existe'))


"""Crea un diccionario que te pida por teclado los campos nomrbre,apellido,alias,edad, género,estado Civil,mascota, nombre de la mascota"""
"""
for i in midiccionario:
    variable = input("Introcuce campo " + i)
    midiccionario[i] = variable

for i in midiccionario:
    print(str(i) +" "+ str(midiccionario.get(i)))
"""
"""crea un programa que tenga un diccionario con marcas de zaparillas y su precio(por consola)
debera pedir el numero que queremos que el mayorista nos triga y ver cuanto nos vale el total
de cada zapatilla
entrada: nombre zapatilla, y cuantas queremos
salida: el coste total es: (total compra) y el coste por marca es:(el se esa marca en concreto)"""

diccionadio = {}
diccionariovacio = {}
salida = "s"
costeTotal = 0
while(salida != "si"):
    marca = input("marca")
    precio = input("precio")
    diccionadio[marca] = precio
    salida = input("Salir(si/no)\n")

salida = "no"
for i in diccionadio:
    print(str(i) +" "+ str(diccionadio.get(i)))

for i in diccionadio:
    numero = input("¿cuantas quieres de " + i + " ?")
    diccionariovacio[i] = numero

for i in diccionariovacio:
    precio2 = int(diccionariovacio.get(i)) * int(diccionadio.get(i))
    print(str(i) +"-> coste por " +str(diccionariovacio.get(i)) +" zapatillas: " + str(precio2))
    costeTotal += precio2

print("El coste total es: " + str(costeTotal))
