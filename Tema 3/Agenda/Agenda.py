#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Crear el fichero (vacío) que contenga los nombres y teléfonos de clientes. El fichero se llamará “miagenda.txt
Deberá comprobarse si el fichero existe o no.
Si no existe, el programa pedirá si queremos crearlo
Si existe, deberá pedir si queremos dejarlo en blanco
'''
nombre_archivo = "miagenda.txt"
def crearFichero():
    try:
        with open(nombre_archivo) as f:
            opcion = input("¿Quieres dejarlo en blanco?(1/0)")
            if int(opcion) == 1:
                file = open(nombre_archivo,"w")
                file.truncate()
    except FileNotFoundError:
        opcion = input("No existe el fichero.\n¿Quieres crearlo?(1/0)")
        if int(opcion) == 1:
            file = open(nombre_archivo,"w")
            file.close()


'''
- Podrá añadir al fichero un nuevo cliente, siguiendo la estructura en pareja: nombre,teléfono.
    Por ejemplo:
    r2d2,6666666666
    harry,888888888
    neo,811081108
    El formato es: Nombre del cliente y teléfono separados por una coma y cada cliente en una línea diferente.
    No deberán haber saltos de línea al principio o al final del documento. No habrá nombres repetidos. 
    Se deberá distinguir entre mayúsculas y minúsculas. 
'''
def añadirContacto():
    comprobar = True
    file = open(nombre_archivo,"r+")
    mensaje = file.readlines()
    contacto = input("Introduce contacto: (nombre,telefono)")
    if len(contacto.split(",")) == 2:
        for line in mensaje:
            if line.split(",")[0] == contacto.split(",")[0]:
                comprobar = False
    if comprobar:
        file.write(contacto+'\n')
    else:
        print("Contacto existente")
    file.close()


'''
- Se podrá consultar el número de teléfono de un cliente, para lo cual el programa nos preguntará el nombre del cliente del que
    necesitamos saber su teléfono.
'''
def consultarTelefono():
    file = open(nombre_archivo,"r")
    contactos = file.readlines()
    contacto = input("Introduce nombre de contacto:")
    for line in contactos:
        nombre = line.split(",")[0]
        numero = line.split(",")[1]
        if contacto == nombre:
            print("El numero de "+nombre+" es " + numero)
            break
    file.close()

'''
- Se podrá eliminar un cliente y su teléfono de la lista, quedando el fichero si dicho cliente.
'''
def borrarContacto():
    file = open(nombre_archivo,"r+")
    contactos = file.readlines()
    contacto = input("Introduce nombre de contacto:")
    contenido = dict([(line.split(','))for line in contactos])
    if contacto in contenido:
        #por terminar
        print(contacto)
    file.close()



'''
- Crea un menú que permita gestionar la agenda. El menú deberá llamar a las funciones:
    · Crear fichero
    · Añadir contacto
    · Consultar teléfono
    · Borrar contacto
    · Salir
'''
opcion = 0
while True:
    opcion = int(input("""Que quieres hacer ?
    1.Crear fichero
    2.Añadir Contacto
    3.Consultar Telefono
    4.Borrar Contacto
    5.Salir
    """))

    if opcion == 1:
        crearFichero()
    elif opcion == 2:
        añadirContacto()
    elif opcion == 3:
        consultarTelefono()
    elif opcion == 4:
        borrarContacto()
    elif opcion == 5:
        print("Salir")
        break
    else:
        print("Opcion no valida\n")
